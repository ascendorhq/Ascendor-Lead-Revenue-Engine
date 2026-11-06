
"""
Ascendor Lead Processing Service.
"""

class LeadService:
    """Handle lead processing operations."""

    @staticmethod
    def validate_lead(lead_data):
        """Validate required lead information."""

        if not isinstance(lead_data, dict):
            return False, "Invalid lead data"

        name = lead_data.get("name")
        email = lead_data.get("email")

        if not isinstance(name, str) or not name.strip():
            return False, "Name is required"

        if not isinstance(email, str) or not email.strip():
            return False, "Email is required"

        if "@" not in email:
            return False, "Invalid email address"

        return True, "Lead data is valid"


    @staticmethod
    def normalize_email(email):
        """Normalize an email address."""
        if not isinstance(email, str):
            return None

        return email.strip().lower()

