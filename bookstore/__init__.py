"""Pacific Coast Book Store: the Bookstore Management System web app."""
import os
from pathlib import Path

from flask import Flask

from . import models  # noqa: F401  Loads the tables, so migrations can see them.
from .extensions import db, migrate
from .main import bp as main_bp

MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"


def create_app(config_overrides=None, instance_path=None):
    """Build the app. The tests pass their own settings and folder."""
    app = Flask(__name__, instance_path=instance_path)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")
    if config_overrides:
        app.config.update(config_overrides)
    instance = Path(app.instance_path)
    instance.mkdir(parents=True, exist_ok=True)
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", f"sqlite:///{(instance / 'bookstore.db').as_posix()}")

    db.init_app(app)
    migrate.init_app(app, db, directory=str(MIGRATIONS_DIR), render_as_batch=True)

    app.register_blueprint(main_bp)
    return app
