# Monograph SEO

The 72 existing archive records (47 Plant, 25 Fungi) now have individual HTML
documents at `/monographs/<scientific-name-slug>.html`. These preserve the
original full narrative, clinical, safety and citation fields from `data.json`.
The directory at `/monographs/` links to every record without JavaScript.
Database cards retain the modal interaction and provide real links that can
also open in a new tab. Each modal links to its full standalone page.

Run after editing archive records:

```sh
python3 scripts/build_seo.py
python3 scripts/check_seo.py
```

Commit the generated `monographs/` and `sitemap.xml` alongside the source changes.
Slugs derive from scientific names; changing a scientific name changes its URL.
Review and add a permanent redirect in Nginx before renaming an existing record.
The generator rejects slug collisions rather than overwriting another record.

The web Dockerfile generates these documents again in a Python build stage so
the final image's data and pages stay synchronized. Only generated HTML and XML
are copied from that stage; Python, generation scripts and local admin tools
are not installed in the Nginx image. When staging a Docker deployment via
Proxmox, include `scripts/build_seo.py` at that relative path, `.dockerignore`,
the revised Dockerfile, `data.json`, public HTML and `nginx.conf` along with the
existing public assets. Never copy admin files or development secrets.

The new sitemap contains 75 URLs: homepage, database, monograph directory and
72 record pages. It deliberately excludes checkout, admin, and redirected grow
pages. No fabricated modification dates, review credentials or medical claims
are included in metadata or structured data.

Nginx returns real 404s for missing `/monographs/` paths and revalidates their
HTML. Existing API/TLS routes and security headers are unchanged.

These changes must be deployed before Google can discover the new documents.
After an explicitly authorized deployment and verification of the live pages,
resubmit `https://bmsarchive.com/sitemap.xml` in Search Console. Submission and
valid structured data do not guarantee indexing or rankings.

Further review: archive source quality and taxonomic duplicates require their
own evidence/taxonomy audits. This SEO change renders existing records as-is
and does not validate their medical claims or establish 72 distinct accepted taxa.

## Local verification (23 October 2026)

- `scripts/check_seo.py`: passed for all 72 complete monographs, 75 sitemap
  URLs, unique titles/canonicals, JSON-LD parsing, local link targets and
  reproducible generation.
- Inline scripts in homepage/database: `node --check` passed. All 72 JavaScript
  URL slugs match Python-generated paths.
- Safari: homepage and directory rendered; Curcuma and Ganoderma standalone
  pages rendered with complete sections; Reishi search, modal, Advanced mode,
  permanent-page navigation, list view, and filters (25 fungi / 47 plants)
  were exercised successfully.
- Adversarial generator checks: escaping, unsafe URL rejection, duplicate
  slug rejection and obsolete-output cleanup passed in temporary directories.
- Existing archive validator: no errors, seven pre-existing safety-text
  warnings across five records; data was not edited.
- Docker build and `nginx -t`: not run, executables unavailable. A batch HTTP
  check from the shell was blocked by local network sandboxing; individual
  pages were exercised through Safari instead. No production deployment or
  live checks of the new paths have occurred.

## Production deployment (23 October 2026)

PRE-DEPLOY AUDIT RESULT: PASS for the scoped SEO release.

- QA, security, architecture, operations and scientific rendering-preservation
  reviews completed. Existing scientific claims were not evidence-certified.
- Docker build succeeded in LXC 102 via the Proxmox host. Only the web service
  was recreated with `--no-deps --no-build`; API, payment assets, environment
  and persistent volumes were preserved.
- Candidate and active `nginx -t` passed. The pre-existing duplicate
  `text/html` gzip MIME warning remains non-blocking.
- Final image contains 73 monograph HTML documents (72 records plus directory)
  and excludes admin files, secrets, generation scripts and Python.
- All 75 public sitemap URLs returned HTTPS 200 and byte-matched the local
  documents. Security headers and monograph HTML revalidation were verified.
  A nonexistent monograph returned 404.
- Public `data.json` and the prior live checkout page retained their original
  SHA-256 hashes. No payment or newsletter submissions were performed.
- Search Console confirmed the sitemap was submitted, status `Succes`.
  Its discovered-page count still showed 2 immediately after submission;
  Google has not yet reported a fresh crawl of the expanded sitemap.
- Rollback image: `bms-archive-web:before-seo-20261023`.
  Source backup: `/opt/bms-seo-backup-20261023` in LXC 102.
- New active web image: `sha256:a5fd2f68a78a3484953e976b2074fd7a5e6c6da9c204b58b7549de6adb418bfb`.

Files deployed: Dockerfile, .dockerignore, nginx.conf, index.html, database.html,
unchanged data.json/robots.txt/tailwind.js/og-image.png/favicon.svg, and the
build-only `scripts/build_seo.py`. Sitemap and monograph HTML are generated
inside the Docker build. Unrelated local admin/API/checkout/e-book edits were
not deployed. Git synchronization was not part of this publication.
