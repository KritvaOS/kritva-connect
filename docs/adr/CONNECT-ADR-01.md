# CONNECT-ADR-01: Repository and deployment boundaries

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D1, D12 |

## Context

Connect needs public, reusable code and contracts, and also holds LiveKit project settings and secrets that must stay private. A standalone always-on Connect service would add an internet-facing component, an owner and an on-call burden.

## Decision

- Public `KritvaOS/kritva-connect` holds the provider-neutral core, interfaces, contracts, provider adapters, mock provider, conformance tests, and a thin robot/lab/simulator gateway process built from the same package (option B3).
- Private `kritva-connect-deployment` holds LiveKit Cloud project configuration, secrets, gateway deployment policy, monitoring, usage and credit tracking, and recovery notes. It is not named in the public program registry (owner decision, 2026-11-22).
- RaaS uses its own LiveKit server SDK for tokens and room administration (see CONNECT-ADR-06).
- No always-on Connect cloud service and no public Connect endpoint in V2 without an approved decision backed by a concrete need. The main expected trigger is a customer network that cannot reach LiveKit Cloud directly and needs a lab gateway or relay.

## Consequences

- Public code never contains credentials, project identifiers or deployment secrets.
- Connect is a library plus a gateway process, so there is no Connect service to operate in V2.
- The deployment repo is private; its tasks (DEPLOY-001..009) live in the Enterprise Program namespace, outside the V2 baseline.

## Open items

Whether robots always connect directly to LiveKit Cloud or some networks need a relay (owner policy question, `docs/SECURITY_MODEL.md`).
