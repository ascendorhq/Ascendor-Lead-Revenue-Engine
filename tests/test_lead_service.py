
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

    def test_missing_name(self):
        lead = {
            "name": "",
            "email": "john@example.com",
        }

        valid, message = LeadService.validate_lead(lead)

        self.assertFalse(valid)
        self.assertEqual(message, "Name is required")

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

    def test_normalize_email(self):
        email = "  JOHN@EXAMPLE.COM  "

        normalized = LeadService.normalize_email(email)

        self.assertEqual(normalized, "john@example.com")


if __name__ == "__main__":
    unittest.main()
