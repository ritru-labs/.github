# Security Policy

Ritru repositories may contain privileged automation and must be treated as software supply-chain assets.

## Reporting

Report suspected vulnerabilities, credential exposure, customer-data disclosure, unsafe agent behaviour, or supply-chain compromise privately to Ritru founding leadership. Do not publish exploit details, secrets, or customer information in an issue.

## Immediate response

For suspected exposure:

1. revoke affected credentials and tokens;
2. stop unsafe automation or workflows;
3. preserve logs and evidence;
4. identify affected repositories, artefacts, systems, and customers;
5. remove exposed material from active references and history where practical;
6. document containment, remediation, and preventive action.

## Baseline

Repositories must follow the organisation [security baseline](docs/security-baseline.md). AI-enabled systems must additionally address prompt injection, untrusted context, excessive agency, tool abuse, secret exposure, tenant isolation, auditability, and non-AI recovery.
