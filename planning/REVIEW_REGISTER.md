# Kritva Connect: Review Register

| Property | Value |
|---|---|
| Document ID | CONNECT-PLAN-REVIEW-REGISTER |
| Repository | `KritvaOS/kritva-connect` (public) |
| Document Type | Report (index) |
| Status | PROPOSED. Nothing here is a baseline, task, weight, estimate, gate or credit. |
| Owner | Project owner (role) |
| Reviewer/Approver | Not yet assigned; owner approval is provisional |
| Version | 0.1 |
| Last Updated | 2026-11-23 |
| Authority | REFERENCE (index only; the linked records govern) |
| Related Tasks/Milestones | None (record keeping) |
| Related Documents | [README.md](../README.md), [AGENTS.md](../AGENTS.md), [docs/adr/README.md](../docs/adr/README.md), [contract/README.md](../contract/README.md) |

## Format (the same in every Kritva repository register)

This register is an index for later re-review. It does not hold decision text and does not replace the repository's own decision records: the "Authoritative record" column says where the decision lives, and that record wins if the two differ. "Approval basis" states who approved it and in what form; it is evidence, not a status. A decision with no repository record is marked **Not yet recorded** and is only as strong as the cited chat statement. One register per repository, so public and private records stay in the repository that owns them. `kritva-program` (public) and `kritva-enterprise-program` (private) link to the registers of the repositories they cover; they do not copy these rows.

Row fields: ID (`<REPO>-REV-nn`, never reused) | Subject | Authoritative record | Approval basis | Reopen when | Re-review by | Open items.

Public repository: do not add private details (customer data, secrets, credit or contract terms, private repository paths). Link to a private record by repository name and record ID only.

## 1. Provisional owner approvals awaiting re-review

All rows below rest on the same basis unless stated: an owner statement by Dinesh Annayya, overall project owner, in chat on 2026-11-22. It is not an independent review, and it stands in for the accountable roles for now.

| ID | Subject | Authoritative record | Reopen when | Re-review by | Open items |
|---|---|---|---|---|---|
| CONNECT-REV-01 | Provider and boundary: LiveKit supplies signalling, ICE and TURN; RaaS owns business sessions, room administration, tokens and the browser client; Connect owns the robot and lab-side client and telemetry transport | [docs/OWNERSHIP.md](../docs/OWNERSHIP.md), [docs/adr/](../docs/adr/README.md) (CONNECT-ADR-01 to 10); kritva-raas SYS-ADR-009 (private) | A non-LiveKit provider is needed; V2 adds operator control; the Studio web view cannot run the LiveKit client; self-hosted LiveKit is chosen | Independent architecture review | None |
| CONNECT-REV-02 | Draft v0.1.0 contracts under `contract/`: RaaS-issued join grant that Connect only consumes; telemetry envelope that carries an unchanged Sense record with its own delivery sequence and gap notice | [contract/README.md](../contract/README.md); PR #3, merge `f3bc369` | A contract is proposed for acceptance | RaaS, Connect and Sense maintainers | No accepted contract ID. The participant identity pattern is unverified against LiveKit. RaaS has not accepted the join grant |
| CONNECT-REV-03 | `kritva-sdk` and `kritva-sim` stay unregistered until each has an owner and a verified first task (D-017); Connect uses a mock behind a contract | kritva-program D-017, D-144 | V2-M5 planning, or a first task record appears | Programme review at V2-M5 | None |
| CONNECT-REV-04 | Spike in two stages: Stage 0 on a development PC with synthetic or USB video (no target-hardware claim, no credit); Stage 1 a one-week benchmark on target hardware | **Not yet recorded** (chat only; KOS-CONNECT-002 in [planning/TASKS.md](TASKS.md) does not state the stages) | Target hardware inputs arrive | Hardware review of the Stage 1 criteria | Board, OS, cameras, encoder, codec, telemetry rates and network target are not supplied |
| CONNECT-REV-05 | Gateway behaviour when RaaS is unreachable: its own freshness timer; on lapse it stops publishing, disconnects and buffers telemetry locally; local robot execution is unaffected and the timer is never a safety command | [docs/adr/](../docs/adr/README.md) CONNECT-ADR-10 (freshness timer); buffering is **Not yet recorded** | The gateway contract is drafted | Connect owner; Motion and robot review of anything touching execution | Bounded-buffer contract (capacity, overflow, ordering, recovery) |
| CONNECT-REV-06 | Robots connect outbound-only, directly to LiveKit Cloud; no relay or standalone Connect service in V2; universal connectivity is not claimed | **Not yet recorded**: [CONNECT-ADR-01](../docs/adr/CONNECT-ADR-01.md) still lists direct connection versus relay as an open owner question | A customer network blocks outbound-only connections | Firewall and NAT test results | None |
| CONNECT-REV-07 | Connect pull request order: CI and docs hygiene, then draft contracts with validation tests, then the status generator after tasks are approved, then mock-provider code after implementation tasks are approved. KOS-CONNECT-009 narrows to Connect-side integration tests against a RaaS mock | **Not yet recorded** (chat only) | Task definitions are approved | Owner approval before any code PR | CI workflows are proposed separately |

## 2. Reviews still pending

| Review | Covers | Needed before |
|---|---|---|
| Security Owner | Token handoff and device identity as seen from Connect (RaaS owns the decisions) | Any real device authentication or P7 token acceptance |
| Hardware | Target board, encoder and key storage | Stage 1 spike |
| Independent | Everything above rests on the owner's approval and AI-assisted drafting | Any acceptance claim |
| Contract acceptance | RaaS, Connect and Sense on CONNECT-REV-02 | Any contract ID |

## 3. Not approved

Baselining any task; any weight, estimate, credit or task ID; any SEC-GATE ID; a control lease, teleoperation, jog or operator voice in V2; superseding D-144.

## 4. Program links

Not yet recorded. When `kritva-program` points here it will name this path and the commit it reviewed; until then this repository's records stand alone.

## 5. Change log

| Date | Change |
|---|---|
| 2026-11-23 | Created from the cross-repository decision register that was kept as a project document |
