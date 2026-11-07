
# Ascendor Database Design

## 1. Purpose

This document defines the database structure and data integrity rules for the Ascendor Lead-to-Revenue Automation Engine MVP.

PostgreSQL provides persistent storage for lead records, activity history, and follow-up management.

The database design supports reliable lead processing and future business automation capabilities.

## 2. Database Technology

- **Database:** PostgreSQL 17
- **Purpose:** Persistent data storage
- **Data Model:** Relational
- **Primary Identifier:** UUID
- **Database Schema:** `database/schema.sql`

## 3. Database Tables

### 3.1 Leads Table

The `leads` table stores incoming lead information and sales-related data.

| Column | Data Type | Description |
|---|---|---|
| id | UUID | Primary key |
| full_name | VARCHAR(150) | Lead's full name |
| email | VARCHAR(254) | Lead's email address |
| phone | VARCHAR(30) | Optional phone number |
| company_name | VARCHAR(150) | Optional company name |
| source | VARCHAR(100) | Lead acquisition source |
| status | VARCHAR(30) | Lead processing status |
| qualification_status | VARCHAR(30) | Lead qualification state |
| lead_score | INTEGER | Lead score from 0 to 100 |
| estimated_revenue | NUMERIC(12,2) | Optional estimated revenue |
| actual_revenue | NUMERIC(12,2) | Optional actual revenue |
| converted_at | TIMESTAMPTZ | Lead conversion timestamp |
| created_at | TIMESTAMPTZ | Record creation timestamp |
| updated_at | TIMESTAMPTZ | Last modification timestamp |

### 3.2 Lead Activities Table

The `lead_activities` table records activity history associated with leads.

| Column | Data Type | Description |
|---|---|---|
| id | UUID | Primary key |
| lead_id | UUID | Associated lead |
| activity_type | VARCHAR(50) | Activity category |
| description | TEXT | Activity description |
| metadata | JSONB | Additional activity information |
| created_at | TIMESTAMPTZ | Activity timestamp |

### 3.3 Lead Follow-ups Table

The `lead_followups` table stores scheduled follow-up records.

| Column | Data Type | Description |
|---|---|---|
| id | UUID | Primary key |
| lead_id | UUID | Associated lead |
| followup_type | VARCHAR(50) | Follow-up category |
| scheduled_at | TIMESTAMPTZ | Scheduled execution time |
| completed_at | TIMESTAMPTZ | Completion timestamp |
| status | VARCHAR(30) | Follow-up status |
| attempts | INTEGER | Execution attempt count |
| last_error | TEXT | Last execution error |
| created_at | TIMESTAMPTZ | Record creation timestamp |

## 4. Relationships

The database uses foreign keys to maintain relationships between records.

```text
leads
  |
  |-- lead_activities
  |
  |-- lead_followups
```

- One lead can have multiple activity records.
- One lead can have multiple follow-up records.
- Activity records reference their associated lead.
- Follow-up records reference their associated lead.
- Deleting a lead automatically deletes its associated activities and follow-ups.

## 5. Constraints and Data Integrity

The database enforces the following constraints:

- UUID primary keys for record identification.
- Required lead fields must not be null.
- Email addresses are normalized to lowercase.
- Email addresses must be unique.
- Lead statuses must use approved values.
- Qualification statuses must use approved values.
- Lead scores must remain between 0 and 100.
- Revenue values must not be negative.
- Converted leads must have a conversion timestamp.
- Follow-up statuses must use approved values.
- Follow-up attempts must not be negative.
- Foreign keys maintain valid lead relationships.

## 6. Lead Status

Initial lead statuses:

- NEW
- QUALIFIED
- UNQUALIFIED
- CONTACTED
- CONVERTED
- LOST

The default status for newly created leads is `NEW`.

## 7. Qualification Status

Initial qualification statuses:

- PENDING
- QUALIFIED
- UNQUALIFIED

New leads default to `PENDING`.

## 8. Follow-up Status

Initial follow-up statuses:

- PENDING
- PROCESSING
- COMPLETED
- FAILED
- CANCELLED

New follow-ups default to `PENDING`.

## 9. Data Normalization

The current implementation normalizes email addresses before database insertion.

Database triggers also normalize email addresses to lowercase and trim surrounding whitespace.

Additional normalization may be introduced for:

- Lead names
- Phone numbers
- Company names
- Optional field values

Normalization rules will be implemented incrementally as requirements evolve.

## 10. Indexes and Performance

The schema includes indexes to support common database operations.

Current indexes include:

- Unique email index
- Lead status index
- Lead creation timestamp index
- Lead score index
- Lead activity relationship index
- Lead activity timestamp index
- Follow-up scheduling index
- Follow-up relationship index

These indexes support lead retrieval, filtering, and follow-up processing.

## 11. Security Considerations

- Database credentials must not be committed to GitHub.
- Database access should use dedicated credentials.
- Access permissions should follow least privilege.
- Production database access should be restricted.
- Sensitive information should not appear unnecessarily in logs.
- Database backups should be protected.

## 12. Current Status

- **Database Design:** Documented
- **PostgreSQL Schema:** Prepared
- **Leads Table:** Defined
- **Lead Activities Table:** Defined
- **Lead Follow-ups Table:** Defined
- **Database Constraints:** Defined
- **Indexes:** Defined
- **Runtime Verification:** Pending
- **Database Operations:** Not yet verified against a running PostgreSQL instance

The database schema is defined in `database/schema.sql`.

The database has not yet been executed or verified in the development environment.

---

**Ascendor — RISE BEYOND.**
