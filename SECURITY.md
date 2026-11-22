# Kritva Connect Security Policy

**Repository:** `kritva-connect`
**Security Owner:** Dinesh (program decision D-032)

## 1. Scope

Reproducible security vulnerabilities in this repository's code, contracts, tooling, documentation and CI configuration. Connect carries realtime media, telemetry and operator input and enforces robot-side command checks, so reports about authentication, token or lease handling, replay, identity confusion or unsafe behaviour on disconnect are in scope. The security model is in [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md).

## 2. Do not disclose unfixed vulnerabilities publicly

Please do not put details of an unpatched vulnerability in a public issue, pull request, discussion or post.

## 3. Reporting

Contact the Security Owner (Dinesh, D-032) directly through your existing Kritva channel, say only that you have a security report, and ask for a private place to share the details; do not put details in the first message. GitHub private vulnerability reporting may also be offered under this repository's Security tab; it has not been enabled or tested for this repository, so do not rely on it until the owner records that it has.

Include the affected file or commit, a description, steps to reproduce, observed and expected behaviour, the potential impact and any mitigation you know of. Leave out personal, customer, credential or production data.

## 4. What to expect

The Security Owner will make reasonable efforts to acknowledge a valid report, assess it, coordinate a fix and agree disclosure timing. This policy sets no guaranteed deadlines.

## 5. Secrets

Never commit credentials, tokens, private keys, LiveKit API keys or secrets, or production data. If one is committed by mistake, tell the Security Owner at once so it can be revoked or rotated.
