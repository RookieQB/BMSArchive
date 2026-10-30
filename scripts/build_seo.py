#!/usr/bin/env python3
"""Generate crawlable monographs and sitemap from data.json, without dependencies.

Run after archive edits: python3 scripts/build_seo.py
The Docker build also runs this generator so published HTML matches its data.
"""
import argparse
import html
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://bmsarchive.com'
DISCLAIMER = ('For educational and scientific research only. Not medical advice. '
              'Independently verify claims against the cited primary sources. '
              'Consult a qualified healthcare professional before using any plant or fungal preparation.')
LABELS = {
    'narrative_summary': 'Research overview', 'historical_use': 'Historical use',
    'modern_application': 'Modern research context', 'side_effects': 'Adverse effects',
    'contraindications': 'Contraindications', 'clinical_data': 'Clinical and phytochemical data',
    'used_part': 'Used part', 'primary_active_compounds': 'Primary active compounds',
    'mechanism_of_action': 'Mechanism of action', 'pharmacokinetics': 'Pharmacokinetics',
    'safety_and_interactions': 'Safety and interactions', 'special_precautions': 'Special precautions',
}
CSS = '''
:root{color-scheme:light;font-family:system-ui,-apple-system,sans-serif;color:#102318;background:#f4fbf5}
*{box-sizing:border-box}body{margin:0;line-height:1.7}a{color:#1c5235;text-underline-offset:4px}
a:hover{color:#0c2519}a:focus-visible{outline:3px solid #268050;outline-offset:4px}
header,main,footer{max-width:1000px;margin:auto;padding:24px}header{display:flex;gap:24px;flex-wrap:wrap;align-items:center}
.brand{font-weight:800;text-decoration:none;margin-right:auto}nav{display:flex;gap:20px;flex-wrap:wrap}
article,.panel{background:white;border:1px solid #d9e8dd;border-radius:18px;padding:clamp(20px,5vw,48px)}
h1{font-size:clamp(2rem,6vw,3.5rem);line-height:1.15;overflow-wrap:anywhere;margin:.4em 0}h2{line-height:1.3;margin-top:2em}
h3,h4{line-height:1.4}p,li{overflow-wrap:anywhere}section{scroll-margin-top:20px}
.eyebrow{font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:#486853}.common{font-size:1.3rem;color:#486853}
.notice{border-left:4px solid #268050;background:#eaf8ed;padding:16px 20px;border-radius:6px;font-size:.95rem}
.directory{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px}
.directory a{display:block;border:1px solid #d9e8dd;border-radius:12px;padding:16px;text-decoration:none;background:#fff}
.directory a:hover{background:#eaf8ed}.directory span{display:block;color:#486853;font-size:.9rem}
.sources li{padding:8px 0}footer{font-size:.9rem;color:#486853}.breadcrumb{font-size:.9rem;margin-bottom:20px}
@media(max-width:480px){header,main,footer{padding:16px}nav{gap:12px}article{border-radius:12px}}
'''


def esc(value):
    return html.escape(str(value), quote=True)


def slug(name):
    text = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')


def path_for(entry):
    return '/monographs/' + slug(entry['scientific_name']) + '.html'


def plain(value):
    return html.unescape(re.sub(r'</?[A-Za-z][^>]*>', '', str(value)))


def rich(value):
    # Preserve scientific emphasis/subscripts, but no attributes or executable HTML.
    safe = esc(value)
    for tag in ('strong', 'em', 'b', 'i', 'sub', 'sup'):
        safe = safe.replace(f'&lt;{tag}&gt;', f'<{tag}>').replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    return safe


def label(key):
    return LABELS.get(key, key.replace('_', ' ').capitalize())


def fields(value, level=2):
    if isinstance(value, dict):
        return ''.join(f'<section><h{level}>{esc(label(k))}</h{level}>'
                       f'{fields(v, min(level + 1, 6))}</section>' for k, v in value.items())
    if isinstance(value, list):
        return '<ul>' + ''.join(f'<li>{fields(v, level)}</li>' for v in value) + '</ul>'
    return '<p>' + rich(value) + '</p>' if value is not None else '<p>Not provided in the archive.</p>'


def source_link(url, text):
    parsed = urlsplit(url)
    if parsed.scheme in ('http', 'https') and parsed.netloc:
        return f'<a href="{esc(url)}" rel="noopener noreferrer">{esc(text)}</a>'
    return esc(text)


def sources(entry):
    source = entry.get('sources', {})
    refs = []
    for ref in source.get('cited_references', []):
        pmid = re.search(r'PMID:\s*(\d+)', ref)
        doi = re.search(r'DOI:\s*(10\.[^\s,]+)', ref)
        url = ('https://pubmed.ncbi.nlm.nih.gov/' + pmid[1] + '/' if pmid else
               'https://doi.org/' + doi[1].rstrip('.;)') if doi else '')
        refs.append('<li>' + source_link(url, ref) + '</li>')
    urls = ['<li>' + source_link(url, url) + '</li>' for url in source.get('top_studies_urls', [])]
    remaining = {k: v for k, v in source.items() if k not in ('cited_references', 'top_studies_urls')}
    return ('<section id="sources"><h2>Sources and references</h2>'
            + ('<ol class="sources">' + ''.join(refs) + '</ol>' if refs else '')
            + ('<h3>Additional source links</h3><ul class="sources">' + ''.join(urls) + '</ul>' if urls else '')
            + fields(remaining, 3) + '</section>')


