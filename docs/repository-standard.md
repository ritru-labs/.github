# Repository Standard

## Creation gate

Create a repository only when it has one durable responsibility, an accountable owner, a concrete user or consumer, and an independent lifecycle. Do not create repositories for speculative product names or because a technology is fashionable.

## Required declaration

Every active repository README must state:

- purpose and primary users;
- lifecycle status;
- product and technical ownership;
- included and excluded scope;
- architecture or handbook relationship;
- development and validation commands;
- security and data boundaries;
- release, compatibility, and support model;
- deprecation and archival expectations.

## Required files

- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- explicit licence or private-use notice
- `.github/CODEOWNERS`
- pull-request controls
- automated validation appropriate to the repository

Executable repositories additionally require tests, dependency management, release/versioning rules, operational documentation, and rollback or recovery guidance.

## AI-enabled repositories

Repositories using AI agents must define agent responsibilities, context sources, data classification, tool allow-lists, authority boundaries, approval gates, credential handling, deterministic validation, evidence, evaluation, and non-AI recovery.

AI-generated implementation without accountable ownership and deterministic validation is prohibited.

## Customer separation

Generic Ritru assets must not contain customer names, repositories, endpoints, credentials, topology, source code, data, or infrastructure state. Customer-specific composition remains in isolated customer repositories and systems.

## Lifecycle

Active repositories must use an explicit status such as `experimental`, `supported`, `limited`, `deprecated`, `retired`, or `archived`. Ownership, support, compatibility, and security obligations must match the declared status.
