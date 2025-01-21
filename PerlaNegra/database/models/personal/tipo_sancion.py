import reflex as rx
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from personal_s import PersonalS


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class TipoSancion(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
