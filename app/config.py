

"""
Ascendor application configuration.
"""

import os


class Config:
    """Application configuration."""

    APP_NAME = "Ascendor Lead-to-Revenue Engine"

    APP_ENV = os.getenv("APP_ENV", "development")

    DEBUG = APP_ENV == "development"

    TIMEZONE = "Asia/Manila"

    DATABASE_URL = os.getenv("DATABASE_URL")
