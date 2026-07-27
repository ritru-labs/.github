# Repository Bootstrap Checklist

## Before creation

- [ ] One durable responsibility and concrete consumer are defined.
- [ ] Product and technical ownership are defined by company role or organisation team.
- [ ] Repository class and customer-data boundary are clear.
- [ ] Independent lifecycle and maintenance obligations justify a repository.
- [ ] MVP or first concrete use case exists.

## Initial content

- [ ] README declares purpose, users, status, ownership, scope, validation, security, release, and support.
- [ ] CONTRIBUTING, SECURITY, and licence or private-use notice exist.
- [ ] Pull-request and issue defaults are inherited or intentionally overridden.
- [ ] Team-based CODEOWNERS is added only when a stable organisation team exists and review routing is required.
- [ ] Architecture and handbook links are present.
- [ ] Examples contain no customer identifiers, personal employment details, or secrets.

## Engineering controls

- [ ] Validation is proportionate to the repository's actual failure modes.
- [ ] Executable repositories run deterministic tests and security checks on pull requests.
- [ ] `main` protection and merge policy are configured.
- [ ] Secret and dependency scanning are enabled where available.
- [ ] Workflow permissions are minimal.
- [ ] Versioning, compatibility, release, and deprecation are documented where relevant.
- [ ] Rollback, recovery, or archival path is documented.

## AI controls

- [ ] Agent roles and authority boundaries are explicit.
- [ ] Context and data classification are defined.
- [ ] Policy and approval exist outside model reasoning.
- [ ] Credentials are short-lived and excluded from model context.
- [ ] Deterministic validation and evidence are implemented for material actions.
- [ ] Non-AI containment and recovery are possible.
