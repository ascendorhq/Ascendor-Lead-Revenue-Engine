
"""
Ascendor API routes.
"""

from flask import Blueprint, request
from app.services.lead_service import LeadService

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():
    """Check whether the API is responding."""
    return {
        "service": "Ascendor Lead-to-Revenue Engine",
        "status": "healthy",
        "version": "0.1.0",
    }, 200


@api.route("/api/v1/leads", methods=["POST"])
def create_lead():
    """Receive and validate a new lead."""

    lead_data = request.get_json(silent=True)

    if not isinstance(lead_data, dict):
        return {
            "success": False,
            "message": "Invalid JSON request body",
        }, 400

    valid, message = LeadService.validate_lead(lead_data)

    if not valid:
        return {
            "success": False,
            "message": message,
        }, 400

    lead_data["email"] = LeadService.normalize_email(
        lead_data["email"]
    )

    return {
        "success": False,
        "message": "Validation successful. Database persistence not implemented yet.",
    }, 501
