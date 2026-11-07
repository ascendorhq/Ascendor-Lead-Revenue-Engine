
"""
Ascendor application entry point.
"""

from flask import Flask

from app.config import Config
from app.routes import api


def create_app():
    """Create and configure the Flask application."""

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(api)

    return app


if __name__ == "__main__":
    application = create_app()

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=application.config["DEBUG"],
    )
