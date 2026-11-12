
# Ascendor Flagship 01 — Master Architecture & Implementation Blueprint

**Project:** Ascendor AI Lead Generation & Revenue Engine  
**Document:** Master Architecture & Implementation Blueprint  
**Version:** 1.0  
**Status:** Architecture Baseline  
**Architecture Type:** Multi-Tenant SaaS  
**Primary Objective:** Reliable, Secure, Premium, Usable, and Scalable SaaS

---

## 1. Executive Summary

Ascendor Flagship 01 is a multi-tenant SaaS platform designed to help businesses capture leads, qualify opportunities, manage their sales pipeline, automate follow-ups, coordinate appointments, and understand revenue performance.

The platform must provide reliable business automation without sacrificing data security, operational integrity, usability, or customer trust.

Ascendor will use a modular architecture built around:

- Next.js and TypeScript for the application interface and server-side application logic.
- Supabase Auth for authentication.
- PostgreSQL for persistent business data.
- Supabase Row-Level Security (RLS) for database authorization.
- n8n for background automation and workflow orchestration.
- AI providers for evidence-based lead analysis and assistance.
- External integrations for lead sources, communication, calendars, and CRM systems.

The architecture prioritizes a secure and practical MVP while establishing a foundation that can evolve into a larger SaaS platform.

## 2. Architectural Philosophy

Ascendor follows these principles:

1. Security must be enforced, not assumed.
2. Organization isolation must exist at the database level.
3. Business rules must have one authoritative implementation.
4. Important business operations must be durable and recoverable.
5. External integrations must never compromise internal data integrity.
6. AI may assist decisions but cannot bypass authorization.
7. Historical business records must remain trustworthy.
8. Every important action must be traceable.
9. The interface must remain simple despite complex underlying systems.
10. Scalability must be introduced when justified by measurable needs.
11. Production readiness requires demonstrated evidence.
12. Documentation, implementation, and testing must remain synchronized.

### Product Philosophy

> Powerful underneath. Simple on the surface. Premium in every interaction.

## 3. Final SaaS Architecture

### 3.1 Architecture Model

Ascendor uses a shared-application, multi-tenant SaaS architecture with organization-scoped data access.

The initial deployment uses shared application infrastructure and a shared PostgreSQL database, with tenant-owned records protected through organization relationships, database constraints, authorization policies, and RLS.

Customers share the platform infrastructure but cannot access another organization's business data.

Dedicated customer environments may be introduced later as an enterprise deployment option.

### 3.2 System Components

#### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Accessible reusable UI components
- Responsive dashboard layouts

Responsibilities:

- Render dashboard and business interfaces.
- Display authorized information.
- Collect user input.
- Provide clear interaction feedback.
- Support organization switching.
- Present loading, empty, error, and success states.

The frontend is never an authorization authority.

#### Application Layer

Next.js Server Components, Server Actions, and Route Handlers provide the trusted application boundary.

Responsibilities:

- Validate requests.
- Verify authenticated identity.
- Verify organization membership.
- Enforce role and record-level permissions.
- Apply business rules.
- Perform authorized database operations.
- Publish durable business events.
- Return predictable responses.

#### Database Layer

Supabase PostgreSQL stores authoritative business data.

Responsibilities:

- Persist business records.
- Enforce relationships and constraints.
- Maintain transactional consistency.
- Apply RLS.
- Preserve historical records.
- Support reporting and analytics.

#### Automation Layer

n8n executes background business workflows.

Responsibilities:

- Process durable business events.
- Execute follow-up sequences.
- Coordinate external integrations.
- Handle scheduling and retries.
- Produce automation execution records.
- Report failures for recovery.

n8n is not the authoritative source of business permissions or business state.

#### AI Layer

AI providers assist with:

- Lead information extraction.
- Qualification recommendations.
- Personalization suggestions.
- Sales summaries.
- Evidence-based insights.

AI output is untrusted until validated.

#### Integration Layer

External integrations may include:

- Website lead forms.
- Facebook lead capture.
- Email providers.
- Calendar providers.
- CRM integrations.
- AI providers.

All external integrations must use isolated credentials, validated inputs, and controlled execution.

### 3.3 Logical Architecture

```text
Users
  |
  v
Next.js Application
  |
  +-- Authentication
  +-- Organization Context
  +-- Authorization
  +-- Business Logic
  +-- Dashboard
  |
  v
Supabase PostgreSQL
  |
  +-- Tenant Data
  +-- RLS
  +-- Constraints
  +-- Business Events
  +-- Outbox
  |
  v
Automation Workers / n8n
  |
  +-- AI Qualification
  +-- Follow-Up
  +-- Appointments
  +-- Notifications
  +-- Integrations
  |
  v
External Providers
```

