#!/usr/bin/env python3
"""Check generated SEO documents, complete content, links and reproducibility."""
import json
import re
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

from build_seo import BASE, ROOT, build, path_for, plain


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.text = []
        self.hidden = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag in ('script', 'style'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden -= 1
        if tag in ('p', 'li', 'h1', 'h2', 'h3', 'h4', 'section', 'nav', 'header', 'footer'):
            self.text.append(' ')

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


def values(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from values(child)
    elif isinstance(value, list):
        for child in value:
            yield from values(child)
    elif value is not None:
        yield str(value)


def normalized(value):
    return re.sub(r'\s+', ' ', value).strip()


def check():
    entries = json.loads((ROOT / 'data.json').read_text())
    urls = [node.text for node in ET.parse(ROOT / 'sitemap.xml').iter()
            if node.tag.endswith('}loc')]
    expected = [BASE + p for p in ['/', '/database.html', '/monographs/']]
    expected += [BASE + path_for(d) for d in entries]
    assert set(urls) == set(expected) and len(urls) == len(expected), 'Sitemap mismatch'
    directory = Document((ROOT / 'monographs/index.html').read_text())
    directory_links = {a.get('href') for tag, a in directory.tags if tag == 'a'}
    titles = set()
    for entry in entries:
        path = path_for(entry)
        assert path in directory_links, f'Directory missing {path}'
        raw = (ROOT / path.lstrip('/')).read_text()
        doc = Document(raw)
        visible = normalized(''.join(doc.text))
        assert sum(tag == 'h1' for tag, _ in doc.tags) == 1, path
        canonical = [a['href'] for tag, a in doc.tags
                     if tag == 'link' and a.get('rel') == 'canonical']
        assert canonical == [BASE + path], path
        title = re.search(r'<title>(.*?)</title>', raw)[1]
        assert title not in titles, f'Duplicate title: {title}'
        titles.add(title)
        for key in ('narrative_summary', 'clinical_data', 'sources'):
            for value in values(entry.get(key, {})):
                assert normalized(plain(value)) in visible, f'Missing {key} content in {path}: {value[:60]}'
        for structured in re.findall(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
            json.loads(structured)
        for tag, attrs in doc.tags:
            if tag == 'script':
                assert attrs.get('type') == 'application/ld+json', path
            if tag == 'a' and attrs.get('href', '').startswith('/'):
                target = ROOT / attrs['href'].lstrip('/')
                assert target.exists(), f'Broken internal link in {path}: {target}'
    with tempfile.TemporaryDirectory() as temporary:
        output = Path(temporary)
        build(ROOT / 'data.json', output)
        for generated in output.rglob('*'):
            if generated.is_file():
                relative = generated.relative_to(output)
                assert generated.read_bytes() == (ROOT / relative).read_bytes(), f'Stale generated file: {relative}'
    print(f'PASS: {len(entries)} complete monographs; {len(urls)} sitemap URLs; unique titles, canonicals, JSON-LD, internal links and deterministic output.')


if __name__ == '__main__':
    check()
