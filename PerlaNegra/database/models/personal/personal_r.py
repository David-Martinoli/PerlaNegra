# database/models/personal.py
import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalR(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    fecha_nacimiento: date
    dni: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = datetime.now(timezone.utc)
    estado_civil_id: int | None = Field(foreign_key="estadocivil.id")
    cantidad_hijos: int = 0
