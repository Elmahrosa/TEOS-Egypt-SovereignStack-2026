# Conceptual Data Model & Event Taxonomy

TEOS is **event-centric**: identity, governance, finance, asset, and audit actions are represented as structured events.

This document provides a high-level, implementation-agnostic view of core entities and events.

## 1. Core Entities

### Identity Subject

Represents a person, institution, or service.

- Identifier (policy-controlled; may be pseudonymous or derived from existing ID systems)
- Credential set (education, professional, eligibility, KYC status where applicable)
- Roles (e.g., beneficiary, approver, auditor, operator)

### Governance Object

Represents a proposal or decision process.

- Proposal ID
- Proposer (linked to Identity Subject)
- Policy domain (finance, infrastructure, logistics, etc.)
- Status (draft, under review, approved, rejected, executed, closed)
- Linked resources (budget lines, assets, programs)

### Financial Record

Represents a transaction or disbursement log entry.

- Record ID
- Program / project reference
- Amount and currency
- Counterparties (institutional)
- Timestamps (initiated, approved, recorded)
- Links to governance approvals and audit events

### Asset / Infrastructure Item

Represents an asset or infrastructure element.

- Asset ID
- Type (facility, equipment, land, digital asset, etc.)
- Ownership / custodian
- Location (where relevant and policy-permitted)
- Lifecycle state (registered, in use, decommissioned)

### Audit Evidence Package

Represents a collection of events and supporting material.

- Evidence ID
- Scope (time window, program, module)
- Event references
- Attached documents (hashes or pointers)
- Verifier / auditor notes

---

## 2. Event Categories

### Identity Events (T-ID)

Examples:

- `IdentityCredentialIssued`
- `IdentityCredentialRevoked`
- `AccessEligibilityChecked`
- `SelectiveDisclosurePerformed`

Each includes:

- Subject reference
- Issuer/verifier
- Timestamp
- Policy context (e.g., program, legal basis)

### Governance Events (T-Gov)

Examples:

- `ProposalCreated`
- `ProposalEligibilityValidated`
- `ComplianceGatePassed` / `ComplianceGateFailed`
- `VoteCast`
- `ProposalApproved` / `ProposalRejected`
- `ExecutionTriggered`

Each includes:

- Proposal reference
- Actors (proposer, reviewer, voters)
- Decision rationale fields where policy allows
- Links to audit trail events

### Financial Events (T-Finance, T-Stake)

Examples:

- `ProgramDisbursementRecorded`
- `ObligationRegistered`
- `SettlementReferenced`
- `ParticipationIncentiveGranted` (T-Stake)

Each includes:

- Program / project reference
- Amount and currency
- Linked governance approvals
- Compliance flags (e.g., KYC/AML checks where applicable)

### Asset & Infrastructure Events (T-RWA, T-Infra, T-Green, T-Work)

Examples:

- `AssetRegistered`
- `AssetUpdated`
- `InfrastructureMilestoneLogged`
- `ESGTagApplied`
- `WorkCredentialVerified`

Each includes:

- Asset or project reference
- Location / sector where applicable
- ESG/SDG tags (structured fields)
- Links to governance and audit events

### Audit Events (T-Audit)

Examples:

- `AuditLogEntryCreated`
- `EvidencePackageAssembled`
- `OversightAccessGranted`
- `OversightAccessRevoked`

Each includes:

- Scope and modules affected
- Actor and role (e.g., auditor, regulator)
- Integrity proofs (e.g., hash references, anchor references)

---

## 3. SDG & FDI Tagging

Events can carry **SDG and FDI tags** as structured metadata:

- SDG tags (e.g., `SDG:1`, `SDG:9`, `SDG:16`)
- Sector and program codes (aligned to local classifications)
- Investment and funding source references

These tags power the SDG and FDI dashboards (`dashboards/sdg-dashboard.md`, `dashboards/fdi-dashboard.md`).

This model is intentionally abstract and should be specialized per country and institution, with attention to data protection and legal constraints.
