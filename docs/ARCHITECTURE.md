# Architecture: kritva-connect

Status: PROVISIONAL. The decisions it rests on are CONNECT-ADR-01 to CONNECT-ADR-10 ([adr/](adr/README.md)), accepted by the owner in chat on 2026-11-22. This document is the subject of task KOS-CONNECT-001 and has not been reviewed. No code or contract exists yet; contracts will live in `contract/` when KOS-CONNECT-001 adds them.

## Components

```
Studio / RaaS UI --> RaaS (identity, authorization, jobs, durable store)
                       | issues: Kritva session grant, LiveKit participant token,
                       |         control lease, short-lived room-admin tokens
                       v
   kritva-connect package (provider-neutral API)
   - Session lifecycle   create / join / end, grant validation, recovery policy
   - Media               audio and video tracks
   - Data                telemetry and operator input (lossy), RPC and streams (reliable)
   - Provider adapters   livekit | mock
                       |
              LiveKit Cloud (rooms, SFU, TURN)
                       |
   Robot / lab agent / simulator gateway   (thin process built from the package; outbound connections only)
```

## Flow

1. RaaS authenticates the enrolled device and the operator, and decides what the session may do (CONNECT-ADR-06, CONNECT-ADR-10).
2. RaaS issues a short-lived, room-scoped participant token for identity `robot:<device-id>:<session-id>` and, separately, a control lease.
3. The gateway joins the room using the provider-neutral API. Telemetry flows from the robot; operator input flows to it.
4. The gateway checks every command against the lease (expiry, sequence order, bounds) and runs its own watchdog and RaaS-freshness timer, whatever LiveKit reports (CONNECT-ADR-07, CONNECT-ADR-10).
5. Durable telemetry and results are stored by RaaS, not by the realtime session.

## Boundaries

Connect carries data; it does not define it (Sense), authorize it (RaaS), or make it safe (Motion and local safety design). See [OWNERSHIP.md](OWNERSHIP.md) and [SECURITY_MODEL.md](SECURITY_MODEL.md).

## Not yet decided

The media language outcome (CONNECT-ADR-03 benchmark), the device key storage, enrollment owner, lease durations and token TTL (owner policy questions in [SECURITY_MODEL.md](SECURITY_MODEL.md)).
