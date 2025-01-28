import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Familiar(rx.Model, TimestampMixin, table=True):
    __tablename__ = "familiar"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    personal_id: int | None = Field(foreign_key="personal.id")  # personalR
    dni = str
    nacionalidad = str
    fecha_nacimiento: date
    vinculo_familiar_id: int | None = Field(foreign_key="vinculofamiliar.id")
    fecha_vinculo: date
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )
