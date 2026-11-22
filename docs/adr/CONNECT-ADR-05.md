# CONNECT-ADR-05: Language-neutral contracts

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D5 |

## Context

Python (Connect, Sense, Mind, Motion), TypeScript (RaaS) and possibly C++ must agree on the same messages without sharing source code.

## Decision

Canonical contracts are versioned JSON Schema, placed in `contract/` (the convention used by kritva-sense), each with a compatibility policy and conformance tests. No Python, Node or C++ types appear in a contract. Python, TypeScript and C++ validate against the same schemas. Connect does not import source from other Kritva repositories; it uses released, versioned packages or their published contracts.

## Consequences

- Contracts for KOS-CONNECT-001 are marked provisional wherever upstream contracts or repositories are unfinished.
- Connect never redefines the Sense stream contract or the RaaS telemetry envelope; it carries them.

## Open items

Which upstream packages are actually released and consumable is not verified.
