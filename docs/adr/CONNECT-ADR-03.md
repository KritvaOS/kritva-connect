# CONNECT-ADR-03: Media architecture and benchmark

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D3, D10 |

## Context

Whether Python can carry the target video load, or a native (C++) media process is needed, depends on the real board, camera, encoder and network. These are not defined yet, so any threshold set now would be invented.

## Decision

KOS-CONNECT-002 includes a time-boxed (one week) benchmark on the real target hardware comparing two configurations: Python (using `EncodedVideoSource` where the encoder allows) and C++. A Python plus C++ hybrid is built only if Python shows a measurable bottleneck that C++ resolves. The benchmark includes the camera and encoder pipeline so an encoder bottleneck is not blamed on the language.

Metrics: p50/p95/p99 latency, FPS and frame loss, CPU and RSS, telemetry latency under video load, reconnect and republish time, long-run memory, expired-grant rejection.

Decision rule: accept Python; accept Python with a native capture/encode path; choose a C++ media adapter; or defer if the bottleneck is network, encoder, camera or server capacity.

Results are evidence for an ADR and earn no credit by themselves. No production media-language decision beyond the Python-first default until the results are reviewed.

## Consequences

- The benchmark cannot start until the owner supplies: target board and OS; camera model, interface, count, resolution and FPS; encoder, codec and whether hardware encoding is available; telemetry message sizes and rates; expected network conditions and target video latency.
- Thresholds are set after those inputs exist, not before.

## Open items

The five benchmark inputs above are owner inputs and are not yet provided.
