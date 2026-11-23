# Contributing to kritva-connect

1. Work from a task in [planning/TASKS.md](planning/TASKS.md). If there is none, propose one first.
2. Branch from `main` and open a pull request; do not push to `main`.
3. Commit format: `type(scope): summary` plus one `Task:` or `Tasks:` footer (`Tasks: None (reason)` on a docs or chore commit that implements no task). PRs use `.github/PULL_REQUEST_TEMPLATE.md`; the merge method is a merge commit. See [AGENTS.md](AGENTS.md).
4. A change to an accepted decision needs a new ADR in [docs/adr/](docs/adr/README.md). A provisional owner approval, including one with no ADR yet, is indexed in [planning/REVIEW_REGISTER.md](planning/REVIEW_REGISTER.md).
5. Required checks and review by the Code Owner: see `.github/CODEOWNERS` and [AGENTS.md](AGENTS.md).

Do not commit secrets, LiveKit credentials or project identifiers, generated session metadata or empty placeholder folders.
