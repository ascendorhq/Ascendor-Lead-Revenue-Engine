
"""
Ascendor application entry point.
"""

from flask import Flask
from app.routes import api


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    app.register_blueprint(api)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )
