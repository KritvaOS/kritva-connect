# Security model: kritva-connect

Status: PROVISIONAL, part of KOS-CONNECT-001. It has not had the Security Owner review that KOS-CONNECT-003 requires. It follows CONNECT-ADR-06, CONNECT-ADR-07 and CONNECT-ADR-10.

## Credentials and lifetimes

| Credential | Issuer | Lifetime | Purpose |
|---|---|---|---|
| Device credential (mTLS certificate or protected device key) | RaaS enrollment | Long, rotated | Authenticates a gateway to RaaS |
| Kritva session grant | RaaS | Per session | What the session may do |
| LiveKit participant token | RaaS | Short; 10 minutes is the starting candidate | Transport access to one room |
| Control lease | RaaS, verified by the robot | Short, renewable | Authority to send operator commands |
| LiveKit room-admin token | RaaS | Very short, room-scoped | One server-side room operation |

No long-lived LiveKit API key or secret is held by Connect or committed here.

## Rules for the gateway

- Identity is `robot:<device-id>:<session-id>` (encoding fixed in the contract). A participant identity is never proof of device identity.
- Every command is untrusted: check lease, expiry, monotonically increasing sequence number and local limits. Keep a receive buffer of one and use the latest valid command.
- Run a local watchdog and a RaaS-freshness timer. When either lapses, restrict or disconnect without waiting for LiveKit or RaaS.
- Joining a room never inherits a control lease. Reconnecting never restores control without a valid session and lease.
- An RPC acknowledgement is not proof an actuator executed. A LiveKit reconnect is not evidence of robot health.

## LiveKit behaviour this model depends on

Checked against LiveKit's documentation on 2026-11-22 through search results and page summaries, not a hands-on test. Documentation changes, so re-check against the pinned version when the contract is written.

- Token expiry is checked only when connecting; a connected participant is not dropped when its token expires, and the SDK refreshes the reconnect token (the longer of 10 minutes or the original's remaining life).
- Revocation exists on LiveKit Cloud only and lasts 10 minutes; self-hosted LiveKit has none. This is a provider limitation, not a Kritva guarantee.
- Two participants with the same identity: the newer stays, the older is disconnected.
- Rooms are created when the first participant joins. Room administration takes a signed token with grants such as `roomAdmin` or `roomCreate`.
- India region pinning needs the Scale plan or higher, must be enabled by LiveKit for the project, and has no automatic failover. The project data region is US or EU only and fixed at creation; observability data is stored there. Confirm residency with LiveKit before any customer data flows.

## Defaults

Recording is off in V2 until consent, retention and storage policies exist. Hardware interlocks are not replaced by anything here.

## Owner policy questions (open)

TPM or secure element on the target board versus protected file storage for the first device key; who performs enrollment; whether a robot stays connected read-only when RaaS is down (only if it can enforce read-only locally, otherwise disconnect); maximum lease duration and renewal interval; participant-token TTL 10 versus 30 minutes; India region versus default routing; whether some networks need a gateway or relay.