def page(title, description, path, body, schema):
    structured = json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}">
<link rel="canonical" href="{BASE}{path}"><meta name="robots" content="index,follow">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:type" content="website">
<meta property="og:image" content="{BASE}/og-image.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><style>{CSS}</style>
<script type="application/ld+json">{structured}</script></head><body>
<header><a class="brand" href="/">BMS Archive</a><nav aria-label="Main navigation"><a href="/database.html">Search database</a><a href="/monographs/">All monographs</a></nav></header>
<main>{body}</main><footer><p>{esc(DISCLAIMER)}</p><a href="/">Home</a> · <a href="/database.html">Search and filters</a> · <a href="/monographs/">Monograph directory</a></footer>
</body></html>
'''


def links(entries):
    return '<ul class="directory">' + ''.join(
        f'<li><a href="{path_for(d)}"><em>{esc(d["scientific_name"])}</em>'
        f'<span>{esc(d["common_name"])}</span></a></li>' for d in entries) + '</ul>'


def build(data_path, output):
    entries = sorted(json.loads(data_path.read_text()), key=lambda d: d['scientific_name'])
    paths = [path_for(d) for d in entries]
    if not entries or len(paths) != len(set(paths)) or any(not slug(d['scientific_name']) for d in entries):
        raise ValueError('Archive must have records with unique, nonempty URL slugs.')
    directory = output / 'monographs'
    directory.mkdir(parents=True, exist_ok=True)
    for index, entry in enumerate(entries):
        name, common = entry['scientific_name'], entry['common_name']
        path = path_for(entry)
        title = f'{name} ({common}) | BMS Archive'
        description = f'{name} ({common}): research overview, active compounds, safety, interactions and source references in BMS Archive.'
        schema = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'WebPage', '@id': BASE + path, 'url': BASE + path, 'name': title,
             'description': description, 'inLanguage': 'en',
             'isPartOf': {'@type': 'WebSite', 'name': 'BMS Archive', 'url': BASE + '/'},
             'about': {'@type': 'Thing', 'name': name, 'alternateName': common}},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'BMS Archive', 'item': BASE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Monographs', 'item': BASE + '/monographs/'},
                {'@type': 'ListItem', 'position': 3, 'name': name, 'item': BASE + path}]}]}
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / '
                f'<a href="/monographs/">Monographs</a> / {esc(name)}</nav><article>'
                f'<p class="eyebrow">{esc(entry["type"])} · Scientific monograph</p>'
                f'<h1><em>{esc(name)}</em></h1><p class="common">{esc(common)}</p>'
                f'<p class="notice">{esc(DISCLAIMER)}</p>'
                f'<p>Research areas: {esc(", ".join(entry.get("primary_categories", [])))}</p>'
                '<nav aria-label="On this page"><a href="#overview">Overview</a> · '
                '<a href="#clinical">Clinical data and safety</a> · <a href="#sources">Sources</a></nav>'
                '<div id="overview">' + fields({'narrative_summary': entry.get('narrative_summary', {})}) + '</div>'
                '<div id="clinical">' + fields({'clinical_data': entry.get('clinical_data', {})}) + '</div>'
                + sources(entry) + '</article>')
        neighbors = [entries[i] for i in (index - 1, index + 1) if 0 <= i < len(entries)]
        body += '<section><h2>Continue browsing</h2>' + links(neighbors) + '</section>'
        (output / path.lstrip('/')).write_text(page(title, description, path, body, schema))
    groups = ''.join(f'<section id="{kind.lower()}"><h2>{heading}</h2>'
                     + links([d for d in entries if d['type'] == kind]) + '</section>'
                     for kind, heading in [('Plant', 'Plants'), ('Fungi', 'Fungi')])
    body = (f'<div class="panel"><p class="eyebrow">The complete archive</p><h1>Plant &amp; fungal monographs</h1>'
            f'<p>Browse all {len(entries)} archive records by scientific and common name. Each monograph includes '
            'research context, clinical data, safety information and source references.</p>'
            '<nav aria-label="Monograph groups"><a href="#plant">Plants</a> · <a href="#fungi">Fungi</a> · '
            '<a href="/database.html">Search and filter</a></nav>' + groups + '</div>')
    (directory / 'index.html').write_text(page('Plant & Fungal Monographs | BMS Archive',
        f'Browse {len(entries)} plant and fungal monographs with research context, active compounds, safety information and references.',
        '/monographs/', body, {'@context': 'https://schema.org', '@type': 'CollectionPage',
                              'name': 'Plant & Fungal Monographs', 'url': BASE + '/monographs/'}))
    # This directory is owned by the generator. Remove obsolete generated pages only.
    expected = {Path(p).name for p in paths} | {'index.html'}
    for old in directory.glob('*.html'):
        if old.name not in expected and 'Scientific monograph' in old.read_text():
            old.unlink()
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    root = ET.Element(ns + 'urlset')
    for path in ['/', '/database.html', '/monographs/'] + paths:
        ET.SubElement(ET.SubElement(root, ns + 'url'), ns + 'loc').text = BASE + path
    ET.ElementTree(root).write(output / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    print(f'Generated {len(entries)} monographs, directory and {len(paths) + 3} sitemap URLs.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'data.json')
    parser.add_argument('--output', type=Path, default=ROOT)
    args = parser.parse_args()
    build(args.data, args.output)
