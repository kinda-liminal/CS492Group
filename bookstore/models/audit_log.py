"""The audit log: one row for each change to books, sales, orders, and accounts."""
from datetime import datetime, timezone

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..extensions import db


def utc_now():
    """The current time in UTC. The database keeps all times in UTC."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class AuditLogEntry(db.Model):
    """One recorded action: who did it, what they did, to what, and when."""

    __tablename__ = "audit_log"

    log_id: Mapped[int] = mapped_column(primary_key=True)
    staff_id: Mapped[int | None]
    action: Mapped[str] = mapped_column(String(50))
    entity_type: Mapped[str] = mapped_column(String(50))
    entity_id: Mapped[int | None]
    timestamp: Mapped[datetime] = mapped_column(default=utc_now)