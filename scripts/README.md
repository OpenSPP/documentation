# Documentation tracking scripts

These scripts are for **internal** documentation-maintenance workflows (they do not affect published content unless you choose to write metadata into pages).

## Per-page status tracking (`doc_status.py`)

OpenSPP documentation pages can optionally include a YAML frontmatter block that tracks the refresh/verification state:

```yaml
openspp:
  doc_status: unverified | drafted | validated
  validated_against: "optional context"
```

### Report current status

```bash
python3 scripts/doc_status.py report --format markdown --output DOC_STATUS_REPORT.md
```

### Initialize or update statuses (dry-run by default)

```bash
# Dry-run: show which files would change
python3 scripts/doc_status.py set --status unverified

# Apply changes
python3 scripts/doc_status.py set --status unverified --apply
```

### Notes

- The script skips auto-generated module docs under `docs/modules/**` by default.
- The frontmatter key names intentionally avoid “V2” terminology; it’s just a page status.

