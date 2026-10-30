# Plant batch production deployment — 2026-10-30

## Release

- Production site: https://bmsarchive.com/database.html
- Data file SHA-256: `d68912d878d6c4e87762915b4099a91c981982d9acb290f932e41ec12d3c3638`
- Archive: 82 entries (57 plants, 25 fungi); 10 plants added.
- Production backup: `/opt/bms-plants-backup-20261030-d68912d8/data.json`
- Rollback web image tag: `bms-archive-web:rollback-20261030-d68912d8`
- New web image: `sha256:8b36552a543f94d695d9e43b164a24bc7c7b8c55f245ae36cf6f5923cc13fb43`

## Procedure and checks

Before deployment, production data matched the pre-release SHA-256 `4031a772f400eb66a8cd0924a597bf0957b32c7dde174e4b5b0f6a44012e73e8`. Existing nginx configuration test passed. A dated copy of the old data and a rollback image tag were saved in the LXC.

Only `data.json` was transferred and replaced. The staged file matched the approved SHA-256 and parsed as 82 entries. The existing multi-stage web image build generated 82 monographs and 85 sitemap URLs. Candidate nginx configuration passed before the web service was recreated. The API service was not recreated; its container ID remained `d6b38e5c4a6071e6c783619105e09c01601824c7688ca73e514852cea482977b`.

Verified over certificate-validated HTTPS after deployment:

- Homepage, database, JSON and sitemap: HTTP 200.
- JSON count: 82.
- Sitemap URL count: 85.
- All ten new monograph pages: HTTP 200.
- Active nginx configuration test: passed.

Nginx reports an existing duplicate `text/html` gzip MIME warning at line 101; syntax and configuration tests pass. No API, checkout, admin, environment, volume or backend configuration was changed.

## Rollback

Restore `/opt/bms-plants-backup-20261030-d68912d8/data.json` to `/opt/bms-archive/data.json`, retag `bms-archive-web:rollback-20261030-d68912d8` as `bms-archive-web:latest`, then recreate only the web service and repeat HTTPS checks.

## Content scope

The profiles are educational summaries. Abstract-only numeric medicinal regimens were omitted. Full clinical risk-of-bias appraisal and licensed ESCOP/complete WHO monograph review were not performed; limitations and preparation-specific uncertainty remain documented in the research and QA reports.
