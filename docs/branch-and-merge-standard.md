# Branch and Merge Standard

## Default branch

Use `main` as the protected default branch.

## Working branches

Branches should be short-lived and focused. Preferred prefixes are:

- `feature/`
- `fix/`
- `docs/`
- `security/`
- `chore/`
- `foundation/`
- `experiment/`

## Pull requests

Material changes require a pull request. The author must describe problem, scope, trade-offs, AI involvement, security, validation, deployment, rollback, and follow-up.

The author must not treat an AI-generated review or test summary as independent approval.

## Required controls

For active repositories, progressively apply:

- pull requests before merge;
- required successful CI and policy checks;
- resolved review conversations;
- CODEOWNERS review for sensitive areas;
- blocked force pushes and branch deletion;
- restricted direct pushes;
- secret scanning and push protection where available;
- dependency and vulnerability alerts;
- signed release artefacts and provenance for distributable software.

Do not require a check until it is stable and maintainable. A permanently failing control trains engineers to bypass governance.

## Merge strategy

Use squash merge by default to preserve a focused main-branch history. Use another strategy only when commit history has deliberate release, audit, or migration value.

## Emergency changes

Emergency administrator changes require an incident or exception record containing reason, approver, affected scope, validation, rollback, and follow-up. Emergency access is not a substitute for fixing the normal delivery path.
