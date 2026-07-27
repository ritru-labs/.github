## Problem and outcome

What problem does this change solve, who is affected, and what measurable outcome should result?

## Scope and boundaries

What is included, excluded, and intentionally deferred? Which repositories, systems, environments, customers, or contracts are affected?

## Decision and trade-offs

Why is this the simplest durable approach? What alternatives, costs, limitations, and risks remain?

## AI assistance and provenance

- Was AI used for discovery, analysis, generation, testing, review, documentation, or execution?
- Which tools, agents, models, prompts, or workflows materially influenced the change?
- Which generated artefacts received human review?
- What authority and data boundaries applied to the AI system?

State `No material AI assistance` where applicable.

## Security and privacy

Describe identity, permissions, secrets, data classification, customer isolation, dependency, supply-chain, and prompt-injection considerations.

## Validation and evidence

List deterministic tests, policy checks, previews, scans, manual validation, and evidence produced. Include commands or workflow references.

## Deployment, rollback, and recovery

How is the change introduced safely? What triggers rollback? How is the previous state restored? What non-AI recovery path exists?

## Operational impact

Describe observability, alerts, SLOs, support ownership, compatibility, cost, migration, and deprecation impact.

## Checklist

- [ ] The change has one clear purpose and accountable owner.
- [ ] Repository boundaries and customer-data isolation are preserved.
- [ ] AI-generated output was treated as untrusted and independently validated.
- [ ] No AI system granted itself authority or approved its own execution.
- [ ] Secrets and privileged credentials are absent from code, prompts, logs, and evidence.
- [ ] Tests and required security checks pass.
- [ ] Rollback or documented recovery is practical.
- [ ] Documentation and decision records are updated.
- [ ] Breaking changes, migrations, and follow-up work are explicit.
