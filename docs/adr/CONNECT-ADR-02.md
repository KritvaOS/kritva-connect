# CONNECT-ADR-02: Implementation language and runtime

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D2 |

## Context

Sense, Mind and Motion are Python packages with JSON-schema contracts; Core is C++ (CMake); the RaaS backend is TypeScript on Node; Sim and SDK are empty. LiveKit's Python and C++ SDKs both sit on the same Rust FFI core, so the choice is about glue, build cost, hardware-encoder access and existing code, not two different WebRTC engines.

## Decision

Python is the default implementation language for the provider abstraction, session lifecycle, transport orchestration, recovery policy, telemetry routing and the first LiveKit integration. Native media code stays replaceable behind a stable interface: the robot-side media adapter is a separate interface from the control layer so it can move to a native process later.

## Consequences

- Python-first code can reuse Kritva's Python packages through released, versioned packages or published contracts only.
- A C++ media adapter is an approved option, not part of the initial plan. CONNECT-ADR-03 decides whether it is needed.

## Open items

None beyond CONNECT-ADR-03.
