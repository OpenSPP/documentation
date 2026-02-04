---
openspp:
  doc_status: draft
  products: [core]
---

# Production Hardening

**For:** System administrators deploying OpenSPP to production

This guide covers hardening a single-node Docker Compose deployment using the reference `docker-compose.production.yml`. It applies to small-to-medium deployments (10k-100k beneficiaries) on a single VPS or cloud instance.

## Architecture Overview

The production stack runs four services behind a Traefik reverse proxy:

```{mermaid}
flowchart TB
    Internet((Internet))

    subgraph proxy["Traefik v3.2 (ports 80/443)"]
        direction TB
        TLS["TLS termination, headers, rate limiting"]
    end

    subgraph odoo["Odoo Services"]
        direction LR
        OdooHTTP["Odoo<br/>:8069<br/>(HTTP)"]
        OdooWS["Odoo WS<br/>:8072<br/>(WebSocket)"]
    end

    subgraph workers["Background Processing"]
        QueueWorker["Queue Worker<br/>(Odoo gevent mode)"]
    end

    subgraph db["Database"]
        PostgreSQL[("PostgreSQL 18<br/>PostGIS 3.6<br/>:5432")]
    end

    Internet --> proxy
    proxy --> OdooHTTP
    proxy --> OdooWS
    OdooHTTP --> PostgreSQL
    OdooWS --> PostgreSQL
    QueueWorker --> PostgreSQL
```

Traefik handles TLS termination, security headers, rate limiting, and database manager blocking. Odoo runs in multi-worker mode with a separate gevent-based queue worker for background jobs.

## HTTPS and TLS

Traefik obtains certificates automatically from Let's Encrypt using the HTTP-01 challenge. All HTTP traffic is redirected to HTTPS.

### Configuration

Set `ACME_EMAIL` in your `.env.production` file:

```bash
ACME_EMAIL=admin@example.org
DOMAIN=openspp.example.org
```

Traefik stores certificates in a Docker volume (`traefik_certs`) so they persist across restarts.

### HSTS

Strict-Transport-Security is enabled with a one-year max-age and includes subdomains:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

This tells browsers to only connect via HTTPS for the next year.

## Security Headers

The `odoo-headers` middleware injects the following response headers:

| Header | Value | Purpose |
|--------|-------|---------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Force HTTPS for 1 year |
| `X-Content-Type-Options` | `nosniff` | Prevent MIME-type sniffing |
| `X-Frame-Options` | `DENY` | Block framing (clickjacking protection) |
| `Content-Security-Policy` | `default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self' data:; frame-ancestors 'self'; base-uri 'self'; form-action 'self';` | Restrict resource loading origins |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limit referrer leakage to cross-origin requests |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=()` | Disable unused browser APIs |
| `X-XSS-Protection` | `1; mode=block` | Legacy XSS filter (browsers that lack CSP support) |
| `Server` | `OpenSPP` | Hide Werkzeug/Python version |

The CSP includes `'unsafe-inline'` and `'unsafe-eval'` for `script-src` because Odoo's web client requires inline scripts and `eval()` for its QWeb template engine.

## Database Manager Blocking

The Odoo database manager (`/web/database`) allows creating, duplicating, and dropping databases. In production this must be disabled.

The compose file uses two complementary mechanisms:

1. **`LIST_DB=False`** environment variable prevents Odoo from listing databases
2. **Traefik `block-dbmanager` middleware** redirects any request to `/web/database*` to `/web/login`

The Traefik rule uses a higher priority (`priority=20`) to match before the main Odoo router:

```yaml
# Traefik labels on the odoo service
- "traefik.http.routers.odoo-dbmanager.rule=Host(`${DOMAIN}`) && PathPrefix(`/web/database`)"
- "traefik.http.routers.odoo-dbmanager.priority=20"
- "traefik.http.middlewares.block-dbmanager.replacepathregex.regex=^/web/database.*"
- "traefik.http.middlewares.block-dbmanager.replacepathregex.replacement=/web/login"
```

Both layers are needed because `LIST_DB=False` alone does not block direct URL access to the database manager.

### Choose a Database Management Policy (Two Options)

Your security posture determines how strictly you lock down database creation and restore operations. Odoo supports two patterns; choose one explicitly and document it for your team:

**Option A — Strict hardening (recommended for production):**
- Odoo runs as a **non-superuser** with **NO CREATEDB**
- The database is created/owned by an admin role (not the Odoo role)
- The DB manager UI is effectively disabled (even with the master password)
- All create/drop/restore operations require an admin role outside Odoo

**Option B — Operational flexibility (acceptable for controlled environments):**
- Odoo role can **CREATEDB** (still not a superuser)
- DB manager UI can be used for backup/restore if needed
- Higher risk: a compromised Odoo user can create databases and exfiltrate data

If you choose Option A, you must provision roles explicitly (init script or external DBA tooling) rather than relying on the default container user.
When using the bundled PostgreSQL container, the role defined by `POSTGRES_USER` is created as a superuser by the official image initialization. For Option A, keep `POSTGRES_USER` as an admin role and create the `odoo` role with `NOSUPERUSER NOCREATEDB` in an init script.

#### Init Script Example (Option A)

If you use the bundled PostgreSQL container, place an SQL file in `/docker-entrypoint-initdb.d` so roles are created on first initialization. For example:

```sql
-- docker/initdb/01-create-roles.sql
CREATE ROLE odoo LOGIN PASSWORD 'strong-password-here' NOSUPERUSER NOCREATEDB;
CREATE ROLE openspp_admin LOGIN PASSWORD 'admin-password-here' SUPERUSER;
CREATE DATABASE openspp OWNER openspp_admin;
GRANT ALL PRIVILEGES ON DATABASE openspp TO odoo;
```

Mount the init directory in your database service (path is relative to the compose file directory):

```yaml
volumes:
  - ./initdb:/docker-entrypoint-initdb.d:ro
