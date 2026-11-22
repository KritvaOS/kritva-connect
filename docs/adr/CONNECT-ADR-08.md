# CONNECT-ADR-08: Cross-repository ownership

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D8 |

## Context

Connect sits between Sense, Mind, Motion, Skill and RaaS. Without boundaries it could redefine their contracts or be mistaken for a safety controller.

## Decision

Sense: data semantics. Connect: transport and delivery. RaaS: durable telemetry and results, identity, authorization. Motion: command lifecycle and fault semantics. Core and local components: real-time execution. Connect is not a safety controller. Software or simulation acceptance is never labelled physical or safety validation, and no physical-robot dependency is taken while V2-M6 is on HOLD.

## Consequences

- `docs/OWNERSHIP.md` records the table and must be kept in line with program records.

## Open items

None.
