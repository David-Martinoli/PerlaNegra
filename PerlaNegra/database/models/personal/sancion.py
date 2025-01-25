import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class Sancion(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    motivo: str
    tipo_sancion_id: int | None = Field(foreign_key="tiposancion.id")
    fecha: date
    personal_id: int | None = Field(foreign_key="personal.id")
    autoridad_id: int | None = Field(foreign_key="personal.id")
    fecha_comision: date
    fecha_aplicacion: date
    fecha_revision_jefe: date
    fecha_recurso: date
    dias_arresto: int
    descripcion_reglamentaria: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
