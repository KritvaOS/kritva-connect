# Tasks: kritva-connect

Task IDs use the prefix `KOS-CONNECT`. **The prefix is not yet in kritva-program `repo-pipeline.json` (approved registry, D-080), the workstream `CONNECT` does not exist, and these tasks are not in the planning inventory or the baseline.** They carry no weight and cannot earn credit. A task earns credit only by entering an approved baseline version and then a central approval bound to immutable evidence, never from this file. Status vocabulary: NOT_STARTED, READY, IN_PROGRESS, BLOCKED, IN_REVIEW, CHANGES_REQUESTED, ACCEPTED, DEFERRED, CANCELLED.

| Task | Title | Status | Milestone | Acceptance |
|---|---|---|---|---|
| KOS-CONNECT-001 | Architecture, ownership and interface contracts | IN_PROGRESS (documents drafted 2026-11-22; contracts not written; not submitted for review) | V2-M1-CONNECT-001 (proposed) | [criteria](../tasks/KOS-CONNECT-001/ACCEPTANCE_CRITERIA.md); [task](../tasks/KOS-CONNECT-001/TASK.md) |
| KOS-CONNECT-002 | Provider abstraction, LiveKit adapter, mock provider, session lifecycle, and the CONNECT-ADR-03 benchmark | NOT_STARTED (benchmark needs owner hardware inputs) | V2-M2-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-003 | Session grant and authorization integration | NOT_STARTED (depends on RaaS device-identity, token and lease tasks that are not registered) | V2-M3-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-004 | Voice and audio | NOT_STARTED | V2-M7-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-005 | Video and media | NOT_STARTED (needs the RaaS WebRTC and signaling overlap resolved) | V2-M7-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-006 | Telemetry transport | NOT_STARTED | V2-M5-CONNECT-001 prototype, V2-M7-CONNECT-001 end to end (proposed) | not yet written |
| KOS-CONNECT-007 | Robot and simulator gateway (simulation first) | NOT_STARTED (provisional: Sim has no verified interface) | V2-M5-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-008 | Mind, Skill and Motion integration | NOT_STARTED (provisional) | V2-M5-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-009 | RaaS live-session integration | NOT_STARTED | V2-M7-CONNECT-001 (proposed) | not yet written |
| KOS-CONNECT-010 | Security and production qualification | NOT_STARTED | V2-M8-CONNECT-001 (proposed) | not yet written |

Only KOS-CONNECT-001 has a task file and criteria. The others get theirs when they are defined and approved. Dependencies are recorded here and in [DEPENDENCY_MAP.md](DEPENDENCY_MAP.md), because the central baseline has no dependency field.
