
"""
Ascendor API routes.
"""

import logging

from flask import Blueprint, request
from psycopg import Error as PsycopgError
from psycopg.errors import UniqueViolation

from app.services.lead_service import LeadService
from app.repositories.lead_repository import LeadRepository


api = Blueprint("api", __name__)

logger = logging.getLogger(__name__)


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
    """Receive, validate, and save a new lead."""

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

    try:
        lead = LeadRepository.create_lead(lead_data)

        return {
            "success": True,
            "message": "Lead created successfully",
            "lead": {
                "id": str(lead["id"]),
                "name": lead["name"],
                "email": lead["email"],
                "created_at": lead["created_at"].isoformat(),
            },
        }, 201

    except UniqueViolation:
        return {
            "success": False,
            "message": "A lead with this email already exists",
        }, 409

    except PsycopgError:
        logger.exception("Database error while creating lead")

        return {
            "success": False,
            "message": "Database operation failed",
        }, 500
