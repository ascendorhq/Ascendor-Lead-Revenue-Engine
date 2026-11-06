
# Ascendor System Requirements

## 1. Purpose

This document defines the functional and non-functional requirements of the Ascendor MVP.

## 2. MVP Scope

The MVP will implement the following business process:

Lead Submission → Validation → Database Storage → Response → Logging

Advanced AI qualification, CRM integration, automated follow-ups, and dashboards are outside the initial MVP scope.

## 3. Functional Requirements

### FR-01: Lead Intake

The system shall accept lead submissions through an HTTP webhook.

### FR-02: Input Validation

The system shall validate required fields and reject invalid submissions.

### FR-03: Data Normalization

The system shall normalize lead information according to defined rules.

### FR-04: Duplicate Detection

The system shall identify duplicate submissions using defined matching criteria.

### FR-05: Database Storage

The system shall persist valid lead records in PostgreSQL.

### FR-06: Response Handling

The system shall return an appropriate response indicating whether the submission was accepted or rejected.

### FR-07: Execution Logging

The system shall provide execution information and error details for troubleshooting.

### FR-08: Error Handling

The system shall handle validation failures, duplicate submissions, and database errors without silently treating failed submissions as successful.

## 4. Initial Lead Data

The MVP lead record is expected to include:

- Lead ID
- Full name
- Email address
- Phone number (optional)
- Lead source
- Lead status
- Created timestamp

The final database schema will define exact field types, constraints, and validation rules.

## 5. Non-Functional Requirements

### NFR-01: Reliability

The system should avoid losing valid lead submissions during normal operation.

### NFR-02: Data Integrity

Lead records shall follow defined database constraints and validation rules.

### NFR-03: Security

The system shall protect credentials and sensitive information.

### NFR-04: Maintainability

Workflows and database structures should be documented and understandable.

### NFR-05: Testability

The MVP shall include test cases for valid submissions, invalid submissions, duplicates, and database failures.

### NFR-06: Observability

The system should provide sufficient execution information to investigate failures.

## 6. MVP Acceptance Criteria

The MVP will be considered functional when:

- A valid lead can be submitted successfully.
- Required fields are validated.
- Invalid submissions are rejected appropriately.
- Duplicate submissions are handled consistently.
- Valid lead records are stored in PostgreSQL.
- Responses accurately reflect processing outcomes.
- Database failures are handled appropriately.
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

## 8. Status

Requirements are documented for the planned MVP.

Implementation and testing have not yet begun.

---

Ascendor — RISE BEYOND.
