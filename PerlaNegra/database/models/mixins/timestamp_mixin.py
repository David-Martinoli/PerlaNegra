from datetime import datetime
from sqlmodel import Field, func


class TimestampMixin:
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=True,
        sa_column_kwargs={"onupdate": func.now()},
    )
