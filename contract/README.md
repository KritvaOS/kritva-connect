# Connect Contracts (DRAFT, CROSS-REPOSITORY REVIEW REQUIRED)

Status: **DRAFT v0.1.0. No accepted contract identifier exists. No implementation credit.** These drafts were prepared for task KOS-CONNECT-001 (planning only). They are owner-approved to draft ([review register](../planning/REVIEW_REGISTER.md), CONNECT-REV-02), not accepted. RaaS, Connect and Sense maintainers must agree on content and version before any identifier is assigned.

## Rule to preserve

Sense defines what telemetry means. Connect defines how it is delivered. RaaS defines what is authorized, ingested and retained.

## What is here

| Schema | Owner of the final shape | What it is |
|---|---|---|
| `media-session/join-grant.schema.json` | **RaaS** (issues it); Connect consumes it | What the gateway needs from RaaS to join a room. Connect's stated requirement, for RaaS review |
| `media-session/participant-identity.schema.json` | **RaaS** assigns the value; Connect validates the format | Proposed identity format, pending LiveKit compatibility validation |
| `media-session/track-descriptor.schema.json` | Connect | Transport and media track identity and lifecycle only |
| `media-session/session-event.schema.json` | Connect | Transport connection events and error categories. Never business-session or robot safety state |
| `telemetry-delivery/envelope.schema.json` | Connect | Delivery metadata around an unchanged Sense stream record, and the gap notice |

## Boundaries

- **Join grant.** It is RaaS-issued. Connect is only the consumer. The token is secret material: Connect never logs it, never persists it and never includes it in a diagnostic dump. Expiry is information for connection handling and does not make Connect the authority for token validity. Connect never receives a LiveKit API secret or any authority to create tokens. Device and tenant authorization, session validation, token creation and signing, room administration, renewal and revocation stay with RaaS.
- **Session reference.** An opaque correlation value. Connect does not interpret Job or Run business state from it.
- **Capabilities.** RaaS authorizes the grant. Connect enforces only its own local media behaviour. The schema has no field for room administration or command authority, and `additionalProperties` is false, so such a field is invalid by construction.
- **Events.** Every event carries `state_scope: "transport"`. A `freshness_lapsed` event means platform or transport freshness lapsed. It is never a Motion safety state and never a statement that the robot is safe or unsafe. `token_refresh_failed` reports a failure; RaaS controls renewal and authorization.
- **Tracks and channels.** A media track (video) is distinct from a telemetry delivery channel. If telemetry travels over a LiveKit data track, that is a transport implementation choice. Sense's contract does not depend on LiveKit.

## Telemetry delivery rules (draft)

1. The `sense_record` is carried **unchanged and opaque**. Connect does not copy, redefine or reinterpret Sense records, sample sequence, clocks or diagnostics. Sense stream contract 0.1.0 (`stream.schema.json` and `STREAM_CONTRACT.md` in the `KritvaOS/kritva-sense` repository under `contract/`) stays authoritative for telemetry semantics. The receiver validates the record against the Sense contract version named in `sense_stream_version`.
2. `delivery_sequence` is a transport ordering number. It is monotonic per `(channel_id, channel_epoch)`, starts at 0 for a new epoch and increases by 1 for each envelope the gateway sends on that channel. It is not the Sense sample sequence.
3. A receiver detects a missing range when a received `delivery_sequence` is greater than the previous plus one. A `gap_notice` lets the gateway state the missing range (`missing_from` to `missing_to`, inclusive, `missing_to >= missing_from`) and a reason when it knows it dropped envelopes. A gap notice is a delivery event. It is not a Sense `STREAM_SEQUENCE_GAP`, which stays a Sense diagnostic.
4. Channel recreation (for example after a reconnect that loses state) starts a new `channel_epoch` and resets `delivery_sequence` to 0. A receiver never compares sequence numbers across epochs.
5. `gateway_sent_at` is transport metadata. It does not replace sensor or event time inside the Sense record.
6. Reliable and lossy behaviour, buffer limits, overflow and recovery after reconnect are not defined in v0.1 and need the gateway contract ([review register](../planning/REVIEW_REGISTER.md), CONNECT-REV-05).

## Versioning

SemVer. All v0.x drafts may change without notice. A breaking change after acceptance needs a new MAJOR version, a changelog entry and an approved decision (AGENTS.md rule 4). The exact identity length limits and characters must be checked against LiveKit's rules before acceptance; the value in the draft is unverified (2026-11-22).

## Tests

`python3 -m unittest discover -s contract/tests` needs the `jsonschema` package. The tests check that each schema is valid JSON Schema 2020-12 and that the examples in the test file behave as expected. They are software checks of the draft, not hardware or safety validation. The `tests` workflow runs them on every pull request.
