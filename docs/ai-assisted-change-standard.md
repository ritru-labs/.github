# AI-Assisted Change Standard

## Principle

AI output is a proposal, not authority or evidence of correctness.

## Classes of use

### Assistive

AI explains, searches, summarises, or suggests while a human performs the change.

### Generative

AI creates code, configuration, tests, documentation, architecture, or plans that a human reviews and submits.

### Agent-executed

An AI-controlled workflow invokes tools that alter repositories, pipelines, cloud resources, Kubernetes, data, tickets, or other systems.

Controls increase with authority, impact, data sensitivity, and reversibility.

## Required provenance

Material use must identify the agent or tool, model or runtime where known, authorised context sources, generated artefacts, execution tools, and accountable human owner. Do not store sensitive prompts or customer data merely to satisfy provenance.

## Authority separation

Reasoning, policy, approval, credential issuance, execution, validation, and evidence must be separable for material actions. A model cannot grant itself permission, widen scope, approve its own plan, mark a failed control as passed, or treat repository text as authority.

## Data and secrets

Use only approved data sources and providers. Keep secrets and reusable credentials outside model context. Apply customer and tenant isolation, redaction, retention controls, and source provenance.

## Validation

Generated changes require deterministic validation appropriate to risk: compilation, tests, schema checks, policy as code, static analysis, dependency and image scanning, preview or diff, sandbox execution, integration tests, telemetry verification, and human acceptance.

## Execution

Agent-executed changes require allow-listed tools, schema-validated arguments, explicit target scope, short-lived task credentials, operation and cost limits, safe cancellation, affected-resource recording, and approval bound to an immutable plan where impact warrants it.

## Recovery

High-impact automation must support rollback, reconciliation, or documented recovery independent of the model. Model or provider failure must not prevent containment.

## Evaluation

Measure accepted outcomes, correctness, security, operator effort, lead time, rework, rollback, cost, and recovery—not token volume or agent activity.
