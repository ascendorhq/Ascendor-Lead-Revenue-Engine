
"""
Ascendor application configuration.
"""

import os


class Config:
    APP_NAME = "Ascendor Lead-to-Revenue Engine"
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = APP_ENV == "development"
    TIMEZONE = "Asia/Manila"