```

These scripts only run when the database data directory is empty. If the volume already exists, run the SQL manually as the admin role.

## Database Filter (dbfilter)

The `DB_FILTER` setting restricts which database Odoo will serve. This is critical for security in production.

```bash
# In .env.production
DB_NAME=openspp
DB_FILTER=^openspp$
```

The filter is a regular expression. The `^...$` anchors ensure an exact match, preventing access to other databases that might exist on the same PostgreSQL server.

Without a proper `dbfilter`:
- Attackers could probe for other databases
- Multi-tenant confusion could expose data across tenants
- The database selector might appear on the login page

The compose file sets `DB_FILTER` automatically based on `DB_NAME`:

```yaml
DB_FILTER: "^${DB_NAME:-openspp}$$"
```

## WebSocket Routing

Odoo 19 uses WebSocket connections on port 8072 for live updates (bus notifications, chat, presence). The `/websocket` path is routed to the longpolling service:

```yaml
- "traefik.http.routers.odoo-websocket.rule=Host(`${DOMAIN}`) && PathPrefix(`/websocket`)"
- "traefik.http.services.odoo-websocket.loadbalancer.server.port=8072"
```

This router has `priority=15` so it matches before the default Odoo router but after the database manager block.

If WebSocket routing is misconfigured, you will see:
- Chat messages not appearing in real time
- "Bus connection lost" warnings in the browser console
- Notifications requiring page refresh to appear

## Rate Limiting

The `odoo-ratelimit` middleware provides brute-force protection:

| Setting | Value | Meaning |
|---------|-------|---------|
| `average` | 50 | 50 requests per period allowed per source IP |
| `burst` | 100 | Up to 100 requests in a burst before throttling |
| `period` | 1m | Rate window is 1 minute |

Both `odoo-headers` and `odoo-ratelimit` are applied to the main Odoo router:

```yaml
- "traefik.http.routers.odoo.middlewares=odoo-headers,odoo-ratelimit"
```

### Tuning

- If legitimate users hit rate limits (e.g., during data imports via the UI), increase `average` and `burst`
- For higher security, reduce `average` to 20-30 for login-heavy deployments
- Rate limiting applies per source IP, so users behind a shared NAT may trigger limits sooner

## Brute Force Protection with fail2ban

For additional protection against brute-force attacks, configure fail2ban on the host to monitor Odoo login failures.

Odoo logs failed login attempts in this format:

```
2024-01-15 14:56:31,506 24849 INFO openspp odoo.addons.base.res.res_users: Login failed for db:openspp login:admin from 192.168.1.100
```

Create `/etc/fail2ban/jail.d/odoo.conf`:

```ini
[odoo-login]
enabled = true
port = http,https
filter = odoo-login
logpath = /var/log/odoo/odoo.log
bantime = 900
maxretry = 10
findtime = 60
```

Create `/etc/fail2ban/filter.d/odoo-login.conf`:

```ini
[Definition]
failregex = ^ \d+ INFO \S+ odoo.addons.base.res.res_users: Login failed for db:\S+ login:\S+ from <HOST>
ignoreregex =
```

This bans an IP for 15 minutes after 10 failed login attempts within 1 minute.

To use fail2ban with Docker, either:
1. Mount Odoo logs to the host filesystem
2. Use `docker logs` with a log driver that writes to syslog

## Cookie Security

Odoo uses Werkzeug as its HTTP server. Werkzeug 2.3+ sets `SameSite=Lax` on cookies by default, which prevents CSRF attacks from cross-origin requests.

Verify cookie flags in production:

```bash
curl -sI https://yourdomain.com/web/login | grep -i set-cookie
```

You should see `SameSite=Lax` and `Secure` on the `session_id` cookie.

**Note:** Traefik v3 does not support rewriting cookie flags natively (unlike nginx's `proxy_cookie_flags` directive). The `SameSite=Lax` flag relies on Werkzeug setting it at the application level, which it does by default in Odoo 19.

## PostgreSQL Hardening

### Non-Superuser Database User

The PostgreSQL user connecting to Odoo **must not be a superuser**. This limits the damage if an SQL injection vulnerability is exploited.

Use one of the two policies above:
- **Option A (strict):** `odoo` is **NOSUPERUSER NOCREATEDB**, database owned by admin role
- **Option B (flexible):** `odoo` is **NOSUPERUSER CREATEDB**, database owned by `odoo`

```sql
-- Option A (strict): admin-owned database, Odoo has no createdb
CREATE ROLE odoo LOGIN PASSWORD 'strong-password-here' NOSUPERUSER NOCREATEDB;
CREATE ROLE openspp_admin LOGIN PASSWORD 'admin-password-here' SUPERUSER;
CREATE DATABASE openspp OWNER openspp_admin;
GRANT ALL PRIVILEGES ON DATABASE openspp TO odoo;

