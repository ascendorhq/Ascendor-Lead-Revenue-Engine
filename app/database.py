
"""
Ascendor PostgreSQL database connection module.
"""

import psycopg
from psycopg.rows import dict_row

from app.config import Config


def get_connection():
    """Create and return a PostgreSQL database connection."""

    database_url = Config.DATABASE_URL

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL environment variable is not configured."
        )

    return psycopg.connect(
        database_url,
        row_factory=dict_row,
    )