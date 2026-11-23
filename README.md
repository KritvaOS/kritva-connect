# kritva-connect

> Planning and governance repository for Kritva Connect, the connectivity and real-time communication layer of the Kritva OS V2 plan, built to work with LiveKit. The repository holds the accepted architecture decision records, provisional architecture, ownership and security-model documents, and the proposed task list. There is no connectivity code yet. Draft contract schemas (not accepted), their tests and three CI workflows exist, and nothing here is registered in kritva-program.

| Property | Value |
|---|---|
| Project | KritvaOS (Kritva OS V2) |
| Repository | `KritvaOS/kritva-connect` |
| Repository Type | Capability (connectivity layer; planned, no code yet) |
| Visibility Class | PUBLIC (CONNECT-ADR-01, accepted by the owner in chat on 2026-11-22; not yet recorded in kritva-program) |
| GitHub Setting | Not verified from this repository |
| Lifecycle Status | PLANNING (scaffold; no workstream or task is registered in kritva-program) |
| Repository Owner | Project owner (role; see section 15) |
| Security Owner | Security Owner role ([SECURITY.md](SECURITY.md)) |
| Architecture | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) (PROVISIONAL) and [docs/adr/](docs/adr/README.md) |
| Milestones | [planning/MILESTONE.md](planning/MILESTONE.md) (proposed, not in kritva-program) |
| Tasks | [planning/TASKS.md](planning/TASKS.md) (proposed, not in kritva-program) |
| Review Register | [planning/REVIEW_REGISTER.md](planning/REVIEW_REGISTER.md) (provisional owner approvals awaiting re-review) |
| Acceptance Criteria | [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) |
| Status Reporting | None yet (see section 10) |
| License | [LICENSE](LICENSE) (Apache License 2.0) |

This README is a navigation map; the documents it links own the detail. It was written following the section layout of the sibling repositories' READMEs, and the README standard check is not run by this repository's CI (`make readme_check` points to the kritva-program checker).

## 1. Purpose and Scope

Kritva Connect is planned to carry audio, video, telemetry and operator interaction between robots, simulators, lab agents and the Kritva platform through a provider-neutral API, with LiveKit as the first provider.

**This repository owns** (as planned): the provider abstraction, the LiveKit adapter, a mock provider, session, media and data-channel contracts, robot-side connectivity interfaces, a thin gateway process, and conformance tests.

**This repository does not own**: identity, authorization, device enrollment, token and lease issuance and durable telemetry (kritva-raas); sensor data semantics (kritva-sense); motion command lifecycle and fault semantics (kritva-motion); LiveKit project configuration and secrets (private `kritva-connect-deployment`). Connect is not a safety controller.

**Implementation state.** Documents, draft contract schemas with schema tests, and CI scripts. No connectivity code, provider adapter or gateway is implemented.

## 2. Position in the KritvaOS Ecosystem

Connect sits between the platform (kritva-raas) and robots or simulators, and carries the data defined by kritva-sense. It is planned and tracked from [kritva-program](https://github.com/KritvaOS/kritva-program), which owns the repository roster, order and dependencies; Connect is not in that roster yet.

## 3. Architecture

Provisional. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), the decisions in [docs/adr/README.md](docs/adr/README.md), ownership in [docs/OWNERSHIP.md](docs/OWNERSHIP.md) and the security model in [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md).

## 4. Documents to Read First

