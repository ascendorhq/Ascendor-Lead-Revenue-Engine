
# Ascendor Database Design

## 1. Purpose

This document defines the initial database structure for the Ascendor MVP.

The database will use PostgreSQL to provide persistent storage for lead records.

## 2. Database Technology

- **Database:** PostgreSQL
- **Purpose:** Persistent lead storage
- **Data Model:** Relational
- **Primary Identifier:** UUID

## 3. Initial Database Schema

### 3.1 Leads Table

The `leads` table stores incoming lead information.

| Column | Data Type | Description |
|---|---|---|
| id | UUID | Primary key |
| full_name | VARCHAR(150) | Lead's full name |
| email | VARCHAR(254) | Lead's email address |
| phone | VARCHAR(30) | Optional phone number |
| source | VARCHAR(100) | Lead acquisition source |
| status | VARCHAR(30) | Lead processing status |
| created_at | TIMESTAMPTZ | Record creation timestamp |
| updated_at | TIMESTAMPTZ | Last modification timestamp |

## 4. Constraints

The database should enforce:

- A unique primary key for every lead.
- Required fields must not be null.
- Email addresses must follow defined validation rules.
- Lead status must use approved values.
- Duplicate handling must follow defined business rules.
- Timestamps must use consistent timezone-aware formats.

## 5. Lead Status

Initial lead statuses:

- NEW
- QUALIFIED
- UNQUALIFIED
- CONTACTED
- CONVERTED

The MVP will initially use NEW for successfully accepted leads.

Additional statuses may be introduced as functionality expands.

## 6. Data Integrity

- PostgreSQL will serve as the persistent source of truth.
- UUIDs will identify lead records.
- Database constraints will protect record integrity.
- Valid lead submissions will be stored before downstream processing.
- Duplicate submissions will be handled consistently.

## 7. Data Normalization

Before storage, lead information should be normalized.

Examples:

- Trim unnecessary whitespace.
- Normalize email addresses to lowercase.
- Normalize empty optional values.
- Apply consistent phone number formatting where possible.

## 8. Future Database Extensions

Future versions may introduce:

- lead_activities
- qualifications
- assignments
- followups
- deals
- workflow_executions
- error_records

These tables are not part of the initial MVP schema.

## 9. Security Considerations

- Database credentials must not be committed to GitHub.
- Database access should use dedicated credentials.
- Access permissions should follow least privilege.
- Production database access should be restricted.
- Sensitive data should not appear unnecessarily in logs.

## 10. Current Status

Database design is documented.

The actual PostgreSQL schema has not yet been implemented.

---

Ascendor — RISE BEYOND.