-- Option B (flexible): Odoo can create databases (still not superuser)
CREATE ROLE odoo LOGIN PASSWORD 'strong-password-here' NOSUPERUSER CREATEDB;
CREATE DATABASE openspp OWNER odoo;

-- Verify the user is NOT a superuser
SELECT usename, usesuper, usecreatedb FROM pg_user WHERE usename = 'odoo';
-- Expected: usesuper = false
```

### Master Password

The `ODOO_ADMIN_PASSWD` (master password) protects database management operations. Generate a strong random password:

```bash
python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)).decode())'
```

Store this password securely (e.g., in a password manager or secrets vault). It is required for database backup/restore operations via the Odoo interface if you use **Option B** above. In **Option A**, database operations should be done via admin tooling outside Odoo.

### Connection Encryption

Set `DB_SSLMODE` in `.env.production` to encrypt database connections:

| Value | Use When |
|-------|----------|
| `prefer` | Default. Uses SSL if available, falls back to unencrypted |
| `require` | External database (RDS, Cloud SQL). Enforces SSL |
| `verify-ca` | Strict mode. Verifies server certificate against CA |
| `verify-full` | Strictest. Verifies certificate and hostname match |

For local PostgreSQL (same Docker network), `prefer` is acceptable. For external databases, use `require` or stricter.

### Network Restrictions

The PostgreSQL service is only accessible within the `openspp-prod` Docker network. It does not bind to any host port, so it cannot be reached from outside the Docker network.

If you need external database access (e.g., for backups from another host), use an SSH tunnel rather than exposing the port.

## Proxy Mode

`PROXY_MODE=True` is required when running behind a reverse proxy. It tells Odoo to:

- Trust `X-Forwarded-For` headers for client IP detection
- Trust `X-Forwarded-Proto` headers for HTTPS detection
- Generate correct URLs in emails and redirects

Without proxy mode, Odoo sees all requests as coming from Traefik's internal IP on HTTP, which breaks:
- IP-based rate limiting
- Audit logs (all requests logged as proxy IP)
- HTTPS redirect loops
- Session cookie security (cookies not marked `Secure`)

## Worker Sizing

Odoo recommends the formula: **(CPU cores × 2) + 1** workers, with approximately **1 worker serving 6 concurrent users**.

| Beneficiaries | Concurrent Users | Workers | RAM (Total) |
|---------------|------------------|---------|-------------|
| 10,000 | ~12 | 2 | 4 GB |
| 50,000 | ~24 | 4 | 8 GB |
| 100,000 | ~36 | 6 | 16 GB |

### Memory Limits

Each worker has soft and hard memory limits:
- **Soft limit** (`ODOO_MEMORY_SOFT`): Worker is recycled after exceeding this (default: 2 GB)
- **Hard limit** (`ODOO_MEMORY_HARD`): Worker is killed immediately (default: 2.5 GB)

### Request Limits

Additional limits protect against runaway requests:

| Setting | Default | Purpose |
|---------|---------|---------|
| `ODOO_LIMIT_REQUEST` | 8192 | Max requests per worker before recycling |
| `ODOO_TIME_CPU` | 600 | Max CPU seconds per request |
| `ODOO_TIME_REAL` | 1200 | Max wall-clock seconds per request |

The queue worker runs with `ODOO_WORKERS=0` (single-threaded gevent mode) and `ODOO_CRON_THREADS=0` (cron handled by the main Odoo service).

## Verification Checklist

After deployment, verify the hardening is in place:

```bash
DOMAIN="openspp.example.org"

