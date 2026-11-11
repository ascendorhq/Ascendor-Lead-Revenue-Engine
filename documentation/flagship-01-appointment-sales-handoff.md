
# Ascendor Flagship 01 — Appointment & Sales Handoff

## 1. Document Overview

**Project:** Ascendor AI Lead Generation & Revenue Engine  
**Module:** Appointment & Sales Handoff  
**Architecture Version:** 1.0  
**Status:** Architecture Specification

This document defines the appointment scheduling and sales handoff architecture for Ascendor Flagship 01.

The module connects qualified leads with sales representatives through appointment scheduling, notifications, assignment, and structured sales handoff.

Its purpose is to ensure that qualified opportunities move efficiently from automated lead processing into human sales engagement.

The module must satisfy Ascendor's four Architecture Quality Requirements:

1. Reliable
2. Scalable
3. Premium / Aesthetic
4. Simple / Usable

---

## 2. Business Objectives

The Appointment & Sales Handoff module must:

- Convert qualified leads into scheduled sales appointments.
- Reduce manual appointment coordination.
- Prevent appointment scheduling conflicts.
- Notify sales representatives about new opportunities.
- Provide sales representatives with sufficient lead context.
- Maintain appointment history and status.
- Support organization-specific appointment management.
- Improve speed and consistency of sales engagement.

---

## 3. System Architecture

### 3.1 Appointment & Sales Handoff Flow

```text
Qualified Lead
      |
      v
Appointment Request
      |
      v
Availability Validation
      |
      v
Appointment Scheduling
      |
      v
Appointment Record Creation
      |
      v
Sales Representative Assignment
      |
      v
Sales Notification
      |
      v
Appointment Confirmation
      |
      v
Sales Handoff
      |
      v
Appointment Management
```

### 3.2 Technology Stack

| Component | Technology |
|---|---|
| Dashboard | Next.js |
| Application Language | TypeScript |
| UI Styling | Tailwind CSS |
| Database | Supabase PostgreSQL |
| Authentication | Supabase Auth |
| Database Security | Row Level Security |
| Automation | n8n |
| Calendar Integration | External Calendar APIs |
| Notifications | Email / Supported Messaging Services |

---

## 4. Appointment Management

### 4.1 Appointment Creation

Appointments may be created through:

- Lead booking interfaces.
- Client dashboard actions.
- Sales representative scheduling.
- Automated booking workflows.
- Approved external calendar integrations.

Each appointment must be associated with the correct organization and lead.

### 4.2 Appointment Data

An appointment should contain:

- Appointment ID
- Organization ID
- Lead ID
- Appointment title
- Scheduled date and time
- Duration
- Assigned sales representative
- Appointment status
- Meeting location or meeting link
- Notes
- Created timestamp
- Updated timestamp

### 4.3 Appointment Status

The appointment lifecycle may include:

| Status | Description |
|---|---|
| Scheduled | Appointment has been confirmed |
| Pending | Appointment requires confirmation |
| Completed | Appointment has occurred |
| Cancelled | Appointment was cancelled |
| Rescheduled | Appointment time has changed |
| No-Show | Expected participant did not attend |

Status transitions must follow defined business rules.

---

## 5. Appointment Scheduling Logic

### 5.1 Scheduling Requirements

The scheduling system must:

- Validate appointment date and time.
- Validate appointment duration.
- Check availability where calendar integration supports it.
- Prevent conflicting appointments where required.
- Associate appointments with the correct lead.
- Assign an authorized sales representative.
- Record appointment details.
- Trigger confirmation and notification workflows.

### 5.2 Availability Validation

Before confirming an appointment:

1. Validate the requested time.
2. Validate the appointment duration.
3. Check the representative's availability.
4. Check connected calendar availability where applicable.
5. Confirm that the requested time is available.
6. Create the appointment.
7. Trigger confirmation notifications.

Availability checks must not be treated as guaranteed reservations unless the underlying calendar provider supports reliable booking confirmation.

### 5.3 Timezone Handling

Appointments must support timezone-aware scheduling.

Requirements:

- Store timestamps consistently using UTC.
- Display appointments in the user's configured timezone.
- Preserve the intended timezone when scheduling.
- Avoid incorrect date or time conversions.
- Clearly communicate appointment time to participants.

---

## 6. Sales Representative Assignment

### 6.1 Assignment Methods

Appointments may be assigned through:

- Manual assignment.
- Lead owner assignment.
- Organization-defined assignment rules.
- Automated assignment based on availability.
- Future workload-based assignment.

### 6.2 Assignment Requirements

The system must:

- Validate that the assigned user belongs to the organization.
- Validate that the assigned user has appropriate permissions.
- Prevent unauthorized cross-organization assignment.
- Maintain assignment history where required.
- Support reassignment by authorized users.

### 6.3 Assignment Rules

Assignment logic may consider:

- Lead ownership.
- Sales representative availability.
- Organization preferences.
- Sales specialization.
- Lead priority.
- Workload distribution.

Advanced assignment algorithms may be introduced as future enhancements.

---

## 7. Sales Handoff

### 7.1 Handoff Objective

