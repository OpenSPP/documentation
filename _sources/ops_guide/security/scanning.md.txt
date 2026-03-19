---
openspp:
  doc_status: draft
  products: [core]
---

# Security Scanning

**For:** Developers and system administrators running security scans against OpenSPP

OpenSPP uses automated CI security scanning via GitHub Actions, supplemented by local tools for dynamic testing. CI results appear in the GitHub Security tab (SARIF) and as workflow annotations.

## Quick Start

### CI (Automatic)

Security scans run automatically on:
- **Pull requests** to `19.0` — gitleaks, pip-audit, npm audit, semgrep, bandit
- **Pushes** to `19.0` — all of the above plus trivy (container + filesystem)
- **Weekly schedule** (Monday 2am UTC) — full suite

No setup required. Results appear in the GitHub Security tab and PR checks.

### Local (Manual)

```bash
make gitleaks-scan      # Secret detection
make dependency-scan    # pip-audit + npm audit
make trivy-scan         # Container image scan
make zap-scan           # OWASP ZAP baseline (requires running Odoo)
```

Reports are saved to `static/security/latest/`.

## Tool Reference

### Gitleaks

Scans the repository for hardcoded secrets, API keys, passwords, and private keys.

**CI:** Runs via `gitleaks/gitleaks-action@v2`. Uploads SARIF to GitHub Security tab. **Fails build** on findings.

**Local:** `scripts/gitleaks/run-gitleaks.sh`

| Option | Description |
|--------|-------------|
| `--ci` | Exit with error code 1 if secrets are found |
| `--report-dir=DIR` | Override report output directory |
| `--sarif` | Generate SARIF format output |
| `--baseline=FILE` | Ignore known secrets listed in baseline file |
| `--history` | Also scan full git history (default: current state only) |

**Output files:**

| File | Format | Content |
|------|--------|---------|
| `gitleaks.json` | JSON | Current working tree findings |
| `gitleaks.txt` | Text | Human-readable summary |
| `gitleaks-history.json` | JSON | Git history findings (with `--history`) |
| `gitleaks.sarif` | SARIF | GitHub Security tab format (with `--sarif`) |

**Configuration:** `.gitleaks.toml` at the repository root defines path-based allowlists for known false positives (test data, documentation examples, vendored libraries).

### pip-audit

Scans Python dependencies declared in `requirements*.txt` files against the OSV vulnerability database.

**CI:** Runs with pinned `pip-audit==2.8.0`. **Fails build** on findings.

**Local:** `scripts/dependency-scan.sh` (runs both pip-audit and npm audit)

| Option | Description |
|--------|-------------|
| `--ci` | Exit with error code 1 if vulnerabilities are found |
| `--report-dir=DIR` | Override report output directory |
| `--sarif` | Generate SARIF format output |

The script automatically discovers all `requirements*.txt` files, combines them, removes duplicates, and filters out VCS-sourced packages and packages with native build dependencies that cannot be resolved in a container (e.g., Fiona, GDAL). Skipped dependencies are logged as `::warning::` annotations.

**Output files:**

| File | Format | Content |
|------|--------|---------|
| `pip-audit.json` | JSON | Structured vulnerability data |
| `pip-audit.txt` | Text | Column-formatted summary |
| `pip-audit.sarif` | SARIF | GitHub Security tab format (with `--sarif`) |

### npm audit

Scans JavaScript dependencies in `package.json` / `package-lock.json` files.

**CI:** Runs with `--audit-level=high`. **Fails build** on high+ findings.

**Local:** Runs as part of `scripts/dependency-scan.sh`. Requires `package-lock.json` to exist alongside `package.json`. Each package directory is scanned independently.

**Output files:**

| File | Format | Content |
|------|--------|---------|
| `npm-audit-<name>.json` | JSON | Vulnerability data per package directory |
| `npm-audit-<name>.txt` | Text | Human-readable summary |

### Semgrep

Static analysis with custom Odoo security rules covering SQL injection, XSS, access control bypass, PII exposure, and more.

