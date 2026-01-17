# TEOS Pilot — Sovereign DPI Reference Architecture  
**Concept Note (One Page)**

## 1. Purpose

This pilot uses **TEOS** as a **sovereign Digital Public Infrastructure (DPI) reference architecture** to:

- Improve **traceability and auditability** across identity, governance, finance, and assets  
- Provide **SDG- and FDI-aligned** monitoring via dashboards  
- Test a **compliance-first, non-speculative Web3 posture** under existing laws and regulations  

The pilot is **non-disruptive**: TEOS runs alongside existing systems (ID, PFM, registries) and does **not** replace statutory systems.

Reference: `docs/overview.md`, `docs/architecture.md`, `docs/compliance-framework.md`.

---

## 2. Pilot Scope (Illustrative)

**Domain options** (select one or two to start):

- **Finance / Treasury:** program-linked disbursement transparency (T-Finance, T-Audit, T-API)  
- **Infrastructure / Logistics:** ports, logistics, or public works oversight (T-Infra, T-RWA, T-Audit)  
- **Green / ESG:** renewable or climate-related program tracking (T-Green, T-Infra, T-Audit)  
- **Workforce / Skills:** digital labor or credentialing program (T-Work, T-ID, T-Audit)  

**Core TEOS modules in scope** (tailor per use case):

- **T-ID** — eligibility and credential checks (`modules/core/T-ID.md`)  
- **T-Gov** — proposal and decision lifecycle (`modules/core/T-Gov.md`)  
- **T-Finance** — regulated financial record layer (`modules/core/T-Finance.md`)  
- **T-RWA / T-Infra / T-Green / T-Work** — assets, infrastructure, ESG, workforce (`modules/core/fdi/*.md`)  
- **T-Audit** — immutable audit trail and evidence (`modules/core/T-Audit.md`)  
- **T-API** — integration and dashboard feeds (`modules/core/T-API.md`)  

**Size and boundaries (example):**

- 1 priority program or project window  
- 1–3 participating agencies  
- Limited, well-defined beneficiary / project set  
- Time-bound period (e.g., 6–12 months)  
- Use of SDG and FDI dashboards (`dashboards/sdg-dashboard.md`, `dashboards/fdi-dashboard.md`) for monitoring

---

## 3. Objectives & Expected Outcomes

### Primary Objectives

1. Demonstrate that TEOS can provide:
   - End-to-end **decision → disbursement → execution → audit** traceability  
   - **Audit-ready records** aligned with compliance expectations  
   - **SDG/FDI-tagged** monitoring data for oversight and reporting  

2. Assess **institutional fit**:
   - Alignment with legal, regulatory, and data protection frameworks (`docs/compliance-framework.md`)  
   - Compatibility with existing systems (`docs/integrations.md`)  
   - Clarity of roles for ministries, regulators, and audit bodies  

3. Build a **shared reference** for ministries, DFIs, and partners on how Web3 can function as **DPI**, not speculation (`docs/web3-policy.md`).

### Expected Outcomes

- A documented pilot flow consistent with `diagrams/data-flow.mmd` and `diagrams/governance-flow.mmd`  
- SDG- and sector-tagged event data (per `docs/data-model-and-events.md`, `docs/sdg-teos-matrix.md`)  
- A pilot assessment covering:
  - Benefits (transparency, auditability, reporting)  
  - Risks and safeguards effectiveness (`docs/threat-model.md`)  
  - Options for scale, adaptation, or discontinuation  

---

## 4. Key Metrics

Metrics should be specific to the chosen use case but can be structured as:

### a) Transparency & Auditability

- % of program disbursements **linked to a T-Gov approval** (T-Finance ↔ T-Gov events)  
- % of key identity, governance, and finance events with **T-Audit entries**  
- Time required to assemble an **evidence package** for a sampled transaction or project  

### b) Governance & Compliance

- % of proposals passing through the full lifecycle (proposal → compliance gate → vote → execution)  
- Number of **compliance gate passes/fails** (`ComplianceGatePassed/Failed` events)  
- Number and treatment of **exceptions/overrides** recorded in T-Audit  

### c) Operational Efficiency & Data Quality

- Change in time from **proposal to recorded disbursement**  
- Reduction in manual reconciliation steps between systems (qualitative + quantitative)  
- Data completeness: share of pilot events tagged with **program codes and SDG codes**  

### d) SDG / FDI Monitoring

- Coverage of SDG tags as per `docs/sdg-teos-matrix.md`  
- Share of relevant events with **FDI/program source** references (where applicable)  
- Usage metrics for SDG/FDI dashboards: number of users, frequency of access, feedback

---

## 5. Safeguards & Risk Management

### Legal, Regulatory & Policy

- Pilot conducted **under existing statutes and regulations**  
- Documented **compliance mapping** (public finance, data protection, AML/CFT where relevant)  
- Clear designation of:
  - Data controllers and processors  
  - Oversight and audit authorities  

Reference: `docs/compliance-framework.md`, `docs/compliance.md`.

### Technical & Security

- Pilot uses a **sandboxed or segmented environment**; no production cutover  
- Implementation to follow TEOS **threat model** guidelines (`docs/threat-model.md`)  
- Role-based access controls and logging through T-Audit; integrity anchoring patterns may use external chains (`integrations/*.md`) subject to policy  

### Financial & Fiduciary

- TEOS acts as a **recording and transparency layer**, not a core banking replacement (`modules/core/T-Finance.md`)  
- No consumer-facing token, trading, or speculative functionality (`README.md`, `docs/web3-policy.md`)  
- Existing treasury, banking, and settlement systems remain authoritative  

### Governance & Accountability

- Involvement of internal audit / supreme audit institution from design stage (`modules/core/T-Audit.md`)  
- Documented **issue escalation** and pilot **pause/exit** criteria  
- Periodic reporting to steering committee (ministries, DFIs, regulators)  

---

## 6. Roles & Responsibilities (Illustrative)

- **Lead Line Ministry / Program Owner**  
  - Defines use case, objectives, and policy parameters  
  - Provides operational data and staff  

- **Digital / ICT Authority or GovTech Unit**  
  - Leads TEOS configuration and integrations  
  - Applies national cybersecurity and interoperability standards  

- **Ministry of Finance / Treasury**  
  - Aligns pilot with PFM rules and reporting needs  
  - Validates T-Finance configuration and controls  

- **Regulators & Oversight Bodies**  
  - Review safeguards, access rights, and audit flows  
  - Use T-Audit and dashboards for independent oversight  

- **DFIs / Development Partners** (where involved)  
  - Co-design pilot metrics and SDG/FDI indicators  
  - Support evaluation, capacity building, and independent review  

---

## 7. Illustrative Next Steps

1. **Institutional review** of TEOS docs (`README.md`, `docs/overview.md`, `docs/architecture.md`)  
2. Selection of **pilot program** and confirmation of legal/compliance boundaries  
3. Detailed **requirements and risk assessment** (`docs/threat-model.md`, `docs/compliance-framework.md`)  
4. Configuration of TEOS modules and integrations; deployment of SDG/FDI dashboards  
5. Training of operational, oversight, and audit staff  
6. Time-bound pilot operation with periodic check-ins  
7. Independent evaluation and policy decision on **scale-up or closure**  
