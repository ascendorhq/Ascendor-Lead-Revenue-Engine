ASCENDOR MVP — TEST CASES

1. Lead Intake

ID| Test| Expected Result
TC-001| Submit valid lead| Lead accepted
TC-002| Missing full name| Request rejected
TC-003| Missing email| Request rejected
TC-004| Invalid email format| Request rejected
TC-005| Empty request payload| Request rejected
TC-006| Email with uppercase letters| Email normalized to lowercase

2. Duplicate Detection

ID| Test| Expected Result
TC-007| Submit same email twice| Duplicate detected
TC-008| Submit same email with different casing| Duplicate detected
TC-009| Submit different email| New lead accepted

3. Database

ID| Test| Expected Result
TC-010| Save valid lead| Lead stored
TC-011| Update lead| updated_at changes
TC-012| Invalid lead score| Database rejects
TC-013| Negative revenue| Database rejects
TC-014| Duplicate email insert| Database rejects
TC-015| Delete lead| Associated activities and followups deleted

4. Qualification and Scoring

ID| Test| Expected Result
TC-016| Qualified lead| Qualification status updated
TC-017| Unqualified lead| Qualification status updated
TC-018| Score below 0| Rejected
TC-019| Score above 100| Rejected
TC-020| Valid score| Score stored

5. Follow-up System

ID| Test| Expected Result
TC-021| Create follow-up| Follow-up stored
TC-022| Complete follow-up| Status completed
TC-023| Failed follow-up| Error recorded
TC-024| Cancel follow-up| Status cancelled

6. Revenue Tracking

ID| Test| Expected Result
TC-025| Set estimated revenue| Value stored
TC-026| Record actual revenue| Value stored
TC-027| Convert lead| Conversion timestamp recorded
TC-028| Negative revenue| Rejected

7. Webhook

ID| Test| Expected Result
TC-029| Valid webhook request| Success response
TC-030| Invalid webhook request| Error response
TC-031| Duplicate webhook request| Duplicate response
TC-032| Database unavailable| Error handled safely

8. MVP Acceptance Criteria

The MVP is accepted when:

- Valid leads can be received.
- Invalid leads are rejected.
- Duplicate emails are prevented.
- Leads are stored in PostgreSQL.
- Lead scores and qualification can be updated.
- Activities can be recorded.
- Follow-ups can be scheduled and tracked.
- Revenue can be recorded.
- Conversion can be tracked.
- Webhook errors are handled safely.
- Core test cases pass.