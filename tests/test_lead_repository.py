
"""
Tests for Ascendor Lead Repository.
"""

import unittest
from unittest.mock import patch

from app.repositories.lead_repository import LeadRepository


class TestLeadRepository(unittest.TestCase):
    """Test lead database operations."""

    @patch("app.repositories.lead_repository.get_connection")
    def test_create_lead(self, mock_get_connection):
        mock_connection = mock_get_connection.return_value
        mock_cursor = mock_connection.cursor.return_value.__enter__.return_value

        mock_cursor.fetchone.return_value = {
            "id": "test-uuid",
            "name": "John Doe",
            "email": "john@example.com",
            "created_at": None,
        }

        lead_data = {
            "name": "John Doe",
            "email": "john@example.com",
        }

        result = LeadRepository.create_lead(lead_data)

        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")

        mock_cursor.execute.assert_called_once()
        mock_connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
