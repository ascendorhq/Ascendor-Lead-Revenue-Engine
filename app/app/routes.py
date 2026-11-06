
"""
Ascendor API routes.
"""

from flask import Blueprint, request

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
    """Receive a new lead submission."""
    lead_data = request.get_json(silent=True)

    if not isinstance(lead_data, dict):
        return {
            "success": False,
            "message": "Invalid JSON request body",
        }, 400

    return {
        "success": False,
        "message": "Lead processing is not implemented yet",
    }, 501
