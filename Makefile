# kritva-connect Makefile. Run `make` or `make help` for the command list.
#
# "## name: text" documents a target, "##@ Name" starts a group.
# Only targets that really run something are implemented. A target whose code does not exist
# yet exits 3 (NOT_IMPLEMENTED), never 0 (AGENTS.md section 5). Do not claim a check passed
# unless you ran it.

SHELL := /bin/bash
PYTHON ?= python3
NOT_IMPLEMENTED = 3

.DEFAULT_GOAL := help
.PHONY: help test contract-test check build lint conformance integration status readme_check sync git_sync

##@ Help
help: ## Show this list
	@awk 'BEGIN{FS=":.*## "} /^##@/{printf "\n%s\n", substr($$0,5)} /^[a-zA-Z_-]+:.*## /{printf "  %-16s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

##@ Checks
test: contract-test ## Run all implemented tests (today: the contract schema tests)

contract-test: ## Validate the draft contract schemas (needs: pip install jsonschema referencing)
	@$(PYTHON) -c "import jsonschema, referencing" 2>/dev/null || { echo "missing Python packages: pip install jsonschema referencing" >&2; exit 2; }
	@$(PYTHON) -m unittest discover -s contract/tests -v

check: test ## Run every implemented check (same as test for now; CI workflows are not set up here yet)

##@ Not implemented yet (exit 3)
build: ## Build the package (no code exists yet)
	@echo "NOT_IMPLEMENTED: build (no src/ yet; arrives with the first code task)" >&2; exit $(NOT_IMPLEMENTED)

lint: ## Lint the code (no code exists yet)
	@echo "NOT_IMPLEMENTED: lint (no src/ yet)" >&2; exit $(NOT_IMPLEMENTED)

conformance: ## Provider conformance tests (needs the provider interface and mock)
	@echo "NOT_IMPLEMENTED: conformance (needs KOS-CONNECT-002 code)" >&2; exit $(NOT_IMPLEMENTED)

integration: ## Integration tests against a RaaS mock (KOS-CONNECT-009)
	@echo "NOT_IMPLEMENTED: integration (needs an approved task and a RaaS mock)" >&2; exit $(NOT_IMPLEMENTED)

status: ## Generate status/status.json (generator not written; tasks are PLANNING_ONLY)
	@echo "NOT_IMPLEMENTED: status (generator waits for approved task definitions)" >&2; exit $(NOT_IMPLEMENTED)

readme_check: ## Check README.md against the README standard (the checker is not vendored here yet)
	@echo "NOT_IMPLEMENTED: readme_check (run the kritva-program check: make -C ../kritva-program readme_check README=../kritva-connect/README.md)" >&2; exit $(NOT_IMPLEMENTED)

##@ Git
sync: git_sync ## Alias of git_sync

git_sync: ## Switch to main, fast-forward from origin, prune, delete merged local branches
	@git switch main
	@git pull --ff-only --prune
	@git branch --format='%(refname:short)' | grep -vx main | xargs -r git branch -d
	@git log --oneline -3