**CI:** Runs in `returntocorp/semgrep` container with `p/python`, `p/security-audit`, and `.semgrep/` custom rules. Uploads SARIF to GitHub Security tab. **Fails build** on error-severity findings.

**Configuration:** `.semgrep/odoo-security.yml` contains custom rules for Odoo-specific patterns.

### Bandit

Python security linter that checks for common security issues (shell injection, hardcoded passwords, insecure functions, etc.).

**CI:** Runs with `-ll -ii` (low confidence and low severity filtered out). Uploads SARIF to GitHub Security tab. **Fails build** on findings.

**Configuration:** `pyproject.toml` under `[tool.bandit]`.

### Trivy

Scans Docker container images for OS package and application dependency vulnerabilities, plus filesystem misconfiguration checks.

**CI:** Runs on push and schedule only (too slow for every PR). Builds the image from `docker/Dockerfile` (runtime stage) and scans it. Also runs filesystem misconfiguration scan. Uploads SARIF to GitHub Security tab. **Fails build** on CRITICAL/HIGH findings.

**Local:** `scripts/trivy/run-trivy.sh`

| Option | Description |
|--------|-------------|
| `--ci` | Exit with error code 1 on high/critical findings |
| `--image=NAME` | Image to scan (default: auto-detect from running containers) |
| `--report-dir=DIR` | Override report output directory |
| `--severity=LIST` | Severity filter (default: `CRITICAL,HIGH`) |
| `--sarif` | Generate SARIF format output |

**Output files:**

| File | Format | Content |
|------|--------|---------|
| `trivy-image.json` | JSON | Image vulnerability data |
| `trivy-image.txt` | Text | Table-formatted summary |
| `trivy-image.sarif` | SARIF | GitHub Security tab format (with `--sarif`) |
| `trivy-misconfig.json` | JSON | Dockerfile and IaC misconfigurations |

**Configuration:** `.trivyignore.yaml` at the repository root suppresses known false positives and accepted risks. Each entry includes a CVE ID, a statement explaining the risk acceptance, and an expiry date for periodic review. Policy: only suppress CVEs with no available fix in the target platform.

### OWASP ZAP (Local Only)

Passive web application scan that discovers unauthenticated attack surface — finds public endpoints, exposed admin interfaces, and misconfigured routes that should require authentication.

ZAP is **not run in CI** because it requires a running Odoo instance. Use it locally for surface discovery.

**Local:** `scripts/zap/run-baseline.sh` or `make zap-scan`

The scan is configured via `scripts/zap/zap-baseline.yaml`:
- Spiders up to depth 8 for a maximum of 10 minutes
- Waits up to 15 minutes for passive scan completion
- Excludes static assets and longpolling endpoints
- Generates both HTML and JSON reports

**Output files:**

| File | Format | Content |
|------|--------|---------|
| `zap_report.html` | HTML | Human-readable findings with risk ratings |
| `zap_report.json` | JSON | Machine-readable findings |

## CI Workflows

### Security Scanning (`.github/workflows/security.yml`)

| Job | Triggers | Fails Build On |
|-----|----------|----------------|
| gitleaks | PR, push, schedule | Any finding |
| dependency-scan | PR, push, schedule | Any vulnerability |
| semgrep | PR, push, schedule | Error-severity finding |
| bandit | PR, push, schedule | Any finding |
| trivy | Push, schedule | CRITICAL/HIGH finding |

### Other Security Workflows

| Workflow | Triggers | Purpose |
|----------|----------|---------|
| `pre-commit.yml` | PR, push, manual | Lint + format checks (includes ruff, prettier) |
| `code-analysis.yml` | PR, push, weekly, manual | GitHub CodeQL static analysis |

## Configuration Files

| File | Purpose |
|------|---------|
| `.gitleaks.toml` | Path-based allowlist for Gitleaks false positives |
| `.trivyignore.yaml` | CVE suppressions with expiry dates and risk statements |
| `.semgrep/odoo-security.yml` | Custom Semgrep rules for Odoo security patterns |
| `pyproject.toml` | Bandit configuration (under `[tool.bandit]`) |
| `scripts/zap/zap-baseline.yaml` | ZAP baseline scan configuration (spider settings, report formats) |
| `scripts/zap/zap-rules.conf` | ZAP rule overrides (enable/disable specific checks) |

