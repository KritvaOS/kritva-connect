# CONNECT-ADR-07: Transport and robot safety

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D7 |

## Context

LiveKit data tracks are lossy; reliable delivery needs RPC or streams. LiveKit's own teleoperation guidance says to keep the control buffer at size one, treat every command as untrusted, require a single-controller lease and fail to a safe state when input stops. Application safeguards do not replace hardware interlocks.

## Decision

- Audio and video use media tracks.
- Continuous telemetry and continuous operator input use data tracks, with a one-frame receive buffer and latest-valid-command semantics.
- Control leases and discrete acknowledged operations use RPC. Larger payloads use reliable text or byte streams.
- Robot-side validation (expiry, monotonically increasing sequence numbers, bounds) and a local watchdog are mandatory. Network loss never compromises local safety.
- A reconnect never replays an old motion command. A LiveKit reconnect is never evidence of robot health. An RPC acknowledgement is not proof an actuator executed.
- Reconnect is not recovery: Connect owns session state and recovery policy, marks telemetry gaps instead of treating missing data as valid, and drops stale operator interactions after reconnect.

## Consequences

- The safe state is defined by Motion and the local safety design, not by the transport.
- Recording is off by default in V2 until consent, retention and storage policies exist.

## Open items

Safe behaviour on disconnect is an owner/Motion definition, not yet written.
