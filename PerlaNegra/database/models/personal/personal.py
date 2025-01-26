import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class Personal(rx.Model, TimestampMixin, table=True):
    __tablename__ = "personal"
    id: int | None = Field(default=None, primary_key=True)
    personalR_id: int | None = Field(foreign_key="personalr.id")
    personalS_id: int | None = Field(foreign_key="personals.id")
