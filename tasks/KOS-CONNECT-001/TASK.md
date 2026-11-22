# KOS-CONNECT-001: Architecture, ownership and interface contracts

| Property | Value |
|---|---|
| Milestone | V2-M1-CONNECT-001 (proposed; not in kritva-program) |
| Status | IN_PROGRESS (documents drafted 2026-11-22; contracts not written; not submitted for review) |
| Weight | None. Not in the baseline (see [planning/TASKS.md](../../planning/TASKS.md)) |
| Depends on | CONNECT-ADR-01 to CONNECT-ADR-10 (accepted by the owner in chat, 2026-11-22) |
| Requires physical | No (documents and schemas only) |
| Acceptance | [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) (AC-101 to AC-105) |
| Deliverables | `docs/ARCHITECTURE.md`, `docs/OWNERSHIP.md`, `docs/SECURITY_MODEL.md`, `docs/adr/`, provisional JSON Schemas in `contract/` |

## Purpose

Fix what Connect owns, what it does not, the decisions it rests on, and the first versioned message contracts, so later tasks build against written boundaries.

## Scope

- Architecture, ownership and security-model documents and the ten ADRs.
- Provisional JSON Schemas for the session, identity and lease messages and the data-channel envelope, with a compatibility policy and version number (0.x). Provisional wherever upstream contracts or repositories are unfinished.

## Non-goals

No code, no LiveKit connection, no benchmark, no change to the Sense contract or the RaaS telemetry envelope, no RaaS implementation, no physical-robot dependency.

## Completion boundary

Acceptance shows the documents and schemas exist and agree with the ADRs. It does not show any behaviour of a real transport, robot or LiveKit project, and it is not safety validation.
