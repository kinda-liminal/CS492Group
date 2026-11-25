from sqlalchemy import inspect

from bookstore.extensions import db
from bookstore.models import AuditLogEntry


def test_home_page_opens(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Pacific Coast Book Store" in response.get_data(as_text=True)


def test_migrations_make_the_audit_log_table(app):
    with app.app_context():
        assert "audit_log" in inspect(db.engine).get_table_names()


def test_audit_log_entry_saves_with_a_time(app):
    with app.app_context():
        db.session.add(AuditLogEntry(action="create", entity_type="book", entity_id=1))
        db.session.commit()
        entry = db.session.scalars(db.select(AuditLogEntry)).one()
        assert entry.timestamp is not None