| # | Document | Label, status | What it answers |
|---|---|---|---|
| 1 | [AGENTS.md](AGENTS.md) | AUTHORITATIVE for the rules for agents and contributors; in force | Scope, boundaries, commits, security rules |
| 2 | [docs/adr/README.md](docs/adr/README.md) | AUTHORITATIVE for architecture decisions; accepted by the owner in chat, not yet in kritva-program | Why Connect is built this way |
| 3 | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | PROVISIONAL; unreviewed | Components and flow |
| 4 | [docs/OWNERSHIP.md](docs/OWNERSHIP.md) | PROVISIONAL; unreviewed | Who owns what, and open points |
| 5 | [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | PROVISIONAL; no Security Owner review yet | Credentials, lifetimes, gateway rules |
| 6 | [planning/TASKS.md](planning/TASKS.md) | PROPOSED; not in the program registry | Which tasks exist and their status |
| 7 | [planning/MILESTONE.md](planning/MILESTONE.md) | PROPOSED | Proposed milestones |
| 8 | [planning/DEPENDENCY_MAP.md](planning/DEPENDENCY_MAP.md) | PROPOSED | Provisional and hard dependencies |
| 9 | [CONTRIBUTING.md](CONTRIBUTING.md) | AUTHORITATIVE for contribution steps | How to contribute |
| 10 | [SECURITY.md](SECURITY.md) | AUTHORITATIVE for vulnerability reporting | How to report a vulnerability |
| 11 | [planning/REVIEW_REGISTER.md](planning/REVIEW_REGISTER.md) | REFERENCE (index only, governs nothing); PROPOSED | Which provisional owner approvals await re-review, and where each one is recorded |

## 5. Repository Structure and File Responsibilities

| Path | Responsibility |
|---|---|
| `docs/` | Architecture, ownership, security model, and `adr/` decision records |
| `planning/` | Proposed tasks, milestones and dependencies, and the review register |
| `tasks/` | One folder per defined task (task file and acceptance criteria) |
| `contract/` | Draft contract schemas (v0.1.0, not accepted) and their schema tests; see [contract/README.md](contract/README.md) |
| `scripts/security/` | Commit message and commit format checkers used by `make commit-check` and CI |
| `tests/` | Tests for the commit checkers |
| `.github/` | Code owners, the pull request template and the `secret-scan`, `commit-message-check` and `tests` workflows |
| `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `AGENTS.md`, `ACCEPTANCE_CRITERIA.md` | Governance |

`src/` and further `tests/` are added by the tasks that need them.

## 6. Toolchain and Development Workflow

Python is the planned default language (CONNECT-ADR-02). `make test` runs the contract schema tests and the commit checker tests, and `make check` also runs the commit check. No build, lint, conformance or integration target is implemented yet; each exits 3 (NOT_IMPLEMENTED). Workflow: branch, pull request, merge commit; see [CONTRIBUTING.md](CONTRIBUTING.md).

## 7. Dependencies and Interfaces

Depends on LiveKit (first provider), on RaaS for identity, tokens and leases, and on the Sense stream contract. No contract is accepted yet; draft v0.1.0 JSON Schemas are in [contract/](contract/README.md) and contracts stay versioned JSON Schema (CONNECT-ADR-05). See [planning/DEPENDENCY_MAP.md](planning/DEPENDENCY_MAP.md).

## 8. Milestones and Implementation Plan

See [planning/MILESTONE.md](planning/MILESTONE.md). The rows are proposals aligned with the V2 phase dates in kritva-program; none is registered or approved.

## 9. Tasks and Acceptance Criteria

See [planning/TASKS.md](planning/TASKS.md) and [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md). The tasks are not in the program planning inventory or baseline and carry no weight or credit.

## 10. Status Reporting and Program Integration

No status report exists, and no generator has been added. Registration with kritva-program is a separate, owner-approved step.

## 11. Build, Test, Regression and Validation

Nothing to build or test yet.

## 12. Git Workflow and Review

Branch from `main`, open a pull request, merge commit. Commit format and footer rules are in [AGENTS.md](AGENTS.md). Code owners are in `.github/CODEOWNERS`. A provisional owner approval is indexed in [planning/REVIEW_REGISTER.md](planning/REVIEW_REGISTER.md) in the same pull request that records it. The `secret-scan`, `commit-message-check` and `tests` workflows run on every pull request; `pr-acceptance-gate` is not set up here yet.

## 13. Safety and Security

Connect is not a safety controller; local safety stays with Motion and the robot. See [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) and [SECURITY.md](SECURITY.md). No physical or safety validation is claimed anywhere in this repository.

## 14. Release and Versioning

No release. Future releases use annotated SemVer tags created only after the approved merge.

## 15. Ownership and Escalation

Project owner and Security Owner: Dinesh (program decisions D-040 and D-032). Escalate unresolved boundary questions to the owner; see the open points in [docs/OWNERSHIP.md](docs/OWNERSHIP.md).

## 16. Related Repositories and References

[kritva-program](https://github.com/KritvaOS/kritva-program), [kritva-sense](https://github.com/KritvaOS/kritva-sense), [kritva-raas](https://github.com/KritvaOS/kritva-raas), [kritva-motion](https://github.com/KritvaOS/kritva-motion), [LiveKit documentation](https://docs.livekit.io). The private `kritva-connect-deployment` repository is intentionally not linked.

## 17. License

Apache License 2.0; see [LICENSE](LICENSE).
