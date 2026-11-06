
"""
Ascendor API routes.

This module will define the application's API endpoints.
"""

from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():
    """Check whether the API is responding."""
    return {
        "service": "Ascendor Lead-to-Revenue Engine",
        "status": "healthy",
        "version": "0.1.0",
    }, 200