The sales handoff transfers a qualified opportunity from automated lead processing to human sales engagement.

The assigned sales representative must receive sufficient context to understand the lead and continue the sales process.

### 7.2 Handoff Information

The sales representative should receive:

- Lead name
- Contact information
- Company information
- Lead source
- Lead score
- Qualification status
- Budget information where available
- Customer intent
- Customer urgency
- Customer requirements
- Previous interactions
- Appointment details
- AI-generated lead summary
- Recommended next action

### 7.3 Handoff Workflow

```text
Qualified Lead
      |
      v
Lead Prioritization
      |
      v
Sales Assignment
      |
      v
Lead Context Preparation
      |
      v
Appointment Confirmation
      |
      v
Sales Notification
      |
      v
Sales Representative Review
      |
      v
Human Sales Engagement
      |
      v
CRM Activity Recording
```

### 7.4 Human Sales Responsibility

AI assists the sales team but does not replace human decision-making.

Sales representatives remain responsible for:

- Reviewing lead information.
- Conducting sales conversations.
- Evaluating customer requirements.
- Negotiating commercial terms.
- Making business decisions.
- Updating sales outcomes.

---

## 8. Notifications & Communication

### 8.1 Notification Events

The system should generate notifications for:

- Appointment creation.
- Appointment confirmation.
- Appointment cancellation.
- Appointment rescheduling.
- Appointment reminders.
- New qualified lead assignment.
- High-priority lead assignment.
- Sales handoff.
- Appointment completion where applicable.

### 8.2 Notification Recipients

Notifications may be sent to:

- Assigned sales representative.
- Organization administrators.
- Lead or customer.
- Other authorized team members.

### 8.3 Notification Channels

Supported notification channels may include:

- Email.
- Calendar invitations.
- In-dashboard notifications.
- Approved messaging integrations.

### 8.4 Notification Requirements

Notifications must:

- Contain accurate appointment information.
- Respect organization settings.
- Avoid unnecessary sensitive information.
- Handle delivery failures.
- Prevent excessive duplicate notifications.
- Provide clear confirmation or failure status.

---

## 9. Appointment Reminders

### 9.1 Reminder Automation

The system may send reminders before appointments.

Example reminder schedule:

- 24 hours before appointment.
- 1 hour before appointment.
- Organization-configured reminder intervals.

Reminder timing must be configurable.

### 9.2 Reminder Requirements

- Respect the appointment timezone.
- Avoid reminders after cancellation.
- Avoid duplicate reminder execution.
- Handle rescheduled appointments correctly.
- Record reminder execution.
- Respect communication preferences.

---

## 10. Appointment Rescheduling & Cancellation

### 10.1 Rescheduling

When an appointment is rescheduled:

1. Validate the new date and time.
2. Check availability.
3. Update the appointment.
4. Update connected calendar events where applicable.
5. Notify affected participants.
6. Update reminder schedules.
7. Record the change.

### 10.2 Cancellation

When an appointment is cancelled:

1. Validate cancellation permission.
2. Update appointment status.
3. Cancel connected calendar events where supported.
4. Stop pending appointment reminders.
5. Notify affected participants.
6. Record the cancellation.

### 10.3 Cancellation Rules

- Unauthorized users cannot cancel appointments.
- Cancelled appointments must not trigger future reminders.
- Appointment history should remain available according to retention policies.
- Calendar synchronization failures must be recorded.

---

## 11. Database Integration

### 11.1 Appointments Table

The appointment module uses the `appointments` table defined in the database architecture.

Conceptual fields:

| Field | Description |
|---|---|
| id | Appointment identifier |
| organization_id | Owning organization |
| lead_id | Related lead |
| title | Appointment title |
| scheduled_at | Scheduled timestamp |
| duration_minutes | Appointment duration |
| status | Appointment status |
| assigned_to | Assigned sales representative |
| created_at | Creation timestamp |
| updated_at | Last update timestamp |

Additional fields may include:

- Meeting link
- Location
- Notes
- Calendar event ID
- Timezone
- Cancellation reason

### 11.2 Database Integrity

The database must enforce:

- Valid organization relationships.
- Valid lead relationships.
- Valid appointment status.
- Valid assigned user membership.
- Appropriate timestamp handling.
- Referential integrity.

An appointment must not reference a lead or sales representative belonging to another organization.

---

## 12. Multi-Tenant Security

### 12.1 Tenant Isolation

Appointments must remain isolated by organization.

Users must only access appointments permitted by their organization membership and role.

### 12.2 Security Requirements

- Every appointment belongs to an organization.
- Appointment queries must enforce tenant isolation.
- RLS policies must restrict unauthorized access.
- Assignment must validate organization membership.
- Calendar integrations must be associated with the correct organization.
- Cross-organization appointment access must be prevented.

### 12.3 Security Acceptance Criteria

- Organization A cannot access Organization B's appointments.
- Organization A cannot modify Organization B's appointments.
- Users cannot assign appointments to unauthorized members.
- Users cannot access unauthorized lead information through appointment records.
- Unauthorized appointment operations are rejected.

---

## 13. n8n Automation Workflows

### 13.1 Appointment Workflow Responsibilities

