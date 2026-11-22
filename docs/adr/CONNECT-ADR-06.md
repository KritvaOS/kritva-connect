# CONNECT-ADR-06: Identity, tokens and room administration

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D6 |

## Context

A LiveKit token is a signed JWT for transport access. LiveKit rooms are created automatically when the first participant joins, so joining does not need the API secret. Room administration calls (create, delete, remove participant, mute) need a signed token with grants such as `roomAdmin` or `roomCreate`, which can be issued short-lived and scoped.

## Decision

RaaS (the Control Plane capability) owns identity, business authorization, session grants, LiveKit participant tokens and room administration. Connect never holds a long-lived LiveKit API key or secret, in public code or in its normal runtime. Connect joins with a scoped participant token. If Connect needs a server-side room operation, RaaS issues a short-lived, room-scoped token for that operation. Two credentials stay distinct: the Kritva session grant (what the session may do) and the LiveKit access token (room permissions).

## Consequences

- RaaS needs task records for token issuance and room administration (see CONNECT-ADR-10). Connect cannot claim that work or its credit.
- A LiveKit token is never a business authorization and never authority to issue Motion commands.

## Open items

Which program record governs Control Plane ownership (D-030 vs D-144) needs confirming before RaaS tasks are registered (`docs/OWNERSHIP.md`).
