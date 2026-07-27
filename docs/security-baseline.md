# Repository Security Baseline

## Access

- use organisation-managed identities and least privilege;
- minimise administrators and review access regularly;
- use workload identity or short-lived credentials for automation;
- remove inactive collaborators and integrations;
- document emergency administrator access.

## Source protection

- protect `main`;
- require reviewed pull requests and stable checks;
- block force pushes and branch deletion;
- use CODEOWNERS for sensitive code, workflows, policies, and security controls;
- enable secret scanning and push protection where available.

## Dependencies and supply chain

- enable dependency and vulnerability alerts;
- minimise dependencies and remove unused packages;
- review third-party GitHub Actions and privileged integrations;
- pin privileged third-party actions to immutable revisions;
- produce checksums, signatures, SBOMs, and provenance for released artefacts as product maturity requires;
- define supported versions and remediation expectations.

## Secrets

Never store secrets in source, examples, issue forms, prompts, generated plans, logs, workflow artefacts, or evidence. Use approved secret stores, workload identity, environment protection, redaction, rotation, and revocation.

## CI/CD

Use minimal workflow permissions, isolate untrusted pull-request execution, protect release environments, validate generated files, retain useful evidence, and prevent forks or untrusted content from accessing privileged secrets.

## Customer and AI controls

Customer data and configuration remain isolated. AI-enabled workflows must address prompt injection, malicious repository content, excessive agency, cross-customer leakage, model-provider boundaries, tool abuse, audit integrity, and non-AI recovery.

## Exceptions

Security exceptions require owner, business justification, risk, compensating controls, expiry, and remediation plan. Repeated exceptions indicate a design or policy failure.