n8n may handle:

- Appointment confirmation.
- Calendar event creation.
- Appointment reminders.
- Sales notifications.
- Appointment cancellation.
- Appointment rescheduling.
- Sales handoff notifications.
- Appointment-related automation logging.

### 13.2 Workflow Requirements

Each workflow must:

- Validate its input.
- Verify organization context.
- Handle integration failures.
- Prevent duplicate execution where necessary.
- Record execution results.
- Respect appointment status.
- Avoid sending notifications for invalid or cancelled appointments.

### 13.3 Error Handling

When a workflow fails:

- Record the failure.
- Retry transient errors where appropriate.
- Avoid duplicate calendar events.
- Avoid duplicate notifications.
- Notify authorized operators when necessary.
- Preserve appointment data integrity.

---

## 14. Dashboard Integration

### 14.1 Appointment Dashboard

The dashboard should provide a simple interface for managing appointments.

Core capabilities:

- View upcoming appointments.
- View completed appointments.
- View cancelled appointments.
- Create appointments.
- Reschedule appointments.
- Cancel appointments.
- Assign sales representatives.
- View appointment details.
- Access related lead information.

### 14.2 Sales Handoff Interface

The sales handoff interface should display:

- Lead profile.
- Qualification summary.
- Lead score.
- Priority indicator.
- Appointment information.
- Sales activity history.
- Assigned representative.
- Next recommended action.

### 14.3 UX Requirements

The interface must:

- Use clear labels.
- Provide intuitive navigation.
- Display appointment status clearly.
- Prevent accidental destructive actions.
- Provide useful confirmation messages.
- Display understandable error messages.
- Minimize unnecessary steps.

The user must not need technical knowledge of n8n or database operations to manage appointments.

---

## 15. Reliability & Performance

### 15.1 Reliability Requirements

The appointment module must:

- Preserve appointment data integrity.
- Prevent duplicate booking operations where applicable.
- Handle calendar failures safely.
- Handle notification failures independently.
- Maintain appointment history.
- Recover from workflow failures.
- Avoid inconsistent appointment states.

### 15.2 Performance Requirements

The module should support:

- Efficient appointment retrieval.
- Responsive appointment creation.
- Efficient calendar views.
- Appropriate database indexing.
- Scalable notification workflows.
- Increasing organization and appointment volume.

Performance targets must be validated through testing.

---

## 16. Testing Strategy

### 16.1 Functional Testing

Test:

- Appointment creation.
- Appointment confirmation.
- Appointment assignment.
- Appointment rescheduling.
- Appointment cancellation.
- Appointment completion.
- Sales handoff.
- Notification delivery.
- Reminder execution.

### 16.2 Security Testing

Test:

- Unauthorized appointment access.
- Cross-tenant appointment access.
- Unauthorized assignment.
- Unauthorized cancellation.
- Invalid appointment references.
- Invalid organization context.

### 16.3 Integration Testing

Test:

- Supabase appointment records.
- n8n appointment workflows.
- Calendar event creation.
- Calendar event updates.
- Email notifications.
- Reminder scheduling.

### 16.4 Reliability Testing

Test:

- Calendar provider failures.
- Email provider failures.
- Duplicate webhook requests.
- Workflow retry behavior.
- Rescheduled appointment reminders.
- Cancelled appointment reminder suppression.

---

## 17. Acceptance Criteria

The Appointment & Sales Handoff module is considered functionally complete when:

- Appointments can be created successfully.
- Appointments are associated with the correct organization.
- Appointments are associated with the correct lead.
- Authorized sales representatives can be assigned.
- Appointment confirmations work.
- Appointment reminders work.
- Appointment rescheduling works.
- Appointment cancellation works.
- Sales representatives receive appropriate lead context.
- Sales notifications work.
- Appointment history is maintained.
- Tenant isolation is enforced.
- Errors are recorded and handled.
- Dashboard appointment management is usable.

---

## 18. Future Enhancements

Potential future capabilities include:

- Advanced calendar synchronization.
- Automated sales representative assignment.
- AI-assisted meeting preparation.
- AI-generated sales briefing documents.
- Meeting transcription and summaries.
- Sales performance analytics.
- Advanced scheduling optimization.
- Appointment conversion analytics.
- Automated post-meeting follow-up.
- Advanced team availability management.

These enhancements must be prioritized according to actual business requirements.

---

## 19. Architecture Quality Commitment

### Reliable

Appointments must be created, updated, and cancelled predictably, with accurate records and controlled failure handling.

### Scalable

The system must support increasing organizations, appointments, sales representatives, and automation workloads.

### Premium / Aesthetic

Appointment management must provide a polished, professional interface consistent with Ascendor's product identity.

### Simple / Usable

Business owners and sales representatives must be able to schedule, manage, and attend appointments without unnecessary complexity.

---

## 20. Final Architecture Principle

The Appointment & Sales Handoff module transforms qualified opportunities into organized human sales engagement.

It connects automation with real business execution by ensuring that qualified leads are assigned, scheduled, communicated, and managed effectively.

**Automation prepares the opportunity. Human sales converts the opportunity. Ascendor connects both.**
