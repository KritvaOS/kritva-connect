# Acceptance Criteria: KOS-CONNECT-001

Standard: kritva-program `v2/planning/ACCEPTANCE_STANDARD.md`. Task: [KOS-CONNECT-001](TASK.md). Status of these criteria: PROPOSED by the author; not reviewed and not baselined. All criteria are documentation and schema checks only.

| ID | Criterion (testable) | Verified by |
|---|---|---|
| AC-101 | `docs/adr/` holds CONNECT-ADR-01 to CONNECT-ADR-10, each with status, context, decision, consequences and open items, and the index maps every earlier D1-D12 label to exactly one ADR. | review |
| AC-102 | `docs/OWNERSHIP.md` agrees with kritva-program records (workstreams, D-030, D-144) and lists every open point; no component is claimed that a program record assigns elsewhere. | review against program records |
| AC-103 | `docs/SECURITY_MODEL.md` states the credential lifetimes, gateway rules, LiveKit provider limitations (with the date and basis of the check) and the open owner policy questions; no secret, key or project identifier appears in the repository. | review, secret scan |
| AC-104 | `contract/` holds provisional JSON Schemas (session, device identity, lease, data-channel envelope) that validate their own examples, carry a version and a compatibility policy, and use no language-specific types. | schema validation test |
| AC-105 | No document claims physical or safety validation, and every statement about another repository or about LiveKit is either verified (with source and date) or marked unverified. | review |

## Definition of done

AC-101 to AC-105 are demonstrated; required PR checks are green; review is recorded against the closing commit; the owner records the ADR approval in kritva-program `v2/DECISIONS.md`; central registration and approval are recorded in kritva-program.
