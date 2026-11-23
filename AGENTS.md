# AGENTS.md: kritva-connect

Guidance for AI coding agents and contributors. The program rules live in kritva-program (`AGENTS.md`, `v2/planning/ACCEPTANCE_STANDARD.md`); this file adds the rules for this repository.

## 1. Scope

Kritva Connect owns: the provider-neutral connectivity API, the LiveKit adapter, the mock provider, session, media and data-channel contracts, robot-side connectivity interfaces, the gateway process and their conformance tests. It does not own: identity, authorization, device enrollment, token and lease issuance, durable telemetry (kritva-raas); sensor data semantics (kritva-sense); motion command lifecycle and fault semantics (kritva-motion); inference (kritva-mind); skill orchestration (kritva-skill); LiveKit project configuration and secrets (private `kritva-connect-deployment`). No import of other Kritva repositories' internals; use released packages or published contracts only. See [docs/OWNERSHIP.md](docs/OWNERSHIP.md).

## 2. Program rules that apply here

1. This repository reports facts; the program repository decides baseline, weights, approvals and gates. A commit here never creates credit.
2. Software acceptance (tests, simulation, mocks, versioned interfaces) is never described as hardware or safety validation.
3. No empty folders, no placeholder tasks, no invented owners or dates. Add `src/`, `contract/` and other folders only when a real task needs them.
4. Interfaces are contract-first and versioned. A breaking change needs a new MAJOR version, a changelog entry and an approved decision.
5. Do not state anything about LiveKit or another repository as fact unless it was checked; mark it unverified with the date.
6. A provisional owner approval that has not had an independent review gets a row, or an update to its row, in [planning/REVIEW_REGISTER.md](planning/REVIEW_REGISTER.md) in the same pull request that records it. The register links to the authoritative record and never copies decision text. A "Not yet recorded" row is not approved architecture.

## 3. Security rules specific to Connect

- Never commit a LiveKit API key or secret, a token, a device key or a project identifier. Connect holds no long-lived LiveKit secret (CONNECT-ADR-06).
- A LiveKit token is never an authorization. Command authority comes only from a RaaS-issued control lease checked on the robot (CONNECT-ADR-10).
- Never treat a LiveKit connection or reconnect as evidence that a session is authorised or a robot is healthy.

## 4. Commits and pull requests

- Commit header: `type(scope): summary` (feat, fix, docs, refactor, test, build, ci, chore, perf, revert, security), at most 90 characters.
- Exactly one footer line, `Task: KOS-CONNECT-NNN` or `Tasks: KOS-CONNECT-NNN, KOS-CONNECT-NNN`; a docs or chore commit that implements no task uses `Tasks: None (reason)`.
- Merge method is a merge commit (kritva-program D-053). PRs use `.github/PULL_REQUEST_TEMPLATE.md`.
- Never add a `Claude-Session:` trailer or a claude.ai session link to a commit or PR description.
- Open a PR; do not push to `main`. The `secret-scan`, `commit-message-check` and `tests` workflows run on every PR. `pr-acceptance-gate` is not set up here yet. Run `make check` before you push; it does not run `secret-scan`.

## 5. Tests

`make test` runs the contract schema tests and the commit checker tests. No build target exists yet; add it with the first code task. An unimplemented target must exit 3 (NOT_IMPLEMENTED), never 0.

## 6. Tags and milestones

Release tags are annotated SemVer, created only after the approved merge. A milestone closes only through an approved `COMPLETION_RECORD.md`; a tag or a merge does not close it.