The application and database remain authoritative for business data, permissions, and state.

## 4. Multi-Tenant Organization Model

### 4.1 Organization Structure

Ascendor uses the following logical relationships:

- User
- Organization
- Organization Membership
- Organization Role
- Record Assignment
- Business Records

A user may belong to multiple organizations.

An organization may contain multiple users.

Each organization membership has its own role and status.

### 4.2 Organization Context

Organization context must be verified server-side.

The application must:

1. Authenticate the user.
2. Identify the requested organization.
3. Verify active membership.
4. Resolve the user's role.
5. Apply record-level permissions.
6. Execute the operation within the authorized organization.

An organization slug is a navigation identifier, not proof of authorization.

Incoming organization identifiers must never independently grant access.

### 4.3 Tenant Isolation

Every tenant-owned record must have a valid organization relationship.

Tenant isolation must be enforced through:

- Organization-aware database relationships.
- Appropriate database constraints.
- RLS policies.
- Server-side authorization.
- Tenant-aware queries.
- Tenant-aware analytics.
- Tenant-aware caching.
- Tenant-aware automation execution.

Cross-organization access must be denied by default.

## 5. Authentication and Authorization

### 5.1 Authentication

Supabase Auth manages user identity and authentication.

Authentication answers:

> Who is the user?

Organization membership and permissions answer:

> What may this user access or perform?

These are separate responsibilities.

### 5.2 Authorization

Authorization must be enforced at trusted server boundaries and at the database level wherever applicable.

The system must verify:

- Authenticated identity.
- Active organization membership.
- Organization role.
- Record assignment where applicable.
- Permission for the requested operation.
- Valid business state.
- Relevant approval or consent requirements.

Hiding interface elements is not authorization.

### 5.3 Initial Permission Model

| Role | Initial Access |
|---|---|
| Owner | Full organization administration and business access |
| Admin | Organization management and authorized business operations |
| Sales Manager | Team pipeline and authorized sales operations |
| Sales Representative | Assigned leads and associated authorized records |

Sales Representatives access assigned leads by default.

Owners, Admins, and authorized Sales Managers may access broader organization records according to explicit permissions.

The same permission model must apply consistently to leads, appointments, analytics, notifications, exports, and other business data.

### 5.4 Ownership Protection

Ascendor must prevent:

- Removal of the last organization owner.
- Unauthorized ownership transfers.
- Unauthorized role changes.
- Unauthorized membership modifications.
- Unauthorized invitation acceptance.
- Access through inactive memberships.

Ownership transfers and consequential role changes require explicit authorization and appropriate confirmation.

## 6. Database Architecture

### 6.1 Database Principles

PostgreSQL is the authoritative persistent data store.

Database design must prioritize:

- Referential integrity.
- Organization isolation.
- Transactional consistency.
- Reliable business history.
- Explicit relationships.
- Appropriate indexes.
- Predictable query performance.

### 6.2 Core Business Entities

The architecture includes the following logical entities:

- Organizations
- Profiles
- Organization Memberships
- Invitations
- Lead Sources
- Contacts
- Leads
- Lead Assignments
- Lead Activities
- Qualification Assessments
- Qualification Evidence
- Scoring Configurations
- Pipeline Stages
- Opportunities
- Opportunity Stage History
- Appointments
- Appointment History
- Communications
- Communication Events
- Follow-Up Sequences
- Business Events
- Automation Executions
- Outbox Records
- Integration Accounts
- Notification Records
- Security Audit Events

Additional tables may be introduced when required by implementation.

### 6.3 Tenant-Aware Relationships

Tenant-owned relationships must prevent cross-organization references.

For example:

- An appointment must reference an opportunity or lead belonging to its organization.
- A lead assignment must reference a valid organization member.
- An opportunity must reference valid organization-owned records.
- A pipeline stage must belong to the opportunity's organization.

Where appropriate, composite organization-aware foreign keys must enforce these relationships directly in PostgreSQL.

### 6.4 Database Security

The database security model must include:

- Explicit database grants.
- RLS enabled on exposed tenant-owned tables.
- Policies for SELECT, INSERT, UPDATE, and DELETE as appropriate.
- Correct handling of authenticated and privileged database roles.
- Restricted exposed schemas.
- Hardened database functions.
- Automated authorization tests.
- Explicit protection for sensitive records.

