
"""
Tests for Ascendor Lead Processing Service.
"""

import unittest

from app.services.lead_service import LeadService


class TestLeadService(unittest.TestCase):
    """Test lead validation and normalization."""

    def test_valid_lead(self):
        lead = {
            "name": "John Doe",
            "email": "john@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertTrue(valid)
        self.assertEqual(message, "Lead data is valid")

    def test_valid_lead_with_optional_fields(self):
        lead = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+639123456789",
            "company": "Example Corporation",
            "source": "website",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertTrue(valid)
        self.assertEqual(message, "Lead data is valid")

    def test_invalid_lead_data_type(self):
        valid, message = LeadService.validate_lead("invalid")

        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lead data")

    def test_missing_name(self):
        lead = {
            "name": "",
            "email": "john@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "Name is required")

    def test_whitespace_name(self):
        lead = {
            "name": "   ",
            "email": "john@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "Name is required")

    def test_name_too_long(self):
        lead = {
            "name": "A" * 151,
            "email": "john@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(
            message,
            "Name must not exceed 150 characters",
        )

    def test_missing_email(self):
        lead = {
            "name": "John Doe",
            "email": "",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "Email is required")

    def test_invalid_email(self):
        lead = {
            "name": "John Doe",
            "email": "invalid-email",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "Invalid email address")

    def test_email_too_long(self):
        lead = {
            "name": "John Doe",
            "email": "a" * 250 + "@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(
            message,
            "Email must not exceed 254 characters",
        )

    def test_optional_field_wrong_type(self):
        lead = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": 123456789,
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "phone must be a string")

    def test_optional_field_too_long(self):
        lead = {
            "name": "John Doe",
            "email": "john@example.com",
            "company": "A" * 151,
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(
            message,
            "company must not exceed 150 characters",
        )

    def test_normalize_email(self):
        email = "  JOHN@EXAMPLE.COM  "

        normalized = LeadService.normalize_email(email)

        self.assertEqual(normalized, "john@example.com")

    def test_normalize_invalid_email_type(self):
        normalized = LeadService.normalize_email(123)

        self.assertIsNone(normalized)


if __name__ == "__main__":
    unittest.main()
