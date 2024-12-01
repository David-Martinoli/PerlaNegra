import reflex as rx
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import event

class TimestampMixin():
    created_at: datetime = rx.Field(default_factory=datetime.now(datetime.UTC))
    updated_at: datetime = rx.Field(default_factory=datetime.now(datetime.UTC))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(datetime.UTC)
        super().save(*args, **kwargs)

@event.listens_for(TimestampMixin, 'before_update', propagate=True)
def update_timestamp(mapper, connection, target):
    target.updated_at = datetime.now(datetime.UTC)