RLS must be treated as one layer of defense rather than the entire security configuration.

### 6.5 Transactions

Related operations must execute atomically when business integrity requires it.

Examples:

- Creating an organization and its initial owner membership.
- Accepting an invitation and activating membership.
- Creating a lead and its initial activity.
- Recording a business event and its outbox entry.
- Updating a pipeline stage and recording stage history.
- Creating an appointment and its associated business records.

Partial success must not silently corrupt business state.


## 7. Lead-to-Revenue Business Architecture

### 7.1 Business Lifecycle

Ascendor Flagship 01 follows a structured lead-to-revenue lifecycle:

1. Lead Capture
2. AI Lead Qualification
3. CRM and Lead Scoring
4. Automated Follow-Up
5. Appointment and Sales Handoff
6. Revenue Intelligence

Each module must have clear responsibilities, defined data ownership, reliable transitions, and controlled interactions with other modules.

### 7.2 Lead Capture

Lead Capture must support multiple authorized sources, including website forms, approved Facebook integrations, and internal dashboard entry.

The system must:

- Resolve organization context through trusted authorization mechanisms.
- Validate and normalize incoming lead information.
- Authenticate external sources where required.
- Apply duplicate detection and documented duplicate-handling rules.
- Support idempotent processing of retried requests.
- Persist accepted leads reliably.
- Record appropriate business activity and source attribution.
- Create durable automation events for downstream processing.
- Recover from temporary integration and processing failures.

Lead acceptance must not depend on AI qualification, email delivery, or unrelated external integrations completing successfully.

Ascendor should acknowledge successful acceptance only after the lead has been durably persisted or safely recorded for processing.

### 7.3 AI Lead Qualification

AI Lead Qualification must transform available lead information into structured, evidence-supported qualification results.

The system must:

- Use approved organization-specific qualification criteria.
- Maintain versioned qualification rules and prompts.
- Distinguish observed information from AI interpretation.
- Preserve evidence supporting qualification decisions.
- Identify missing, unknown, or contradictory information.
- Record confidence and qualification outcomes separately from lead score.
- Validate AI output before accepting it.
- Support provider failures, retries, and controlled fallback behavior.
- Route uncertain or sensitive cases for human review when required.
- Preserve qualification history for auditability and reporting.

AI must not independently authorize sensitive business actions, bypass organization permissions, or execute unrestricted operations.

### 7.4 CRM and Lead Scoring

The CRM must maintain the authoritative operational state of each lead.

Lead scoring must use deterministic, versioned business rules wherever practical. AI-generated signals may contribute only through explicitly approved scoring inputs.

Ascendor must distinguish:

- Lead Score: numerical assessment of lead priority.
- Qualification Status: whether a lead meets defined business criteria.
- Lead Stage: the current operational position in the sales pipeline.
- Assignment: the authorized person or team responsible for the lead.
- Revenue Estimates: expected or potential revenue.
- Actual Revenue: revenue supported by authoritative business records.

The CRM must support:

- Controlled lead-stage transitions.
- Validation of permitted state changes.
- Optimistic concurrency and conflict detection.
- Immutable stage-transition history.
- Assignment validation and ownership safeguards.
- Search, filtering, sorting, and server-side pagination.
- Activity history and accountable user actions.
- Explicit reopening rules for closed leads.
- Consistent distinction between estimated and actual revenue.

Sales Representatives should access assigned leads by default unless an explicitly approved permission grants broader access.

### 7.5 Automated Follow-Up

Automated Follow-Up must operate through controlled, recoverable communication workflows.

Before sending a communication, Ascendor must revalidate relevant conditions, including:

- Organization authorization.
- Lead and sequence eligibility.
- Communication consent and suppression rules.
- Whether the lead has replied.
- Whether an appointment or conversion changes eligibility.
- Whether the sequence has been cancelled or paused.
- Whether human approval is required.
- Whether the intended communication has already been processed.

Ascendor must preserve communication records, approved message content, provider references, delivery events, and execution history.

External communication outcomes may be ambiguous. A provider timeout does not necessarily mean the message was not sent.

The system must reconcile uncertain outcomes where possible instead of blindly repeating communications.

Exactly-once delivery across external providers must not be assumed.

### 7.6 Appointment and Sales Handoff

Appointment and Sales Handoff must maintain an authoritative Ascendor appointment record independently of external calendar synchronization.

