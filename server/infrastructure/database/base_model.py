import uuid
from datetime import UTC, datetime

from sqlalchemy import UUID, DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

# Column order in CREATE TABLE: id first, model columns (0), then timestamps/audit
PK_SORT_ORDER = -100
TRAILING_SORT_ORDER = 100


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        default=lambda: datetime.now(UTC),
        comment="Timestamp the record was created",
        sort_order=TRAILING_SORT_ORDER,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        comment="Timestamp the record was last updated",
        sort_order=TRAILING_SORT_ORDER + 1,
    )


class AuditMixin:
    created_by: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=True,
        comment="User who created the record; NULL for system/integration inserts",
        sort_order=TRAILING_SORT_ORDER + 2,
    )
    updated_by: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=True,
        comment="User who last updated the record; NULL for system/integration updates",
        sort_order=TRAILING_SORT_ORDER + 3,
    )


class PrimaryKeyMixin:
    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        sort_order=PK_SORT_ORDER,
    )


class BaseModel(PrimaryKeyMixin, TimeStampMixin):
    pass


class AuditableBaseModel(BaseModel, TimeStampMixin, AuditMixin):
    pass
