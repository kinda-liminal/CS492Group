"""Shared test setup. Each test gets its own new database."""
import pytest
from flask_migrate import upgrade

from bookstore import create_app
from bookstore.extensions import db


@pytest.fixture
def app(tmp_path):
    """The app with a new SQLite file that the real migrations build."""
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{(tmp_path / 'test.db').as_posix()}",
        },
        instance_path=str(tmp_path / "instance"),
    )
    with app.app_context():
        upgrade()
    yield app
    with app.app_context():
        db.engine.dispose()


@pytest.fixture
def client(app):
    return app.test_client()
