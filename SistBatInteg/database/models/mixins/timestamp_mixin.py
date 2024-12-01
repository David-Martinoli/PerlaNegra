import reflex as rx
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import event

class TimestampMixin():
    created_at: datetime = rx.Field(default_factory=datetime.utcnow)
    updated_at: datetime = rx.Field(default_factory=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        super().save(*args, **kwargs)

@event.listens_for(TimestampMixin, 'before_update', propagate=True)
def update_timestamp(mapper, connection, target):
    target.updated_at = datetime.utcnow()