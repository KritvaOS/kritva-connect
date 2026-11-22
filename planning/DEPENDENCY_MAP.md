# Dependency map: kritva-connect

Status: PROPOSED, not in the program dependency map. "Provisional" means the upstream item is unfinished or unregistered, so the dependency cannot be treated as hard.

| Task | Depends on | Kind | Note |
|---|---|---|---|
| KOS-CONNECT-001 | CONNECT-ADR-01 to CONNECT-ADR-10 | Hard | Accepted by the owner in chat; not yet in `DECISIONS.md` |
| KOS-CONNECT-002 | KOS-CONNECT-001; owner benchmark inputs | Hard | Benchmark cannot start without board, camera, encoder, telemetry and network inputs |
| KOS-CONNECT-003 | KOS-CONNECT-001; RaaS device enrollment, device-authenticated token endpoint, control-lease service, revocation (tasks not registered); Security Owner review | Hard, blocked | RaaS-owned work; no Connect credit |
| KOS-CONNECT-005 | RaaS WebRTC and signaling tasks (KR-FE-3, KR-BE-6, not located locally) | Provisional | Overlap with Connect unresolved |
| KOS-CONNECT-006 | Sense stream contract (KOS-SENSE-005, accepted), RaaS telemetry envelope | Provisional | Envelope version not verified |
| KOS-CONNECT-007 | A verified simulator interface and task records | Provisional | `kritva-sim` is empty; program D-144 leaves Sim open |
| KOS-CONNECT-008 | Mind, Skill and Motion released contracts | Provisional | Skill and Motion status not verified |
| KOS-CONNECT-009 | KOS-CONNECT-003, KOS-CONNECT-006; RaaS live-session tasks | Hard | |
| KOS-CONNECT-010 | KOS-CONNECT-001 to KOS-CONNECT-009 | Hard | |

No dependency on physical hardware while V2-M6 is on HOLD.
