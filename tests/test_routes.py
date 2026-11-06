
"""
Tests for Ascendor API routes.
"""

import unittest
from unittest.mock import patch

from app.main import create_app


class TestLeadRoutes(unittest.TestCase):
    """Test lead API endpoints."""

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_invalid_json(self):
        response = self.client.post(
            "/api/v1/leads",
            data="invalid",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_invalid_lead(self):
        response = self.client.post(
            "/api/v1/leads",
            json={
                "name": "",
                "email": "john@example.com",
            },
        )

        self.assertEqual(response.status_code, 400)

    @patch("app.routes.LeadRepository.create_lead")
    def test_create_lead_success(self, mock_create_lead):
        from datetime import datetime, timezone

        mock_create_lead.return_value = {
            "id": "test-uuid",
            "name": "John Doe",
            "email": "john@example.com",
            "created_at": datetime.now(timezone.utc),
        }

        response = self.client.post(
            "/api/v1/leads",
            json={
                "name": "John Doe",
                "email": "john@example.com",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["success"])
        self.assertEqual(
            response.json["lead"]["email"],
            "john@example.com",
        )


if __name__ == "__main__":
    unittest.main()
