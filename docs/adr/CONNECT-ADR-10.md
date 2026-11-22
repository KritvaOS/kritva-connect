# CONNECT-ADR-10: Device identity, leases and revocation

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D11 |

## Context

LiveKit token expiry is checked only at connection time; an already-connected participant stays connected and its reconnect token is refreshed by the SDK. Revocation exists on LiveKit Cloud only and lasts about 10 minutes. If two participants join with the same identity, the older is disconnected. A connected robot can therefore stay in a room through a RaaS outage.

## Decision

- Every robot, lab agent or simulator gateway has a unique enrolled device identity and authenticates to RaaS with mTLS, or an equivalent protected device key where certificates are unavailable. One-time bootstrap credentials are used for enrollment only.
- RaaS owns enrollment, credential status, rotation, revocation and issuance of short-lived, room-scoped LiveKit participant tokens, and only after authenticating the enrolled device.
- Gateway participant identity is unique per device and session, for example `robot:<device-id>:<session-id>` (exact encoding in the contract). A participant identity is never proof of Kritva device identity.
- Three lifetimes stay separate: device credential (long-lived, rotated), LiveKit participant token (short; 10 minutes is the starting candidate), operator-control lease (independently issued, short, checked locally by the robot).
- The gateway enforces lease expiry, command validity, sequence order and the watchdog regardless of LiveKit state, and enforces its own RaaS-authority freshness timer: it restricts or disconnects on its own when that timer lapses. An active LiveKit connection never implies the Kritva session is still authorised.
- Loss of RaaS blocks new grants and renewals. Reconnecting never restores control without a valid session and lease. A participant joining a room never inherits an existing control lease.
- LiveKit Cloud's 10-minute revocation window is a provider limitation, not a Kritva guarantee. Local lease expiry and gateway enforcement are the control-authority revocation boundary, and the lease protocol must not depend on LiveKit.

## Consequences

- RaaS needs new tasks (device enrollment, device-authenticated token endpoint, control-lease service, revocation) that are not in any registry yet; KOS-CONNECT-003 depends on them. They are RaaS-owned and earn no Connect credit.
- Gateway-side lease and freshness enforcement is Connect work; the safe-state transition is defined by Motion.
- A Security Owner review is required before KOS-CONNECT-003 is accepted.

## Open items

TPM or secure element on the target board; who performs enrollment; read-only versus disconnect when RaaS is down; maximum lease duration and renewal interval; token TTL 10 versus 30 minutes. All are owner policy questions.
