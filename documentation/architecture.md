
# Ascendor System Architecture

## 1. Overview

Ascendor is designed as a modular lead management and business automation system.

The initial MVP will establish a reliable lead intake and storage process using n8n and PostgreSQL.

## 2. MVP Architecture

```text
Lead Source
    |
    v
HTTP Request
    |
    v
n8n Webhook
    |
    v
Input Validation
    |
    v
Duplicate Detection
    |
    v
PostgreSQL Database
    |
    v
Webhook Response
    |
    v
Execution Logging
```

## 3. Components

### Lead Source

A website form or test client submits lead information.

### n8n Webhook

Receives incoming HTTP requests and starts the workflow.

### Input Validation

Checks required fields, data formats, and invalid submissions.

### Duplicate Detection

Identifies repeated submissions using defined matching rules.

### PostgreSQL

Stores validated lead records for persistent data management.

### Webhook Response

Returns an appropriate response to the submitting client.

### Execution Logging

Records workflow execution information and errors for troubleshooting.

## 4. Data Flow

1. A client submits lead information.
2. The webhook receives the request.
3. The workflow validates the submitted data.
4. Duplicate detection checks existing records.
5. Valid leads are stored in PostgreSQL.
6. The workflow returns a response.
7. Execution information is available for troubleshooting.

## 5. Error Handling

The MVP should account for:

- Missing required fields
- Invalid data formats
- Duplicate submissions
- Database connection failures
- Database constraint violations
- Workflow execution failures

Errors should be handled without silently losing valid lead submissions.

## 6. Data Persistence

PostgreSQL will serve as the persistent source of truth for lead records.

Lead data should not depend exclusively on temporary workflow execution history.

## 7. Future Architecture Extensions

Future versions may introduce:

- AI qualification services
- CRM integrations
- Email automation
- Appointment scheduling
- Sales notifications
- Reporting dashboards
- Monitoring and alerting
- Cloud deployment
- Queue-based processing

These components are outside the initial MVP implementation scope.

## 8. Architecture Principles

- Modular workflow design
- Reliable data persistence
- Secure communication
- Explicit error handling
- Maintainable components
- Incremental implementation
- Documented system behavior

## 9. Current Status

Architecture documentation is being established.

The architecture describes the intended MVP design and does not represent an already deployed system.

---

**Ascendor — RISE BEYOND.**
