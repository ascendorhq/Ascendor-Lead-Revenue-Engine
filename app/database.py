

"""
Ascendor PostgreSQL database connection module.
"""

import os

import psycopg
from psycopg.rows import dict_row


def get_connection():
    """Create and return a PostgreSQL database connection."""

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL environment variable is not configured."
        )

    return psycopg.connect(
        database_url,
        row_factory=dict_row,
    )
