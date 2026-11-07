
# Ascendor System Architecture

## 1. Overview

Ascendor is designed as a modular lead management and business automation system.

The initial MVP establishes a reliable lead intake, validation, and storage process using Python Flask, PostgreSQL, Docker, and n8n.

The architecture separates API processing, database operations, and workflow automation to support maintainability and future expansion.

## 2. MVP Architecture

### Current Application Architecture

```text
Lead Source
    |
    v
HTTP POST Request
    |
    v
Ascendor Flask API
    |
    v
Input Validation
    |
    v
Email Normalization
    |
    v
Lead Repository
    |
    v
PostgreSQL Database
    |
    v
API Response
```

### Development Environment Architecture

```text
Docker Environment
|
|-- Ascendor Flask API
|   |-- Application Entry Point
|   |-- API Routes
|   |-- Lead Processing Service
|   |-- Lead Repository
|   |-- Database Connection
|
|-- PostgreSQL
|   |-- Lead Records
|   |-- Lead Activities
|   |-- Follow-ups
|
|-- n8n
    |-- Workflow Automation Platform
    |-- Future Lead Automation Workflows
```

## 3. Components

### Lead Source

A website form, external application, or test client submits lead information through an HTTP request.

### Ascendor Flask API

The Flask API receives incoming requests and exposes endpoints for lead management.

Current endpoint:

- `GET /health` — API health check
- `POST /api/v1/leads` — Lead creation endpoint

### Lead Processing Service

The lead processing service validates incoming lead information and normalizes email addresses before database operations.

Responsibilities include:

- Required field validation
- Email format validation
- Optional field validation
- Input length restrictions
- Email normalization

### Lead Repository

The repository manages database operations for lead records.

Responsibilities include:

- Creating lead records
- Executing database queries
- Returning stored lead information
- Managing database connections

### PostgreSQL

PostgreSQL provides persistent storage for Ascendor.

Current database structures include:

- Leads
- Lead activities
- Lead follow-ups

Database constraints enforce data integrity, including email uniqueness, lead score limits, and revenue validation.

### n8n

n8n serves as the workflow automation platform.

Future workflows will integrate lead processing with external business applications and automated sales processes.

### Docker

Docker provides a containerized development environment for the application, database, and automation platform.

Docker Compose manages service configuration, networking, and persistent storage.

## 4. Lead Processing Data Flow

1. A client submits lead information to the Ascendor API.
2. Flask receives the HTTP request.
3. The API validates the JSON request body.
4. The lead processing service validates required and optional fields.
5. The email address is normalized.
6. The lead repository executes the database insertion.
7. PostgreSQL enforces database constraints and stores the lead.
8. The API returns an appropriate HTTP response.
9. Errors are handled and logged when database operations fail.

## 5. API Error Handling

The API should handle:

- Invalid JSON requests
- Missing required fields
- Invalid email formats
- Invalid optional field values
- Duplicate email submissions
- Database connection failures
- Database constraint violations
- Unexpected application errors

Expected errors should return appropriate HTTP status codes and meaningful responses.

Unexpected database errors should be logged without exposing sensitive database information to clients.

## 6. Data Persistence

PostgreSQL serves as the persistent source of truth for lead records.

Lead information must not depend exclusively on temporary API requests or workflow execution history.

The database schema includes:

- UUID-based lead identification
- Email normalization
- Duplicate email prevention
- Lead status and qualification fields
- Lead scoring fields
- Revenue tracking fields
- Automatic timestamps
- Activity history
- Follow-up records

## 7. Security and Reliability

The system is designed around the following security and reliability principles:

- Environment-based configuration
- Separation of application and database responsibilities
- Restricted database exposure during development
- Persistent database volumes
- Input validation
- Database constraints
- Error logging
- Secure secret management
- Incremental testing and verification

Production deployment will require additional security controls, monitoring, backups, and operational hardening.

## 8. Future Architecture Extensions

Future versions may introduce:

- n8n lead intake workflows
- AI qualification services
- Automated lead scoring
- CRM integrations
- Email automation
- Appointment scheduling
- Sales notifications
- Reporting dashboards
- Monitoring and alerting
- Cloud deployment
- Queue-based processing
- Infrastructure automation

These components will be implemented incrementally and are not yet part of the verified MVP functionality.

## 9. Architecture Principles

- Modular application design
- Reliable data persistence
- Separation of responsibilities
- Secure configuration
- Explicit error handling
- Maintainable components
- Incremental implementation
- Documented system behavior
- Testing before deployment

## 10. Current Status

- **Architecture:** Documented
- **Application Foundation:** Prepared
- **Database Schema:** Prepared
- **Docker Configuration:** Prepared
- **Runtime Verification:** Pending
- **Automation Workflows:** Not yet implemented
- **Cloud Deployment:** Not yet implemented
- **Production Readiness:** Not yet achieved

This document describes the intended MVP architecture and prepared application components. It does not represent an already deployed or production-verified system.

---

**Ascendor — RISE BEYOND.**
