# Tasks: kritva-connect

Task IDs use the prefix `KOS-CONNECT`. **The workstream `CONNECT` is registered and these tasks are recorded as PLANNING_ONLY in the planning inventory (kritva-program D-145; enterprise program ED-080). The prefix is not in `repo-pipeline.json` (approved registry, D-080) and the tasks are not in the baseline.** They carry no weight and cannot earn credit. A task earns credit only by entering an approved baseline version and then a central approval bound to immutable evidence, never from this file. Status vocabulary: NOT_STARTED, READY, IN_PROGRESS, BLOCKED, IN_REVIEW, CHANGES_REQUESTED, ACCEPTED, DEFERRED, CANCELLED.

| Task | Title | Status | Milestone | Acceptance |
|---|---|---|---|---|
| KOS-CONNECT-001 | Architecture, ownership and interface contracts | IN_PROGRESS (documents drafted 2026-11-22; contracts not written; not submitted for review) | V2-M1-CONNECT-001 (proposed) | [criteria](../tasks/KOS-CONNECT-001/ACCEPTANCE_CRITERIA.md); [task](../tasks/KOS-CONNECT-001/TASK.md) |
| KOS-CONNECT-002 | Provider abstraction, LiveKit adapter, mock provider, session lifecycle, and the CONNECT-ADR-03 benchmark | NOT_STARTED (benchmark needs owner hardware inputs) | V2-M2-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-003 | Session grant and authorization integration, staged: P3 enrollment contract, identity integration and a mocked participant-token exchange; P7 integration with the real RaaS device-authenticated participant-token endpoint | NOT_STARTED (the RaaS enrollment and token tasks are proposals, not registered) | V2-M3-CONNECT-001 (stage 1, proposed); V2-M7-CONNECT-001 (stage 2, proposed) | not yet written |
| KOS-CONNECT-004 | Voice and audio (Connect-side capture, playback and transport capability) | DEFERRED: optional capability, outside V2 acceptance until the owner names a use case | none assigned | not yet written |
| KOS-CONNECT-005 | Video and media: robot and lab-side camera media publication and the provider adapter. Excludes the RaaS browser video player | NOT_STARTED (boundary agreed with the owner 2026-11-22; RaaS-side reconciliation pending) | V2-M7-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-006 | Telemetry transport: delivery, buffering and recovery only. Excludes Sense semantics, RaaS ingestion and validation, durable storage and UI panels. Does not cover logs or result upload | NOT_STARTED | V2-M5-CONNECT-001 prototype, V2-M7-CONNECT-001 end to end (proposed) | not yet written |
| KOS-CONNECT-007 | Robot and simulator gateway (simulation first) | NOT_STARTED (provisional: Sim has no verified interface) | V2-M5-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-008 | Mind, Skill and Motion integration | NOT_STARTED (provisional) | V2-M5-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-009 | RaaS live-session integration: Connect-side interoperability fixtures, contract conformance and end-to-end tests. Excludes RaaS session APIs, authorization and frontend work | NOT_STARTED (may be merged or dropped after its real task body is reviewed; not on title alone) | V2-M7-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-010 | Security and production qualification | NOT_STARTED | V2-M8-CONNECT-001 (proposed) | not yet written |

Only KOS-CONNECT-001 has a task file and criteria. The others get theirs when they are defined and approved. Dependencies are recorded here and in [DEPENDENCY_MAP.md](DEPENDENCY_MAP.md), because the central baseline has no dependency field.

## Boundary with RaaS (owner-approved in chat, 2026-11-22)

Connect owns the robot and lab-side provider client and transport. RaaS owns business sessions, room administration, token issuance, the browser media client and player, telemetry ingestion and validation, durable storage and the UI. See [OWNERSHIP.md](../docs/OWNERSHIP.md). The five RaaS tasks that sit beside Connect (KR-BE-P7-044, KR-BE-P7-045, KR-FE-P7-049, KR-FE-P7-050, KR-FE-P7-051) are kept; the relationships are contract dependencies in [DEPENDENCY_MAP.md](DEPENDENCY_MAP.md), not shared implementation. Nothing here changes a RaaS task or the baseline.
