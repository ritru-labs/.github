# Repository Bootstrap Checklist

## Before creation

- [ ] One durable responsibility and concrete consumer are defined.
- [ ] Product and technical owners are named.
- [ ] Repository class and customer-data boundary are clear.
- [ ] Independent lifecycle and maintenance obligations justify a repository.
- [ ] MVP or first concrete use case exists.

## Initial content

- [ ] README declares purpose, users, status, ownership, scope, validation, security, release, and support.
- [ ] CONTRIBUTING, SECURITY, licence/private notice, and CODEOWNERS exist.
- [ ] Pull-request and issue defaults are inherited or intentionally overridden.
- [ ] Architecture and handbook links are present.
- [ ] Examples contain no customer identifiers or secrets.

## Engineering controls

- [ ] Automated validation runs on pull requests.
- [ ] `main` protection and merge policy are configured.
- [ ] Secret and dependency scanning are enabled where available.
- [ ] Workflow permissions are minimal.
- [ ] Versioning, compatibility, release, and deprecation are documented.
- [ ] Rollback, recovery, or archival path is documented.

## AI controls

- [ ] Agent roles and authority boundaries are explicit.
- [ ] Context and data classification are defined.
- [ ] Policy and approval exist outside model reasoning.
- [ ] Credentials are short-lived and excluded from model context.
- [ ] Deterministic validation and evidence are implemented.
- [ ] Non-AI containment and recovery are possible.
