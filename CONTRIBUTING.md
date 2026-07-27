# Contributing to Ritru Repositories

Ritru treats code, automation, architecture, and documentation as production assets.

## Workflow

1. Confirm the problem, intended outcome, owner, and repository boundary.
2. Create a focused, short-lived branch.
3. Make the smallest coherent change.
4. Add or update tests, validation, security controls, documentation, and recovery guidance.
5. Open a pull request using the shared template.
6. Resolve review feedback and required checks before merge.

## Quality standard

Changes must be specific, maintainable, secure by default, observable where operational, and appropriate to the repository's responsibility. Avoid speculative abstractions, copied customer code, undocumented manual steps, and technology choices without a clear requirement.

## AI-assisted contributions

Disclose material AI assistance in the pull request. Generated content is untrusted until reviewed and validated. AI output must not determine authorisation, approve its own execution, introduce secrets, or bypass deterministic controls.

The accountable contributor remains responsible for correctness, licensing, security, tests, customer-data boundaries, and operational impact.

## Security

Never commit credentials, customer-confidential information, private topology, infrastructure state, personal data, or production identifiers. Report suspected vulnerabilities privately according to `SECURITY.md`.
