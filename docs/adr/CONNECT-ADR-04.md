# CONNECT-ADR-04: Native SDK lifecycle and maintenance

| Property | Value |
|---|---|
| Status | ACCEPTED by the owner (Dinesh) in chat on 2026-11-22. Not yet recorded in kritva-program `v2/DECISIONS.md`; until it is, this ADR is an owner chat approval and no program decision ID exists for it. |
| Date | 2026-11-22 |
| Covers | D4 |

## Context

LiveKit's C++ SDK wraps the Rust `livekit_ffi` library and is moving quickly; documentation pages disagree on version numbers and on the minimum CMake and Clang versions.

## Decision

If a C++ adapter is adopted: pin SDK and FFI versions; record the toolchain (CMake, Rust, Clang), ARM64 support, build, deployment and upgrade costs; name an owner for upgrades and security patches. No unpinned "latest" in production builds. Use the toolchain versions stated on the pinned release's own documentation.

## Consequences

- Native code carries a recurring maintenance cost that must have a named owner before adoption.

## Open items

Owner for upgrades and patches is not named (only needed if C++ is adopted).
