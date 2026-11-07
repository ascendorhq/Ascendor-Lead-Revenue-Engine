
# Ascendor System Requirements

## 1. Purpose

This document defines the functional and non-functional requirements
for the Ascendor Lead-to-Revenue Automation Engine MVP.

## 2. MVP Scope

The MVP will implement the following business process:

Lead Submission → API Intake → Validation → Email Normalization
→ Duplicate Detection → PostgreSQL Storage → Response → Logging

Advanced AI qualification, CRM integration, automated follow-ups,
appointment scheduling, and dashboards are outside the initial MVP scope.

## 3. Functional Requirements

### FR-01: Lead Intake

The system shall accept lead submissions through an HTTP API endpoint.

Initial endpoint:

`POST /api/v1/leads`

### FR-02: Input Validation

The system shall validate required lead fields and reject
invalid submissions with an appropriate response.

### FR-03: Data Normalization

The system shall normalize email addresses by removing
surrounding whitespace and converting them to lowercase.

### FR-04: Duplicate Detection

The system shall identify duplicate lead submissions
using email address uniqueness.

Duplicate submissions shall be rejected consistently.

### FR-05: Database Storage

The system shall persist valid lead records in PostgreSQL.

Database constraints shall enforce data integrity.

### FR-06: Response Handling

The system shall return appropriate HTTP responses
indicating whether a submission was accepted or rejected.

### FR-07: Execution Logging

The application shall provide logging information
for errors and troubleshooting.

### FR-08: Error Handling

The system shall handle validation failures,
duplicate submissions, and database errors
without silently treating failed submissions as successful.

## 4. Initial Lead Data

The lead record shall support the following information:

- Lead ID
- Full name
- Email address
- Phone number
- Company name
- Lead source
- Lead status
- Qualification status
- Lead score
- Estimated revenue
- Actual revenue
- Conversion timestamp
- Created timestamp
- Updated timestamp

The database schema defines the field types,
constraints, and default values.

## 5. Non-Functional Requirements

### NFR-01: Reliability

The system should avoid losing valid lead submissions
during normal operation.

### NFR-02: Data Integrity

Lead records shall follow defined database constraints
and application validation rules.

### NFR-03: Security

The system shall protect credentials and sensitive information.

Database services shall not be unnecessarily exposed
to public network access.

### NFR-04: Maintainability

Application modules, workflows, and database structures
shall be documented and understandable.

### NFR-05: Testability

The MVP shall include automated test cases for:

- Valid lead submissions
- Invalid lead submissions
- Email normalization
- Duplicate submissions
- Database failures
- API response handling

### NFR-06: Observability

The application shall provide sufficient logging
and execution information to investigate failures.

## 6. MVP Acceptance Criteria

The MVP will be considered functionally verified
when the following criteria are satisfied:

- A valid lead can be submitted successfully.
- Required fields are validated.
- Invalid submissions are rejected appropriately.
- Email addresses are normalized consistently.
- Duplicate submissions are handled consistently.
- Valid lead records are stored in PostgreSQL.
- API responses accurately reflect processing outcomes.
- Database failures are handled appropriately.
- Automated tests execute successfully.
- Test results are documented.

## 7. Out of Scope

The initial MVP does not include:

- AI lead qualification
- AI-generated sales messages
- CRM synchronization
- Automated email follow-ups
- Appointment scheduling
- Sales dashboards
- Multi-tenant production deployment
- Production cloud deployment

## 8. Implementation Status

Requirements are documented.

Application foundation:
Prepared.

Database schema:
Prepared.

Automated test files:
Prepared.

Runtime verification:
Pending.

Deployment:
Not yet deployed.

Production readiness:
Not yet achieved.

## 9. Future Extensions

Future versions may introduce:

- AI-powered lead qualification
- Advanced lead scoring
- CRM integrations
- Automated follow-up sequences
- Appointment booking
- Revenue tracking and analytics
- Monitoring and alerting
- Production cloud infrastructure
- Multi-tenant architecture

---

Ascendor — RISE BEYOND.
