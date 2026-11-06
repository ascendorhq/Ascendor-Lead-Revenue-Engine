
"""
Ascendor Lead Repository.

This module handles database operations
for lead records.
"""

from app.database import get_connection


class LeadRepository:
    """Manage lead records in PostgreSQL."""

    @staticmethod
    def create_lead(lead_data):
        """Insert a new lead into the database."""

        sql = """
            INSERT INTO leads (
                name,
                email,
                phone,
                company,
                source
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, name, email, created_at;
        """

        conn = get_connection()

        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        sql,
                        (
                            lead_data["name"],
                            lead_data["email"],
                            lead_data.get("phone"),
                            lead_data.get("company"),
                            lead_data.get("source"),
                        ),
                    )

                    lead = cursor.fetchone()

                    return lead

        finally:
            conn.close()
