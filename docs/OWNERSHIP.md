# Ownership: kritva-connect

Status: PROVISIONAL, part of KOS-CONNECT-001. Must be kept in line with kritva-program records; where this file and a program record disagree, the program record wins.

| Component | Repository | Visibility | Owns |
|---|---|---|---|
| kritva-connect | `KritvaOS/kritva-connect` | Public (Apache-2.0) | Provider abstraction, LiveKit adapter, mock provider, session, media and data-channel contracts, robot-side connectivity interfaces, gateway process, conformance tests |
| kritva-connect-deployment | private | Private (not in the public program registry) | LiveKit project configuration, secrets, gateway deployment policy, monitoring, usage and credit tracking, recovery |
| kritva-raas | `KritvaOS/kritva-raas` | Private | Customer identity, tenancy, session authorization, device enrollment, token and lease issuance, jobs and runs, durable telemetry and results, operator UI |
| kritva-sense, kritva-mind, kritva-motion, kritva-skill | `KritvaOS/...` | Public | Their own contracts and safety semantics. Connect transports; it never redefines them |

## Rules

1. A LiveKit token is transport access only. It is never a business authorization and never authority to issue Motion commands.
2. Realtime transport is for observation and operator interaction. Durable state stays authoritative in RaaS.
3. A cloud or LiveKit disconnect must not change robot-local safety state. Motion owns that.
4. Connect never redefines the Sense stream contract or the RaaS telemetry envelope.
5. Software or simulation acceptance is never labelled physical or safety validation. No physical-robot dependency while V2-M6 is on HOLD.
6. No secrets, keys or LiveKit credentials in this repository.

## RaaS and Connect boundary (owner-approved in chat, 2026-11-22)

| Capability | Owner |
|---|---|
| Business session creation, authorization, expiry and cleanup | RaaS backend |
| LiveKit room administration and participant-token issuance | RaaS backend (CONNECT-ADR-06) |
| WebRTC signalling, ICE and provider media infrastructure | LiveKit; not rebuilt by Kritva |
| Robot and lab-side LiveKit client, track publication, reconnect and transport recovery | Connect gateway |
| Browser-side media client and video player | RaaS frontend, using the LiveKit JS SDK behind a small RaaS-owned media-client interface |
| Telemetry meaning and schema | Sense |
| Telemetry transport | Connect |
| Telemetry ingestion, validation and durable storage | RaaS backend |
| Telemetry panels | RaaS frontend |
| Command lifecycle and local safety | Motion and Core; never delegated to Connect or LiveKit |

Connect publishes a versioned media and session contract (session and room correlation, participant identity and role, track identity and metadata, publication lifecycle, reconnect and disconnect semantics, provider-independent error categories). It does not ship a browser SDK or UI component. V2 live work is observation-only unless the owner approves an operator command path; in that case a control lease and a Studio lease UI become required, as separate tasks.

## Open points

- The Control Plane is a capability whose implementation owner is RaaS (program D-030), while program D-144 records a planned separate `kritva-control-plane` repository (proposed name, not created). Confirm which governs token and lease issuance before RaaS tasks are registered.
- Program D-144 places SDK and Studio in `kritvaos-community` and leaves Sim placement open. The empty `kritva-sdk` and `kritva-sim` repositories are not registered, and registering them would need an owner decision. Connect depends on neither.
