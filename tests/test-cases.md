ASCENDOR MVP — TEST CASES

1. Lead Intake

TC-001 — Valid Lead Submission

- Input: Complete and valid lead information.
- Expected: Lead is accepted.

TC-002 — Missing Full Name

- Input: Lead without a full name.
- Expected: Request is rejected.

TC-003 — Missing Email

- Input: Lead without an email address.
- Expected: Request is rejected.

TC-004 — Invalid Email

- Input: Invalid email format.
- Expected: Request is rejected.

TC-005 — Empty Payload

- Input: Empty webhook request.
- Expected: Request is rejected.

TC-006 — Email Normalization

- Input: Email containing uppercase letters.
- Expected: Email is converted to lowercase.

---

2. Duplicate Detection

TC-007 — Duplicate Email

- Input: Submit the same email twice.
- Expected: Duplicate is detected.

TC-008 — Case-Insensitive Duplicate

- Input: Submit the same email using different capitalization.
- Expected: Duplicate is detected.

TC-009 — New Email

- Input: Submit a different email.
- Expected: New lead is accepted.

---

3. Database Integrity

TC-010 — Save Lead

- Input: Valid lead information.
- Expected: Lead is stored in PostgreSQL.

TC-011 — Update Timestamp

- Input: Update an existing lead.
- Expected: "updated_at" changes automatically.

TC-012 — Invalid Lead Score

- Input: Lead score below 0.
- Expected: Database rejects the value.

TC-013 — Negative Revenue

- Input: Negative estimated revenue.
- Expected: Database rejects the value.

TC-014 — Duplicate Email Insertion

- Input: Insert an existing email.
- Expected: Database rejects the duplicate.

TC-015 — Delete Lead

- Input: Delete an existing lead.
- Expected: Associated activities and follow-ups are deleted.

---

4. Lead Qualification and Scoring

TC-016 — Qualify Lead

- Input: Qualified lead.
- Expected: Qualification status becomes "QUALIFIED".

TC-017 — Disqualify Lead

- Input: Unqualified lead.
- Expected: Qualification status becomes "UNQUALIFIED".

TC-018 — Score Below Minimum

- Input: Score below 0.
- Expected: Database rejects the value.

TC-019 — Score Above Maximum

- Input: Score above 100.
- Expected: Database rejects the value.

TC-020 — Valid Score

- Input: Score between 0 and 100.
- Expected: Score is successfully stored.

---

5. Follow-up Management

TC-021 — Create Follow-up

- Input: Schedule a follow-up.
- Expected: Follow-up is stored.

TC-022 — Complete Follow-up

- Input: Complete a scheduled follow-up.
- Expected: Status becomes "COMPLETED".

TC-023 — Failed Follow-up

- Input: Follow-up execution fails.
- Expected: Error is recorded.

TC-024 — Cancel Follow-up

- Input: Cancel a scheduled follow-up.
- Expected: Status becomes "CANCELLED".

---

6. Revenue Tracking

TC-025 — Estimated Revenue

- Input: Set estimated revenue.
- Expected: Estimated revenue is stored.

TC-026 — Actual Revenue

- Input: Record actual revenue.
- Expected: Actual revenue is stored.

TC-027 — Lead Conversion

- Input: Convert a lead into a customer.
- Expected: Conversion timestamp is recorded.

TC-028 — Negative Revenue

- Input: Negative revenue amount.
- Expected: Database rejects the value.

---

7. Webhook Processing

TC-029 — Valid Webhook

- Input: Valid webhook request.
- Expected: Success response is returned.

TC-030 — Invalid Webhook

- Input: Invalid webhook request.
- Expected: Error response is returned.

TC-031 — Duplicate Webhook

- Input: Duplicate lead submission.
- Expected: Duplicate response is returned.

TC-032 — Database Failure

- Input: Database unavailable.
- Expected: Error is handled safely.

---

8. MVP Acceptance Criteria

The MVP is considered successful when:

- [ ] Lead intake works.
- [ ] Invalid leads are rejected.
- [ ] Duplicate leads are prevented.
- [ ] PostgreSQL stores lead information.
- [ ] Lead qualification works.
- [ ] Lead scoring works.
- [ ] Activity history is recorded.
- [ ] Follow-ups can be scheduled and tracked.
- [ ] Revenue can be recorded.
- [ ] Lead conversion can be tracked.
- [ ] Webhook errors are handled safely.
- [ ] All applicable test cases pass.

---

9. Test Execution Status

Current Status: NOT RUN

Testing will begin after MVP implementation.

- "NOT RUN" — Not yet tested.
- "PASS" — Test passed.
- "FAIL" — Test failed.