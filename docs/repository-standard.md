# Repository Standard

## Creation gate

Create a repository only when it has one durable responsibility, an accountable company role, a concrete user or consumer, and an independent lifecycle. Do not create repositories for speculative product names or because a technology is fashionable.

## Required declaration

Every active repository README must state:

- purpose and primary users;
- lifecycle status;
- product and technical ownership by role or organisation team;
- included and excluded scope;
- architecture or handbook relationship;
- development and validation commands where implementation exists;
- security and data boundaries;
- release, compatibility, and support model;
- deprecation and archival expectations.

Public Ritru repositories must follow the [public identity standard](public-identity-standard.md). Do not use personal names or individual account handles as the public ownership model.

## Required files

Every active repository requires:

- `README.md`;
- `CONTRIBUTING.md`;
- `SECURITY.md`;
- an explicit licence or private-use notice;
- pull-request controls, inherited or repository-specific.

Add `CODEOWNERS` when stable organisation teams exist and review routing provides real enforcement. Public `CODEOWNERS` must reference organisation teams rather than individual accounts.

Add automated validation only when it checks executable behaviour, generated artefacts, schemas, security policy, compatibility, or another material failure mode. Do not create custom code merely to confirm that static documentation files exist.

Executable repositories additionally require tests, dependency management, release and versioning rules, operational documentation, and rollback or recovery guidance.

## AI-enabled repositories

Repositories using AI agents must define agent responsibilities, context sources, data classification, tool allow-lists, authority boundaries, approval gates, credential handling, deterministic validation, evidence, evaluation, and non-AI recovery.

AI-generated implementation without accountable ownership and deterministic validation is prohibited.

## Customer separation

Generic Ritru assets must not contain customer names, repositories, endpoints, credentials, topology, source code, data, or infrastructure state. Customer-specific composition remains in isolated customer repositories and systems.

## Lifecycle

Active repositories must use an explicit status such as `experimental`, `supported`, `limited`, `deprecated`, `retired`, or `archived`. Ownership, support, compatibility, and security obligations must match the declared status.
