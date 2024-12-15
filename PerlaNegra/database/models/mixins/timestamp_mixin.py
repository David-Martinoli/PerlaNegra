import reflex as rx
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from sqlalchemy import event

class TimestampMixin():
    created_at: datetime = Field(default=datetime.now(timezone.utc))
    updated_at: datetime = Field(default=datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        super().save(*args, **kwargs)

@event.listens_for(TimestampMixin, 'before_update', propagate=True)
def update_timestamp(mapper, connection, target):
    target.updated_at = datetime.now(timezone.utc)