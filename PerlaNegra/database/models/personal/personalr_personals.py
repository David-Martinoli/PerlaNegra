import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalR(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    PersonalR_id: int = Field(foreign_key="personal_r.id")
    PersonalS_id: int = Field(foreign_key="personal_s.id")