The system must support:

- Appointment creation and validation.
- Availability and conflict checks.
- Idempotent booking requests.
- Controlled rescheduling and cancellation.
- Appointment lifecycle tracking.
- Timezone-aware scheduling.
- Reminder eligibility and delivery tracking.
- External calendar synchronization.
- Secure calendar integration credentials.
- Defined sales handoff responsibilities.
- Handoff deadlines and escalation policies.

Calendar synchronization success does not automatically mean the entire Ascendor appointment transaction has succeeded.

External calendar conflicts, failures, and uncertain outcomes must be reconciled against the authoritative appointment record.

### 7.7 Revenue Intelligence

Revenue Intelligence must transform operational business records into accurate, reproducible reporting.

Every KPI must have:

- An exact numerator.
- An exact denominator where applicable.
- A defined reporting period.
- Explicit inclusion and exclusion rules.
- A documented source of truth.
- Defined treatment of missing or incomplete information.
- A clear distinction between event-time reporting and record-creation reporting.

Ascendor must distinguish:

- Lead creation.
- Lead qualification.
- Appointment booking.
- Sales opportunity creation.
- Opportunity conversion.
- Revenue estimation.
- Revenue recognition or recording.
- Actual payment collection.

Revenue reporting must preserve attribution, historical changes, timezone consistency, currency handling, and tenant isolation.

Historical reporting must remain explainable even when operational records subsequently change.

---

## 8. Business Events and Automation Architecture

### 8.1 Business Events

Ascendor must use durable, tenant-scoped business events to connect operational modules with asynchronous automation.

Examples include:

- `lead.created`
- `lead.updated`
- `lead.qualified`
- `lead.assigned`
- `lead.stage_changed`
- `follow_up.requested`
- `communication.sent`
- `appointment.booked`
- `appointment.rescheduled`
- `appointment.cancelled`
- `opportunity.won`
- `revenue.recorded`

Events must have defined schemas, versioning, identifiers, organization context, and idempotent processing behavior.

Business history must remain in Ascendor's authoritative database rather than depending exclusively on n8n execution history.

### 8.2 Transactional Outbox

Ascendor must implement a transactional outbox pattern for important business events.

The authoritative business record and its corresponding outbox event must be created or updated within the same database transaction.

A separate dispatcher must publish pending events to the appropriate automation system.

The outbox must support:

- Durable event persistence.
- Retryable dispatch.
- Duplicate-safe processing.
- Delivery tracking.
- Failed-event classification.
- Dead-letter handling.
- Operational reconciliation.
- Manual recovery when appropriate.

This prevents business records from being successfully committed while their required automation events are silently lost.

### 8.3 n8n Security Architecture

n8n must operate as a workflow orchestration system, not as an unrestricted authority over the entire Ascendor database.

Where practical, n8n should interact with Ascendor through narrowly scoped, authenticated application operations.

Every automation-triggered operation must:

1. Authenticate the automation request.
2. Verify organization and event context.
3. Validate the referenced records.
4. Enforce the intended business permissions.
5. Apply idempotency protections.
6. Record execution and business outcomes.

Supabase service-role credentials must never be exposed to browsers, client-side applications, or untrusted users.

Privileged automation credentials must be securely stored, restricted, monitored, and rotated when necessary.

### 8.4 Automation Reliability

Ascendor must maintain durable automation execution tracking independently of temporary workflow execution state.

Automation reliability must include:

- Explicit execution status.
- Bounded retry policies.
- Error classification.
- Idempotent business operations.
- Dead-letter handling.
- Reconciliation of uncertain outcomes.
- Manual recovery procedures.
- Operational alerts.
- Traceability between business records, events, and automation executions.

Retries must not blindly repeat an entire business process when only one operation failed.

---

## 9. Next.js Dashboard Architecture

### 9.1 Application Responsibilities

The Next.js application must provide the authenticated user interface and trusted application operations.

The architecture should use:

- **Server Components** for initial page rendering and server-side data loading.
- **Server Actions** for appropriate authenticated application mutations.
- **Route Handlers** for webhooks, external integrations, and API endpoints.
- **Client Components** for interactive interface behavior.
- **Supabase** for authentication, database access, and database-enforced authorization.
- **n8n** for asynchronous workflow orchestration.
- **Trusted server-side boundaries** for privileged operations.

Sensitive operations must not rely on frontend visibility, client-side validation, or client-provided organization identifiers alone.

### 9.2 Organization Switching

Organization switching must be treated as a security-sensitive context change.