### Trivy Ignore Format

Each entry in `.trivyignore.yaml` requires:

```yaml
vulnerabilities:
  - id: CVE-2023-XXXXX
    statement: "Explanation of why this is accepted"
    expiry_date: 2026-04-29  # Review date
```

When an entry expires, Trivy reports the vulnerability again, forcing periodic review. This prevents suppressions from becoming stale.

### Gitleaks Allowlist

The `.gitleaks.toml` file uses path-based rules (preferred over fingerprints, which break when line numbers shift):

```toml
[allowlist]
paths = [
    '''static/security/''',    # Scan reports
    '''/tests/data/''',        # Test data files
    '''docs/''',               # Documentation examples
]
```

## Interpreting Results

### Reading Findings

Each tool produces structured JSON output. Key fields to check:

- **Gitleaks:** `RuleID`, `File`, `StartLine`, `Secret` (truncated)
- **pip-audit:** `dependencies[].vulns[]` with CVE IDs and fix versions
- **Trivy:** `Results[].Vulnerabilities[]` with severity, CVE, and fixed version
- **ZAP:** `site[].alerts[]` with `riskdesc` (High/Medium/Low/Informational)
- **Semgrep:** `results[].check_id`, `path`, `start.line`
- **Bandit:** `results[].issue_severity`, `issue_confidence`, `filename`

### False Positive Triage

When a finding is a false positive:

1. **Gitleaks:** Add a path rule to `.gitleaks.toml`
2. **Trivy:** Add a CVE entry to `.trivyignore.yaml` with a statement and expiry date
3. **ZAP:** Adjust rule severity in `scripts/zap/zap-rules.conf`
4. **pip-audit/npm audit:** No suppression mechanism; upgrade the dependency or document the risk

### When to Add Ignores

Add a suppression only when:
- The finding is a confirmed false positive (e.g., example API key in documentation)
- The vulnerability does not apply to OpenSPP's usage context (e.g., a library vulnerability in a code path that OpenSPP never calls)
- No fix is available and the risk is documented and accepted

Always include a justification statement. Never suppress a finding without explaining why.

## Troubleshooting

### Docker Not Running

**Symptom:** Local scans fail with "Cannot connect to Docker daemon"

- Gitleaks, Trivy, and ZAP local scripts run inside Docker containers
- Start Docker Desktop or the Docker daemon before running scans
- CI does not require Docker setup (handled by GitHub Actions runners)

### ZAP Scan Timeout

**Symptom:** ZAP scan hangs or takes longer than expected

- The baseline scan has a 10-minute spider timeout and 15-minute passive scan timeout
- If Odoo is slow to respond, increase the `maxDuration` values in `scripts/zap/zap-baseline.yaml`
- Check that the target URL is reachable: `curl -sI http://localhost:8069/web/login`

### Trivy Database Download

**Symptom:** Trivy fails with "failed to download vulnerability DB"

- Trivy downloads its vulnerability database on first run (~30 MB)
- The database is cached in `~/.cache/trivy`
- If behind a proxy, set `HTTPS_PROXY` in the Docker run command
- For air-gapped environments, pre-download the database: `trivy image --download-db-only`

### pip-audit VCS Dependencies

**Symptom:** pip-audit fails with "could not install" errors

- Dependencies sourced from VCS (git+, svn+, hg+) and URL-based dependencies are filtered out automatically and logged as `::warning::` annotations
- Packages with native build dependencies (Fiona, GDAL) are also excluded because they require system libraries not available in the scanning container
- If a new package causes failures, add it to the exclusion filter in `scripts/dependency-scan.sh`

## Related Documentation

- Security overview: {doc}`index`
- Audit logging: {doc}`audit`
- Production hardening: {doc}`../deployment/production-hardening`
