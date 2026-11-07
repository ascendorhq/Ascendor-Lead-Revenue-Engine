
"""
Ascendor Lead Processing Service.
"""

import re


class LeadService:
    """Handle lead processing operations."""

    EMAIL_PATTERN = re.compile(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )

    @staticmethod
    def validate_lead(lead_data):
        """Validate required and optional lead information."""

        if not isinstance(lead_data, dict):
            return False, "Invalid lead data"

        name = lead_data.get("name")
        email = lead_data.get("email")

        if not isinstance(name, str) or not name.strip():
            return False, "Name is required"

        if len(name.strip()) > 150:
            return False, "Name must not exceed 150 characters"

        if not isinstance(email, str) or not email.strip():
            return False, "Email is required"

        email = email.strip()

        if len(email) > 254:
            return False, "Email must not exceed 254 characters"

        if not LeadService.EMAIL_PATTERN.match(email):
            return False, "Invalid email address"

        optional_fields = {
            "phone": 30,
            "company": 150,
            "source": 100,
        }

        for field, max_length in optional_fields.items():
            value = lead_data.get(field)

            if value is not None:
                if not isinstance(value, str):
                    return False, f"{field} must be a string"

                if len(value.strip()) > max_length:
                    return False, (
                        f"{field} must not exceed "
                        f"{max_length} characters"
                    )

        return True, "Lead data is valid"

    @staticmethod
    def normalize_email(email):
        """Normalize an email address."""

        if not isinstance(email, str):
            return None

        return email.strip().lower()
