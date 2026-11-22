# Dependency map: kritva-connect

Status: PROPOSED, not in the program dependency map. "Provisional" means the upstream item is unfinished or unregistered, so the dependency cannot be treated as hard.

| Task | Depends on | Kind | Note |
|---|---|---|---|
| KOS-CONNECT-001 | CONNECT-ADR-01 to CONNECT-ADR-10 | Hard | Accepted by the owner in chat; not yet in `DECISIONS.md` |
| KOS-CONNECT-002 | KOS-CONNECT-001; owner benchmark inputs | Hard | Benchmark cannot start without board, camera, encoder, telemetry and network inputs |
| KOS-CONNECT-003 stage 1 (V2-M3) | KOS-CONNECT-001; RaaS device enrollment contract (proposed P3 RaaS task, not registered) | Hard, blocked | Contract and mocked participant-token exchange only; no production LiveKit token is issued at this stage |
| KOS-CONNECT-003 stage 2 (V2-M7) | RaaS device-authenticated participant-token endpoint and session revocation (proposed P7 RaaS tasks, not registered); KR-BE-P7-045; Security Owner review | Hard, blocked | RaaS-owned; no Connect credit. The control-lease service is added only if the owner approves operator control in V2 |
| KOS-CONNECT-005 | Connect media/session contract; consumed by KR-FE-P7-050 and KR-BE-P7-045 | Contract | RaaS owns the browser player and LiveKit JS adapter; LiveKit owns signalling and ICE. The older KR-FE-3 and KR-BE-6 task files describe custom signalling and are a separate historical generation, not yet cross-walked |
| KOS-CONNECT-006 | Sense stream contract (KOS-SENSE-005, accepted); RaaS telemetry envelope | Provisional | Envelope version not verified. Consumed by KR-BE-P7-044 and KR-FE-P7-051 |
| KOS-CONNECT-007 | A verified simulator interface and task records | Provisional | `kritva-sim` is empty; program D-144 leaves Sim open |
| KOS-CONNECT-008 | Mind, Skill and Motion released contracts | Provisional | Skill and Motion status not verified |
| KOS-CONNECT-009 | KOS-CONNECT-003 stage 2, KOS-CONNECT-006; RaaS session and token API contracts (KR-BE-P7-045, KR-FE-P7-049) | Hard | Soft contract dependency where an agreed contract and mock allow parallel work |
| KOS-CONNECT-010 | KOS-CONNECT-001 to KOS-CONNECT-009 | Hard | |

No dependency on physical hardware while V2-M6 is on HOLD.

## RaaS consumers of Connect contracts (contract dependencies, not hard blockers)

| RaaS task | Needs from Connect |
|---|---|
| KR-BE-P7-044 Telemetry Ingestion and Validation | KOS-CONNECT-006 transport and delivery contract, plus the Sense stream contract |
| KR-BE-P7-045 Live Session Coordination | Connect session and participant contract |
| KR-FE-P7-050 WebRTC Video View | Connect media/session contract (room, participant, track identity, lifecycle, error categories) |
| KR-FE-P7-051 Telemetry Panels | Connect telemetry delivery contract, plus the Sense telemetry contract |

KR-FE-P7-049 depends only on RaaS session and token APIs. The proposed ADR-10 RaaS tasks are listed in [CONNECT-ADR-10](../docs/adr/CONNECT-ADR-10.md); they are not registered and carry no task ID.