# Verify HTTPS redirect
curl -sI http://$DOMAIN | grep -i location
# Expected: Location: https://openspp.example.org/

# Verify security headers
curl -sI https://$DOMAIN/web/login | grep -iE "strict-transport|x-content-type|x-frame|content-security|referrer-policy|permissions-policy|x-xss|^server:"

# Verify database manager is blocked
curl -sI https://$DOMAIN/web/database | grep -i location
# Expected: redirect to /web/login

# Verify cookie flags
curl -sI https://$DOMAIN/web/login | grep -i set-cookie
# Expected: SameSite=Lax; Secure

# Verify WebSocket endpoint responds
curl -sI https://$DOMAIN/websocket
# Expected: 200 or 101 (upgrade)

# Verify server header is overridden
curl -sI https://$DOMAIN/web/login | grep -i "^server:"
# Expected: Server: OpenSPP (not Werkzeug or Python)
```

## Troubleshooting

### Certificate Not Issued

**Symptom:** Browser shows "connection not secure" warning.

- Check Traefik logs: `docker compose logs traefik | grep -i acme`
- Verify DNS: `dig $DOMAIN` must resolve to your server's IP
- Verify port 80 is reachable from the internet (required for HTTP-01 challenge)
- Check the ACME email is valid and not rate-limited

### 502 Bad Gateway

**Symptom:** Traefik returns 502 errors.

- Check Odoo is running: `docker compose ps`
- Check Odoo health: `docker compose exec odoo curl -f http://localhost:8069/web/health`
- Check Odoo logs: `docker compose logs odoo`
- Odoo may still be starting (start period is 120s). Wait and retry.

### WebSocket Timeout

**Symptom:** Chat and notifications stop working after a few minutes.

- Verify the WebSocket router is configured: `docker compose exec traefik cat /etc/traefik/traefik.yml`
- Check that port 8072 is accessible within the Docker network
- Check browser console for WebSocket connection errors

### Rate Limit Too Strict

**Symptom:** Users get 429 (Too Many Requests) during normal usage.

- Increase `average` and `burst` values in the Traefik labels
- Check if users are behind a shared NAT or corporate proxy (many users sharing one IP)
- Consider using Traefik's `ipWhitelist` middleware to exempt trusted internal IPs

## Related Documentation

- Security overview: {doc}`../security/index`
- Security scanning: {doc}`../security/scanning`
- Backup configuration: {doc}`../backup/index`
