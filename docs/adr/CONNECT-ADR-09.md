# CONNECT-ADR-09: Provider-neutral robot and simulator interfaces

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D9 |

## Context

LiveKit Portal for ROS exists but is LiveKit-specific. `kritva-sim` is empty, and program decision D-144 leaves Sim placement open until the simulator artifact interface (COMMUNITY-004-01) is defined.

## Decision

Define provider-neutral robot and simulator connectivity contracts first. LiveKit Portal for ROS is an optional, provider-specific adapter; KOS-CONNECT-007 does not depend on it. Do not assume the empty `kritva-sim` provides an interface; the gateway is architecture and prototype work only until Sim has a verified interface and task records. A mock provider is mandatory so CI never needs LiveKit Cloud.

## Consequences

- KOS-CONNECT-007 stays provisional.

## Open items

Sim placement (program D-144).
