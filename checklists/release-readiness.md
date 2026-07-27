# Release Readiness Checklist

## Product and contract

- [ ] Release scope, users, outcome, owner, and support status are explicit.
- [ ] Inputs, outputs, APIs, schemas, compatibility, and breaking changes are documented.
- [ ] Migration, upgrade, deprecation, and rollback instructions exist.

## Quality

- [ ] Required tests, policy checks, scans, and representative workflow evaluations pass.
- [ ] Known limitations, accepted risks, and stop conditions are documented.
- [ ] Generated artefacts are reproducible and traceable to reviewed source.

## Security and supply chain

- [ ] Dependencies, containers, infrastructure, and release workflows are scanned.
- [ ] Secrets and privileged credentials are absent from source and artefacts.
- [ ] Artefact checksums, signatures, SBOM, and provenance meet the release risk.
- [ ] Customer and tenant isolation is validated where applicable.

## AI systems

- [ ] Model, prompt policy, tools, context sources, and evaluation versions are recorded.
- [ ] Prompt injection, excessive agency, data leakage, and tool abuse controls are tested.
- [ ] Approval and execution authority are external to model reasoning.
- [ ] Fallback, safe interruption, and non-AI recovery are tested.

## Operations

- [ ] Observability, alerts, SLOs, runbooks, capacity, cost, and on-call ownership are ready.
- [ ] Deployment and rollback have been rehearsed at an appropriate level.
- [ ] Customer or internal acceptance evidence is retained.
