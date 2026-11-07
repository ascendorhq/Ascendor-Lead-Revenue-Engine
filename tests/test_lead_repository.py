
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
        mock_connection.__enter__.return_value = mock_connection

        mock_cursor = (
            mock_connection.cursor.return_value.__enter__.return_value
        )

        mock_cursor.fetchone.return_value = {
            "id": "test-uuid",
            "full_name": "John Doe",
            "email": "john@example.com",
            "created_at": None,
        }

        lead_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+639123456789",
            "company": "Example Corporation",
            "source": "website",
        }

        result = LeadRepository.create_lead(lead_data)

        self.assertEqual(result["full_name"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")

        mock_cursor.execute.assert_called_once()

        executed_sql, executed_values = (
            mock_cursor.execute.call_args.args
        )

        self.assertIn("INSERT INTO leads", executed_sql)

        self.assertEqual(
            executed_values,
            (
                "John Doe",
                "john@example.com",
                "+639123456789",
                "Example Corporation",
                "website",
            ),
        )

        mock_connection.close.assert_called_once()

    @patch("app.repositories.lead_repository.get_connection")
    def test_create_lead_closes_connection_on_error(
        self,
        mock_get_connection,
    ):
        mock_connection = mock_get_connection.return_value
        mock_connection.__enter__.return_value = mock_connection

        mock_cursor = (
            mock_connection.cursor.return_value.__enter__.return_value
        )

        mock_cursor.execute.side_effect = RuntimeError(
            "Simulated database error"
        )

        lead_data = {
            "name": "John Doe",
            "email": "john@example.com",
        }

        with self.assertRaises(RuntimeError):
            LeadRepository.create_lead(lead_data)

        mock_connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