When a user switches organizations, Ascendor must:

1. Revalidate the user's active organization membership.
2. Confirm that the membership is authorized and active.
3. Update the trusted organization context.
4. Invalidate organization-dependent cached data.
5. Reset stale client-side state.
6. Revalidate relevant queries and permissions.
7. Prevent previous-organization data from appearing in the new context.

Organization identifiers and slugs must not be treated as proof of authorization.

### 9.3 Dashboard and KPI Consistency

Dashboard reporting must use consistent definitions, filters, timezones, and currency rules.

The dashboard must distinguish pipeline metrics from actual revenue metrics.

Each reporting component must handle:

- Loading states.
- Empty states.
- Errors.
- Partial data where appropriate.
- Permission-restricted information.
- Reporting-period selection.
- Organization-specific timezone settings.

Important aggregations should be performed through appropriately secured server-side queries or database functions.

### 9.4 CRM Interaction Architecture

Lead interactions must be validated through trusted application operations.

Every mutation must verify:

- Active organization membership.
- Required role or permission.
- Record ownership or assignment restrictions.
- Permitted lifecycle transitions.
- Concurrency and conflict conditions.
- Business validation rules.

Successful operations must generate appropriate business history and user feedback.

Conflicting updates must be communicated clearly rather than silently overwriting newer changes.

### 9.5 User Experience Standards

Ascendor must provide a premium, consistent, and accessible interface.

The interface should include:

- Responsive layouts for desktop, tablet, and mobile.
- Accessible contrast and keyboard navigation.
- Predictable navigation and information hierarchy.
- Consistent spacing, typography, and interaction patterns.
- Clear loading, success, empty, and error states.
- Efficient CRM tables and filtering.
- Confirmation for consequential actions.
- Helpful validation messages.
- Appropriate feedback for asynchronous operations.

The dashboard must remain usable when handling hundreds or thousands of leads rather than being optimized only for small demonstrations.

---

## 10. Security Architecture

### 10.1 Defense in Depth

Ascendor must implement multiple independent security layers.

These include:

- Authentication.
- Organization membership validation.
- Role and record-level authorization.
- PostgreSQL Row Level Security.
- Explicit database grants and privileges.
- Server-side validation.
- Secure credential management.
- Rate limiting and abuse protection.
- Security audit logging.
- Tenant-isolation testing.

RLS must not be treated as the only security mechanism.

Privileged database functions, service-role operations, and automation access must receive additional security review.

### 10.2 AI Security

AI-related security must include:

- Prompt-injection resistance.
- Strict input and output validation.
- Structured output schemas.
- Approved knowledge sources.
- Evidence-based business decisions.
- Restricted tool permissions.
- Human approval for sensitive actions.
- Protection against unauthorized data disclosure.
- Tenant-aware AI context.
- Monitoring of suspicious or invalid outputs.

AI must never receive unrestricted authority to access other organizations' data or bypass application authorization.

### 10.3 Logging Separation

Ascendor must maintain separate logging responsibilities for:

- Business activity history.
- Security audit events.
- Application errors.
- Automation execution.
- Integration delivery.
- Performance and operational monitoring.

Logs must avoid unnecessary sensitive information and must follow appropriate retention and access-control policies.

### 10.4 Internal Access Security

Administrative and support access must follow explicit authorization rules.

Privileged access must be:

- Limited to authorized personnel.
- Justified by operational responsibilities.
- Auditable.
- Revocable.
- Restricted from unnecessary client data exposure.

Internal access must not become an unrestricted mechanism for bypassing tenant isolation.

---

## 11. Testing Strategy

### 11.1 Unit Testing

Unit tests must validate isolated business logic, including:

- Input normalization.
- Validation rules.
- Lead scoring.
- Qualification rules.
- State transitions.
- KPI calculations.
- Idempotency logic.
- Eligibility decisions.
- Permission-related business rules.

Tests must include normal cases, edge cases, invalid inputs, and failure conditions.

### 11.2 Integration Testing

Integration tests must validate interactions between:

- Application services.
- PostgreSQL.
- Supabase Auth.
- Database functions.
- RLS policies.
- Transactional outbox.
- Event dispatchers.
- External integration adapters.
- Automation workflows.

Integration tests must verify that failures are handled without corrupting authoritative business state.

### 11.3 Database and Security Testing

Database tests must validate:

- Schema constraints.
- Foreign keys.
- Composite organization relationships.
- Unique constraints.
- Transactional behavior.
- RLS policies.
- Database grants.
- Unauthorized access rejection.
- Cross-organization access prevention.
- Assignment restrictions.
- Privileged operation safeguards.

Security tests must verify actual database and application behavior rather than relying only on frontend restrictions.

### 11.4 Tenant Isolation Testing

Tenant isolation must be tested explicitly across organizations.

Tests must include:

- Organization A attempting to read Organization B's leads.
- Organization A attempting to modify Organization B's records.
- Unauthorized organization switching.
- Cross-tenant relationship creation.
- Cross-tenant search and reporting.
- Unauthorized access through API endpoints.
- Privileged automation requests with invalid organization context.
- Organization-dependent cache and state leakage.

Tenant isolation must be validated using actual database policies and application request paths.

### 11.5 End-to-End Testing

End-to-end tests must validate complete business journeys.

At minimum, Ascendor must test:

1. Lead submission.
2. Lead persistence.
3. Qualification processing.
4. CRM scoring and assignment.
5. Follow-up eligibility.
6. Communication execution.
7. Appointment booking.
8. Sales handoff.
9. Opportunity conversion.
10. Revenue recording.
11. Revenue reporting.

Failure scenarios must include retries, provider errors, duplicate requests, authorization failures, and recovery.

### 11.6 Performance and Usability Testing

Testing must include:

- Large lead datasets.
- Server-side pagination.
- Database query performance.
- Concurrent updates.
- Automation throughput.
- Retry and recovery behavior.
- Dashboard responsiveness.
- Accessibility.
- Mobile usability.
- Organization switching.
- User task completion.

Performance and usability must be evaluated using realistic workloads and actual user workflows.


## 12. Reliability and Operational Architecture

### 12.1 Backup and Recovery

Ascendor must maintain a documented backup and recovery strategy.

The strategy must define:

- Backup frequency.
- Backup retention.
- Backup storage security.
- Recovery Point Objective (RPO).
- Recovery Time Objective (RTO).
- Recovery responsibilities.
- Backup verification.
- Restoration testing.

Backups must be protected against unauthorized access and accidental deletion.

A backup must not be considered reliable until restoration has been successfully tested.

### 12.2 Monitoring and Alerting

Ascendor must monitor critical application and infrastructure components.

Monitoring must cover:

- Application availability.
- Database health.
- API errors and latency.
- Authentication failures and suspicious access patterns.
- Automation execution failures.
- Outbox delivery delays.
- Integration failures.
- Communication delivery problems.
- Database performance.
- Resource utilization.
- Background processing delays.

Alerts must have defined severity levels, responsible owners, and escalation procedures.

Monitoring must help detect failures before they significantly affect client operations.

### 12.3 Deployment and Migration Management

Production deployments must use controlled, versioned processes.

The deployment process must include:

1. Version-controlled application changes.
2. Reviewed database migrations.
3. Defined migration execution order.
4. Compatibility considerations.
5. Deployment verification.
6. Monitoring after deployment.
7. Documented rollback or recovery procedures.

Destructive database changes must receive additional review and must not be performed casually.

Database migrations must preserve data integrity and avoid unnecessary production downtime.

### 12.4 Incident Management

Ascendor must maintain an incident response process.

The process must define:

- Incident classification.
- Severity levels.
- Response responsibilities.
- Escalation procedures.
- Client communication responsibilities.
- Recovery procedures.
- Incident documentation.
- Post-incident review.

Critical incidents must be investigated to identify their underlying causes.

Corrective actions should improve system reliability rather than merely resolving immediate symptoms.

---

## 13. Client Deployment and Commercial Architecture

### 13.1 Default SaaS Deployment Model

Ascendor will initially operate using a shared-application, multi-tenant SaaS architecture.

The default model provides:

- One centrally managed application.
- Shared application infrastructure.
- Organization-isolated business data.
- Organization-specific configuration.
- Organization-specific integrations.
- Role-based access.
- Centralized monitoring and maintenance.
- Controlled platform updates.

Each client organization operates independently within its authorized organizational context.

The shared SaaS model is the default deployment approach for the MVP and initial commercial offering.

### 13.2 Organization Onboarding

Client onboarding must follow a controlled process.

Onboarding must include:

- Organization creation.
- Initial owner assignment.
- Authorized member invitations.
- Role assignment.
- Organization configuration.
- Integration configuration.
- Qualification and scoring configuration.
- Communication settings.
- Security validation.
- Initial operational verification.

