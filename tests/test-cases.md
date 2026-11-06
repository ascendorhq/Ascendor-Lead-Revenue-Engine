Ascendor MVP — Test Cases

1. Lead Intake

Test ID| Test Scenario| Expected Result
TC-001| Submit valid lead| Lead accepted
TC-002| Missing full name| Request rejected
TC-003| Missing email| Request rejected
TC-004| Invalid email format| Request rejected
TC-005| Empty request payload| Request rejected
TC-006| Email with uppercase letters| Email normalized to lowercase

2. Duplicate Detection

Test ID| Test Scenario| Expected Result
TC-007| Submit same email twice| Duplicate detected
TC-008| Submit same email with different casing| Duplicate detected
TC-009| Submit different email| New lead accepted

3. Database Integrity

Test ID| Test Scenario| Expected Result
TC-010| Save valid lead| Lead stored in PostgreSQL
TC-011| Update lead| "updated_at" changes automatically
TC-012| Lead score below 0| Database rejects
TC-013| Negative estimated revenue| Database rejects
TC-014| Duplicate email insertion| Database rejects
TC-015| Delete lead| Associated activities and follow-ups deleted

4. Lead Qualification and Scoring

Test ID| Test Scenario| Expected Result
TC-016| Qualify a lead| Qualification status updated
TC-017| Disqualify a lead| Qualification status updated
TC-018| Score below 0| Database rejects
TC-019| Score above 100| Database rejects
TC-020| Valid lead score| Score successfully stored

5. Follow-up Management

Test ID| Test Scenario| Expected Result
TC-021| Create follow-up| Follow-up stored
TC-022| Complete follow-up| Status becomes "COMPLETED"
TC-023| Failed follow-up| Error recorded
TC-024| Cancel follow-up| Status becomes "CANCELLED"

6. Revenue Tracking

Test ID| Test Scenario| Expected Result
TC-025| Set estimated revenue| Estimated revenue stored
TC-026| Record actual revenue| Actual revenue stored
TC-027| Convert lead| Conversion timestamp recorded
TC-028| Negative revenue| Database rejects

7. Webhook Processing

Test ID| Test Scenario| Expected Result
TC-029| Submit valid webhook request| Success response returned
TC-030| Submit invalid webhook request| Error response returned
TC-031| Submit duplicate webhook request| Duplicate response returned
TC-032| Database unavailable| Error handled safely

8. MVP Acceptance Criteria

The MVP is considered successful when:

- [ ] Valid leads can be received.
- [ ] Invalid leads are rejected.
- [ ] Duplicate emails are prevented.
- [ ] Leads are stored in PostgreSQL.
- [ ] Lead qualification and scoring work correctly.
- [ ] Lead activities can be recorded.
- [ ] Follow-ups can be scheduled and tracked.
- [ ] Revenue can be recorded.
- [ ] Lead conversions can be tracked.
- [ ] Webhook errors are handled safely.
- [ ] All applicable MVP test cases pass.

9. Test Execution Status

Test ID| Status| Notes
TC-001–TC-032| NOT RUN| Pending MVP implementation

Status Legend:

- "NOT RUN" — Test has not been executed.
- "PASS" — Test passed successfully.
- "FAIL" — Test failed and requires investigation.