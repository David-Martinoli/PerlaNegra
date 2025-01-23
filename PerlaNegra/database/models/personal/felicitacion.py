import reflex as rx

# from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone

# from PerlaNegra.database.models.personal.personal import Personal

# from ..personal.personal import Personal
from ..mixins.timestamp_mixin import TimestampMixin


class Felicitacion(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    quien_impone: int = Field(foreign_key="personal.id")
    fecha: date
    causa: str
    descripcion: str
    imagen: str
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
    personal_id: int = Field(foreign_key="personal.id")
    # personal_id: int = Column(ForeignKey(Personal.id))