A client must not begin production operations until the required configuration and security checks have been completed.

### 13.3 Dedicated Client Deployment

Dedicated client environments may be introduced later as an enterprise deployment option.

Dedicated deployment may provide:

- Isolated application environments.
- Dedicated databases or infrastructure.
- Client-specific deployment configurations.
- Separate operational monitoring.
- Custom integration environments.
- Additional security controls.
- Dedicated recovery and maintenance procedures.

Dedicated deployment must have clearly defined operational ownership, maintenance responsibilities, security boundaries, and support arrangements.

It must not be introduced into the MVP unless a justified business requirement exists.

### 13.4 Client Offboarding

Client offboarding must be controlled and documented.

Offboarding must include:

- Revocation of user access.
- Revocation of integration credentials.
- Disabling active automation.
- Handling pending communications and appointments.
- Exporting authorized client data when required.
- Applying documented retention and deletion policies.
- Recording offboarding completion.

Client data must not be retained indefinitely without a legitimate retention basis.

---

## 14. Production Readiness

Ascendor must distinguish between development readiness, pilot readiness, and production readiness.

### 14.1 Development Ready

A component is development ready when:

- Its implementation exists.
- Its intended behavior is documented.
- Relevant unit tests pass.
- Basic integration behavior is verified.
- Known limitations are documented.

Development readiness does not establish production reliability.

### 14.2 Pilot Ready

A component or system is pilot ready when:

- Core business workflows function correctly.
- Authentication and tenant isolation have been tested.
- Important failure scenarios have been evaluated.
- Basic monitoring is available.
- Recovery procedures are documented.
- Client onboarding requirements are defined.
- Known risks and limitations are communicated.
- Human oversight exists for critical operations.

Pilot readiness permits controlled validation with limited users and clearly defined operational boundaries.

### 14.3 Production Ready

Ascendor must not declare production readiness solely because the application works during a demonstration.

Production readiness requires evidence that:

- Core workflows operate reliably.
- Authorization and tenant isolation are validated.
- Database constraints and security policies are tested.
- Critical business operations are recoverable.
- External integration failures are handled safely.
- Automated tests cover important business journeys.
- Monitoring and alerting are operational.
- Backup restoration has been verified.
- Deployment and migration procedures are documented.
- Incident response responsibilities are defined.
- Performance has been evaluated against realistic workloads.
- Client onboarding and offboarding are controlled.
- Operational risks are understood and accepted.

Production readiness must be based on demonstrated behavior, test results, and operational evidence.

---

## 15. MVP Scope

### 15.1 MVP Objectives

The Ascendor Flagship 01 MVP must demonstrate a complete, reliable lead-to-revenue workflow for a real business use case.

The MVP must prioritize operational reliability, security, and usability over unnecessary feature expansion.

### 15.2 Included MVP Capabilities

The MVP must include:

- Authentication.
- Organization creation and membership.
- Role-based authorization.
- Database-enforced tenant isolation.
- Secure lead capture.
- Lead validation and duplicate handling.
- CRM lead management.
- Deterministic lead scoring.
- AI-assisted lead qualification.
- Qualification history.
- Assignment and lead-stage management.
- Automated follow-up.
- Communication records.
- Appointment management.
- Sales handoff.
- Revenue-related opportunity tracking.
- Core revenue intelligence.
- Business activity history.
- Automation execution tracking.
- Error handling and recovery.
- Basic operational monitoring.
- Automated testing.
- Client onboarding.
- Production validation procedures.

### 15.3 Deferred Enhancements

The following capabilities may be introduced after MVP validation:

- Advanced predictive analytics.
- Advanced AI sales recommendations.
- Complex forecasting models.
- Sophisticated territory management.
- Advanced assignment optimization.
- Extensive third-party CRM integrations.
- Dedicated enterprise environments.
- Advanced custom reporting.
- Cross-flagship ecosystem integrations.
- More complex revenue attribution models.

Deferred capabilities must not compromise the reliability or security of the initial product.

---

## 16. Implementation Roadmap

Implementation must follow a dependency-aware sequence.

### Phase 1 — Foundation

Establish:

- Next.js application structure.
- TypeScript configuration.
- Tailwind CSS.
- Supabase project.
- Environment configuration.
- Development workflow.
- Initial testing setup.

### Phase 2 — Authentication and Organizations

Implement:

- Authentication.
- Organization creation.
- Organization membership.
- Invitation handling.
- Role definitions.
- Organization switching.
- Membership validation.

### Phase 3 — Database Security

