import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


class Personal(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personalR_id: int = Field(foreign_key="personalr.id")
    personalS_id: int = Field(foreign_key="personals.id")
