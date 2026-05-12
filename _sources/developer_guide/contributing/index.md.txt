---
openspp:
  doc_status: draft
  products: [core]
---

# Contributing

**For: developers**

How to contribute code to OpenSPP: the coding standards, the pre-commit hook chain, the PR template, and the CI checks that have to pass. OpenSPP uses OCA tooling (pylint_odoo, maintainer-tools) plus an OpenSPP-specific linter suite that enforces the rules in `docs/principles/`.

## Prerequisites

- A GitHub account and a fork of [OpenSPP/OpenSPP2](https://github.com/OpenSPP/OpenSPP2)
- A working development environment — see {doc}`/developer_guide/setup/index`
- Python 3.12+ (ruff `target-version = "py312"`)
- Node.js 22 (pre-commit runs prettier and eslint through Node)

## How to use this section

1. Set up **your fork and branch** (the `19.0` branch is the active target)
2. Install **pre-commit hooks** before your first commit — they catch 95% of what CI would fail on
3. Follow the **code style** rules (ruff, pylint_odoo mandatory checks) and the **OpenSPP conventions** (naming, XML IDs, no PII in logs)
4. Open the PR against `19.0` using the template — the **CI checks** and a reviewer have to approve

## When do you need this?

| You are doing | Required reading |
|---------------|------------------|
| Any code change (fix, feature, refactor) | [Code style](#code-style), [Pre-commit hooks](#pre-commit-hooks), [PR workflow](#opening-a-pull-request) |
| Adding a new model or field | [OpenSPP conventions](#openspp-specific-conventions) (naming, XML IDs, ACLs) |
| Adding a new module | Plus {doc}`/developer_guide/custom_modules/index` for scaffold + manifest requirements |
| Touching API V2 endpoints | API-auth pre-commit hook runs — auth required by default, public endpoints need allowlist entry |
| Writing tests | Don't use `self.assertRaises((A, B))` — Odoo's assertRaises doesn't accept tuples |
| Documentation-only change | Pre-commit skips many hooks on `docs/`, but CI still runs — open the PR like any other |
| Security fix | See `.github/workflows/security.yml` and the {doc}`/developer_guide/security/index` guide |

## Fork, branch, and commit

OpenSPP targets **Odoo 19** on the `19.0` branch. Do not open PRs against `main` — the repo uses Odoo-style version branches.

```bash
# Fork on GitHub, then clone your fork
git clone git@github.com:YOUR-USERNAME/OpenSPP2.git
cd OpenSPP2
git remote add upstream https://github.com/OpenSPP/OpenSPP2.git

# Branch from 19.0
git fetch upstream
git checkout -b 19.0-fix-registrant-search upstream/19.0
```

Branch names are free-form (use what you need) but keep them descriptive. Commits should follow conventional commit style (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`) — the existing history is a reliable guide.

Module versions in `__manifest__.py` follow **Odoo convention** (`19.0.X.Y.Z`). Bump the version when you change public model behavior, add migrations, or ship a breaking change.

## Code style

Formatting and basic lint run via `ruff`, `pylint_odoo`, `prettier`, and `eslint` — all wired into pre-commit. You shouldn't hand-format anything.

### Ruff (Python)

Config in `.ruff.toml`:

| Setting | Value |
|---------|-------|
| Target version | `py312` |
| Line length | `120` |
| Enabled rules | `B` (bugbear), `C90` (mccabe), `E501` (line too long), `I` (isort), `UP` (pyupgrade) |
| McCabe complexity | `max-complexity = 25` |
| Import sections | `future` → `standard-library` → `third-party` → `odoo` → `odoo-addons` → `first-party` → `local-folder` |

Manifest files (`__manifest__.py`) get `B018, E501` ignored — useless expressions and long lines are fine there because the manifest is a dict literal.

### Pylint (`pylint_odoo`)

Two configs run:

- **`.pylintrc-mandatory`** — a small set of checks that **block CI** (e.g. `anomalous-backslash-in-string`, `assignment-from-none`, manifest-required keys). You must pass this.
- **`.pylintrc`** — a larger set of checks that run with `--exit-zero` (warnings only). Fix what you can; CI won't fail you on these, but reviewers may ask.

The mandatory config also enforces **manifest requirements** on every module:

| Manifest key | Required value |
|--------------|----------------|
| `license` | `AGPL-3`, `GPL-2[+]`, `GPL-3[+]`, or `LGPL-3` |
| `author` | Must include `OpenSPP.org` |
| `version` | Must start with `19.0` |
| `description`, `active` | **Deprecated** — do not use |

### Editorconfig

`.editorconfig` sets LF line endings, final newlines, UTF-8 charset, and indent:

- `.py`, `.xml`, `.css`, `.js`, `.less`, `.sass`, `.scss` → 4-space indent
- `.yml`, `.yaml`, `.json`, `.md`, `.rst` → 2-space indent

Almost every editor honors this automatically.

### Prettier + ESLint

Run over `.css/.htm/.html/.js/.jsx/.json/.less/.md/.scss/.toml/.ts/.xml/.yaml/.yml` files. Includes `@prettier/plugin-xml` so Odoo views get normalized too. Generated files (`readme/`, `static/description/index.html`, `static/lib/`) are excluded.

## OpenSPP-specific conventions

These rules are enforced by a custom linter suite in `scripts/lint/` and documented in `docs/principles/`. They go beyond standard Odoo conventions — a module that passes standard pylint_odoo can still fail OpenSPP lint.

### Naming conventions (error — blocks CI)

Documented in [`docs/principles/naming-conventions.md`](https://github.com/OpenSPP/OpenSPP2/blob/19.0/docs/principles/naming-conventions.md) and [ADR-001](https://github.com/OpenSPP/OpenSPP2/tree/19.0/docs/architecture/decisions). Enforced by `scripts/lint/check_naming.py`:

- **Model names** use `spp.*` namespace. `g2p.*` is deprecated (separate check: `openspp-no-g2p-namespace`).
- **Many2one** fields end in `_id` (e.g. `partner_id`, `program_id`). The linter has a built-in exception list of ~30 fields (geography: `country`, `state`, `district`, `region`, `province`, `city`, `village`; framework: `parent`, `company`, `currency`, `partner`, `user`, `categ`, `create_uid`, `write_uid`; audit: `created_by`, `approved_by`, `rejected_by`, `resolved_by`, etc.). Check `scripts/lint/check_naming.py` for the full list. Add project-specific exceptions in `.openspp-lint.yaml` under `rules.naming.many2one_exceptions`.
- **Boolean** fields use `is_*` or `has_*` prefix. A short allowlist (`bidirectional`, `recurring`, `active`) is built in; extend via `.openspp-lint.yaml` `rules.naming.boolean_exceptions`.
- **XML IDs** follow a fixed pattern per element type (view / action / menu / group / record) — enforced by `scripts/lint/check_xml_ids.py`.

### No PII in logs (warning)

Documented in [`docs/principles/error-handling.md`](https://github.com/OpenSPP/OpenSPP2/blob/19.0/docs/principles/error-handling.md). The `openspp-no-pii-in-logs` pygrep hook and `check_logger.py` both scan for `_logger.*(record.name | .national_id | .phone | .mobile | .email | .address | .birth_date | .tax_id | .bank_account)` — any match is a warning.

Don't log field values directly. Log IDs or hashed/masked representations:

```python
# Wrong — puts PII in the log stream
_logger.info("Created registrant %s (%s, %s)", partner.name, partner.email, partner.phone)

# Right — log the ID; operators can look it up if they have the access group
_logger.info("Created registrant id=%s", partner.id)
```

See the `spp_security` guide ({doc}`/developer_guide/security/index`) for the encrypted-field pattern.

### ACL files required (warning)

Every module needs `security/ir.model.access.csv` — enforced by `scripts/lint/check_acl.py`. If you add a new model and forget the ACL entry, the lint will flag it.

### Odoo 19 compatibility (warning)

Documented in [`docs/principles/odoo19-compatibility.md`](https://github.com/OpenSPP/OpenSPP2/blob/19.0/docs/principles/odoo19-compatibility.md). Enforced by `scripts/lint/check_odoo19.py`:

- Use `invisible="..."` attribute expressions, not the old `attrs={'invisible': [...]}` syntax
- Use the `Command` API for Many2many / One2many writes — `Command.link(id)` / `Command.set([ids])` instead of raw tuple literals `(4, id)` / `(6, 0, ids)`
- `group_expand` / `_read_group_*` methods drop the `order` parameter in Odoo 19 — the signature is `(self, records, domain)`, not the pre-17 `(self, records, domain, order)`

### Test style (warning)

`openspp-no-assertraises-tuple` catches `self.assertRaises((A, B), ...)`. Odoo's helper (unlike stdlib `unittest`) doesn't support a tuple of exceptions — you'll get a confusing failure at runtime. Use one `assertRaises` per exception.

### Performance anti-patterns (warning)

`scripts/lint/check_performance.py` flags:

- Offset pagination (`search([...], offset=N, limit=M)`) — prefer cursor-based pagination in API code
- `self.env.cr.commit()` inside a loop
- N+1 query patterns (iterating records and dereferencing related fields one-by-one)

### UI patterns (warning)

`scripts/lint/check_ui_patterns.py` flags missing `limit` on list views, missing `sample="1"` where appropriate, malformed XPath expressions, and statusbar placement issues.

## Pre-commit hooks

The single most useful thing you can do before your first commit: install pre-commit locally. Every PR has to pass `pre-commit run --all-files` in CI, and running it locally catches issues before they bounce back.

```bash
pip install pre-commit
pre-commit install

# One-off: run every hook on the whole tree (slow, but complete)
pre-commit run --all-files

# Normal workflow: runs automatically on `git commit`, only on staged files
git commit -m "fix: resolve search race condition"
```

### What the chain runs (in order)

The full chain is in `.pre-commit-config.yaml`. Highlights:

| Stage | Hooks | Purpose |
|-------|-------|---------|
| Local guards | `forbidden-files`, `en-po-files` | Reject copier `.rej` files and disallowed `en.po` |
| Packaging | `whool-init`, OCA `maintainer-tools` | Generate READMEs, normalize manifests, update addons table |
| OCA checks | `oca-checks-odoo-module`, `oca-checks-po` | Standard OCA module validation |
| Formatters | `prettier`, `eslint`, `ruff`, `ruff-format` | Auto-formatting — commit the result |
| Python lint | `pylint_odoo` (mandatory + optional configs) | Odoo-aware pylint |
| OpenSPP custom | `scripts/lint/check_*.py` hooks | Naming, XML IDs, ACLs, Odoo 19 compat, performance, UI, logger, API auth |
| Secrets & security | `gitleaks`, `bandit`, `semgrep` | Secret scanning + AST-based security analysis |

Some hooks auto-fix (`ruff --fix`, `ruff-format`, `prettier --write`, `eslint --fix`, `end-of-file-fixer`, `mixed-line-ending`). When they do, the commit is rejected so you can review and re-stage the changes:

```bash
# Typical cycle
git commit -m "feat: add registrant deduplication"
# ...pre-commit modifies files, commit aborts
git add -u           # stage the auto-fixes
git commit -m "feat: add registrant deduplication"
```

### Running the OpenSPP linter directly

The custom checks are also available as a unified runner, which is useful when you want JSON output for an editor plugin or scoped checking:

```bash
# All checks, summary format
python scripts/lint/openspp_lint.py --summary

# Only a specific module
python scripts/lint/openspp_lint.py --module spp_programs

# Only specific checks
python scripts/lint/openspp_lint.py --check naming xml_ids

# Errors only (hide warnings)
python scripts/lint/openspp_lint.py --severity error

# JSON output for CI or editor integration
python scripts/lint/openspp_lint.py --format json
```

Extend the defaults via `.openspp-lint.yaml` at the repo root (see the existing file for the schema — `rules.naming.boolean_exceptions`, `modules.*.allow_model_patterns`, etc.).

## Writing tests

Every non-trivial change needs tests. See {doc}`/developer_guide/custom_modules/testing` for the full pattern (test base class, role-based access testing, `@tagged("post_install", "-at_install")`).

The pre-commit chain does **not** run tests — they run in CI. To run them locally before pushing:

```bash
# Replace the module name with yours
spp test spp_my_module

# Or, if you don't have the `spp` helper, directly:
odoo -d openspp_test --test-enable --stop-after-init -i spp_my_module
```

## Opening a pull request

Open your PR against **`19.0`** (not `main`). The PR template is pre-filled with these sections — fill them all in:

```markdown
## Why is this change needed?

## How was the change implemented?

## New unit tests

## Unit tests executed by the author

## How to test manually

## Related links
```

Tips that reviewers will thank you for:

- **Why** — 1-2 sentences of motivation. Don't assume the reviewer has read the linked issue.
- **How** — the moving parts, not line-by-line narration. Call out anything non-obvious (an inherited model, a migration, a new dependency).
- **New unit tests** — list the test methods you added and which behavior each one locks in.
- **Unit tests executed by the author** — the `spp test ...` command you ran and the result. "All pass" without the command is not helpful.
- **How to test manually** — a step-by-step script. Include the demo module to install, the URL to hit, the expected outcome.
- **Related links** — issue, Linear ticket, spec in `openspp-modules-v2/docs/specs/`, or upstream OCA PR.

## CI checks that gate merge

On every PR, GitHub Actions runs these workflows from `.github/workflows/`:

| Workflow | What it does | How to fix a failure |
|----------|--------------|----------------------|
| `pre-commit.yml` | Runs `pre-commit run --all-files` | Run `pre-commit run --all-files` locally, commit the fixes |
| `ci.yml` | Detects which modules changed, runs their test suites on a Postgres+Odoo matrix | Reproduce with `spp test <module>`; check the job log for the failing test |
| `ci-full.yml` | Full test suite (manual dispatch) | Same as above — rarely needed unless your change crosses many modules |
| `code-analysis.yml` | Static analysis pass | Read the annotations on the PR; rerun `scripts/lint/openspp_lint.py` locally |
| `security.yml` | Bandit, Gitleaks, Semgrep | Inspect the flagged line; if it's a false positive, add a targeted `# nosec` or `# nosemgrep` with a justifying comment |
| `stale.yml` | Closes abandoned PRs — informational, not a gate | Keep the PR active |

The `detect-changes` step in `ci.yml` only runs tests for modules you touched (or declared dependents of). If you added a new module, make sure its `__manifest__.py` has the right `depends` list — otherwise CI may skip it.

## License and author requirements

OpenSPP is **LGPL-3.0**. New modules and files must carry an LGPL-3 (or AGPL-3 / GPL-2+ / GPL-3+) license declaration in the manifest. `pylint_odoo` enforces this — see the `license-allowed` list in `.pylintrc-mandatory`.

Every manifest must declare `author` containing `OpenSPP.org` (`manifest-required-authors` in `.pylintrc-mandatory`). Example:

```python
{
    "name": "My OpenSPP Module",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "depends": ["spp_security", "spp_registry"],
    # ...
}
```

Your name can be added to [CONTRIBUTORS.md](https://github.com/OpenSPP/OpenSPP2/blob/19.0/CONTRIBUTORS.md) after your first merged PR.

## Common mistakes

**Opening a PR against `main`.** OpenSPP uses Odoo-style version branches. The active target is `19.0`. Your PR will be closed and asked to retarget if you pick the wrong base.

**Skipping pre-commit locally, pushing, and watching CI fail.** The `pre-commit.yml` workflow runs exactly the same hooks as your laptop. You save a round trip by running them before pushing.

**Using `--no-verify` to bypass a failing hook.** If pre-commit fails, fix the underlying issue. Bypassing the hooks pushes the failure to CI, and the reviewer will ask you to address the same warnings there.

**Bumping the module version "just in case".** Version bumps matter for migrations and packaging. Bump when the change warrants it (public behavior, migration, new feature); don't bump for cosmetic refactors.

**Assuming the optional pylint checks don't matter.** They're `--exit-zero` in CI, so they don't block merge — but reviewers see them, and a PR that fixes all the warnings is easier to approve than one that leaves them.

**Logging `partner.name` or `partner.phone` in a warning message.** The PII-in-logs hook will catch you. This is not cosmetic: OpenSPP deployments route logs to external systems (syslog, CloudWatch, Loki). Once PII leaves the Odoo DB, consent and encryption controls no longer apply.

**Inheriting `spp.versioned.mixin` without overriding `_get_version_snapshot_fields()`.** The mixin captures nothing by default — your versions will be empty. See {doc}`/developer_guide/audit/index`.

**Submitting a PR without `How to test manually` filled in.** Reviewers lean on this section heavily. Fill it in even for "trivial" changes — what's obvious to you is rarely obvious to a reviewer who didn't live with the problem.

## See also

- {doc}`/developer_guide/setup/index` — setting up the dev environment before you start
- {doc}`/developer_guide/custom_modules/index` — module scaffold, manifest requirements, and the three-tier security pattern
- {doc}`/developer_guide/custom_modules/testing` — how to write tests that pass CI
- [`openspp-modules-v2/docs/principles/`](https://github.com/OpenSPP/OpenSPP2/tree/19.0/docs/principles) — the full set of OpenSPP development principles (naming, access rights, UI, performance, error handling)
- [`openspp-modules-v2/docs/architecture/decisions/`](https://github.com/OpenSPP/OpenSPP2/tree/19.0/docs/architecture/decisions) — ADRs that drive the conventions
