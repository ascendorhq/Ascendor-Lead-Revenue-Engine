
# ASCENDOR MVP — TEST CASES

## 1. Lead Intake

### TC-001 — Valid Lead Submission
- Input: Complete and valid lead information.
- Expected: Lead is accepted and returns HTTP 201.
- Implementation: Automated API test exists.

### TC-002 — Missing Full Name
- Input: Lead without a full name.
- Expected: Request is rejected with HTTP 400.
- Implementation: Covered by validation logic.

### TC-003 — Missing Email
- Input: Lead without an email address.
- Expected: Request is rejected with HTTP 400.
- Implementation: Covered by validation logic.

### TC-004 — Invalid Email
- Input: Invalid email format.
- Expected: Request is rejected with HTTP 400.
- Implementation: Automated API test exists.

### TC-005 — Empty Payload
- Input: Empty webhook request.
- Expected: Request is rejected with HTTP 400.
- Implementation: Automated API test exists.

### TC-006 — Email Normalization
- Input: Email containing uppercase letters.
- Expected: Email is converted to lowercase.
- Implementation: Automated service test exists.

---

## 2. Duplicate Detection

### TC-007 — Duplicate Email
- Input: Submit the same email twice.
- Expected: Duplicate is detected with HTTP 409.
- Implementation: Automated API test exists.

### TC-008 — Case-Insensitive Duplicate
- Input: Submit the same email using different capitalization.
- Expected: Duplicate is detected.
- Implementation: Supported by email normalization and database uniqueness.

### TC-009 — New Email
- Input: Submit a different email.
- Expected: New lead is accepted.
- Implementation: Supported by lead creation.

---

## 3. Database Integrity

### TC-010 — Save Lead
- Input: Valid lead information.
- Expected: Lead is stored in PostgreSQL.
- Implementation: Repository code and mocked unit test exist.

### TC-011 — Update Timestamp
- Input: Update an existing lead.
- Expected: updated_at changes automatically.
- Implementation: Future feature / database verification.

### TC-012 — Invalid Lead Score
- Input: Lead score below 0.
- Expected: Database rejects the value.
- Implementation: Database constraint verification required.

### TC-013 — Negative Revenue
- Input: Negative estimated revenue.
- Expected: Database rejects the value.
- Implementation: Database constraint verification required.

### TC-014 — Duplicate Email Insertion
- Input: Insert an existing email.
- Expected: Database rejects the duplicate.
- Implementation: Database verification required.

### TC-015 — Delete Lead
- Input: Delete an existing lead.
- Expected: Associated activities and follow-ups are deleted.
- Implementation: Future feature.

---

## 4. Lead Qualification and Scoring

### TC-016 — Qualify Lead
- Input: Qualified lead.
- Expected: Qualification status becomes QUALIFIED.
- Implementation: Future feature.

### TC-017 — Disqualify Lead
- Input: Unqualified lead.
- Expected: Qualification status becomes UNQUALIFIED.
- Implementation: Future feature.

### TC-018 — Score Below Minimum
- Input: Score below 0.
- Expected: Database rejects the value.
- Implementation: Database constraint verification required.

### TC-019 — Score Above Maximum
- Input: Score above 100.
- Expected: Database rejects the value.
- Implementation: Database constraint verification required.

### TC-020 — Valid Score
- Input: Score between 0 and 100.
- Expected: Score is successfully stored.
- Implementation: Future feature.

---

## 5. Follow-up Management

### TC-021 — Create Follow-up
- Input: Schedule a follow-up.
- Expected: Follow-up is stored.
- Implementation: Future feature.

### TC-022 — Complete Follow-up
- Input: Complete a scheduled follow-up.
- Expected: Status becomes COMPLETED.
- Implementation: Future feature.

### TC-023 — Failed Follow-up
- Input: Follow-up execution fails.
- Expected: Error is recorded.
- Implementation: Future feature.

### TC-024 — Cancel Follow-up
- Input: Cancel a scheduled follow-up.
- Expected: Status becomes CANCELLED.
- Implementation: Future feature.

---

## 6. Revenue Tracking

### TC-025 — Estimated Revenue
- Input: Set estimated revenue.
- Expected: Estimated revenue is stored.
- Implementation: Future feature.

### TC-026 — Actual Revenue
- Input: Record actual revenue.
- Expected: Actual revenue is stored.
- Implementation: Future feature.

### TC-027 — Lead Conversion
- Input: Convert a lead into a customer.
- Expected: Conversion timestamp is recorded.
- Implementation: Future feature.

### TC-028 — Negative Revenue
- Input: Negative revenue amount.
- Expected: Database rejects the value.
- Implementation: Database constraint verification required.

---

## 7. Webhook Processing

### TC-029 — Valid Webhook
- Input: Valid webhook request.
- Expected: Success response is returned.
- Implementation: API endpoint exists.

### TC-030 — Invalid Webhook
- Input: Invalid webhook request.
- Expected: Error response is returned.
- Implementation: Automated API tests exist.

### TC-031 — Duplicate Webhook
- Input: Duplicate lead submission.
- Expected: Duplicate response is returned.
- Implementation: Duplicate handling exists.

### TC-032 — Database Failure
- Input: Database unavailable.
- Expected: Error is handled safely with HTTP 500.
- Implementation: Automated API test exists.

---

## 8. MVP Acceptance Criteria

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

## 9. Test Execution Status

**Current Status: NOT RUN**

Tests have been prepared but have not yet been executed.

- NOT RUN — Test has not been executed.
- PASS — Test passed.
- FAIL — Test failed.

Testing will begin after the development environment is available.

Execution environment:
- Docker
- PostgreSQL
- Ascendor Flask API

Test execution date: Not yet recorded.