Implement:

- Core database schema.
- Tenant-aware relationships.
- Database constraints.
- RLS policies.
- Explicit database grants.
- Security testing.
- Tenant isolation validation.

### Phase 4 — Dashboard Foundation

Implement:

- Application layout.
- Navigation.
- Organization context.
- Dashboard structure.
- Loading and error states.
- Design system foundations.
- Responsive interface.

### Phase 5 — Lead Capture and CRM

Implement:

- Lead creation.
- Lead validation.
- Duplicate handling.
- Lead listing.
- Search and filtering.
- Lead scoring.
- Assignment.
- Lead-stage management.
- Activity history.

### Phase 6 — AI Qualification

Implement:

- Qualification criteria.
- AI provider integration.
- Structured output validation.
- Evidence handling.
- Qualification history.
- Confidence and review behavior.
- Failure handling.

### Phase 7 — Automation

Implement:

- Business event architecture.
- Transactional outbox.
- Event dispatcher.
- n8n integration.
- Follow-up sequences.
- Communication records.
- Retry and recovery mechanisms.

### Phase 8 — Appointments and Sales Handoff

Implement:

- Appointment records.
- Booking and lifecycle management.
- Calendar integration.
- Reminder workflows.
- Sales handoff.
- Handoff tracking.

### Phase 9 — Revenue Intelligence

Implement:

- KPI definitions.
- Revenue-related data structures.
- Reporting queries.
- Pipeline metrics.
- Conversion metrics.
- Revenue reporting.
- Dashboard analytics.

### Phase 10 — Hardening and Validation

Implement and verify:

- Comprehensive tenant isolation tests.
- End-to-end business workflow tests.
- Integration failure testing.
- Automation recovery testing.
- Performance validation.
- Backup restoration testing.
- Monitoring and alerting.
- Security review.
- Pilot validation.
- Production readiness assessment.

Each phase must have defined completion criteria before dependent work is considered ready.

---

## 17. Future Scalability

Ascendor must be designed to support growth without introducing unnecessary complexity prematurely.

Scalability improvements should be introduced based on measured operational requirements.

Potential future improvements include:

- Database query optimization.
- Additional indexes.
- Connection pooling.
- Improved caching.
- Background processing optimization.
- Event processing improvements.
- Read replicas where justified.
- Dedicated enterprise environments.
- Infrastructure scaling.
- Advanced monitoring.
- Integration capacity management.
- Data archival strategies.

The initial architecture must preserve clear boundaries and reliable data ownership so future scaling remains manageable.

Ascendor must not introduce distributed systems, microservices, or complex infrastructure merely for architectural appearance.

Scalability must serve actual business demand.

---

## 18. Architecture Governance

### 18.1 Architectural Decision Management

Important architectural decisions must be documented and reviewed.

Decision records should include:

- Decision title.
- Problem or requirement.
- Considered alternatives.
- Selected approach.
- Reason for selection.
- Security implications.
- Operational implications.
- Known trade-offs.
- Future reconsideration conditions.

### 18.2 Architecture Change Requirements

Architecture changes must preserve:

- Tenant isolation.
- Data integrity.
- Authorization correctness.
- Business workflow consistency.
- Reliability.
- Maintainability.
- Testability.
- Operational recovery.

Changes affecting security, database relationships, business state transitions, or automation reliability must receive additional validation.

### 18.3 Documentation and Implementation Consistency

Architecture documentation must remain aligned with the actual implementation.

When implementation decisions change, the relevant architecture documents, database design, security policies, and tests must be updated.

Documentation must not claim capabilities that have not been implemented or verified.

Architecture specifications describe intended behavior; production evidence establishes actual behavior.

---

## 19. Final Architecture Statement

Ascendor Flagship 01 is designed as a secure, reliable, multi-tenant SaaS platform that transforms incoming business leads into measurable revenue outcomes through structured business workflows, AI-assisted qualification, CRM management, automated communication, appointment coordination, sales handoff, and revenue intelligence.

The architecture prioritizes:

- Security by design.
- Tenant isolation.
- Reliable business transactions.
- Controlled automation.
- Evidence-based AI.
- Recoverable operations.
- Accurate business reporting.
- Premium user experience.
- Maintainable implementation.
- Measurable production readiness.

The product must remain powerful underneath and simple on the surface.

Every architectural decision must support the central objective:

**Build Ascendor into a dependable, secure, scalable, and commercially valuable revenue automation platform that businesses can confidently use in real operations.**

