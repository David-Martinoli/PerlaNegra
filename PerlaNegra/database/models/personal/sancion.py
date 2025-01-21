import reflex as rx
from sqlalchemy import Column, ForeignKey
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from personal_s import PersonalS


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class Sancion(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    motivo: str
    tipo_sancion_id: int = Field(foreign_key="tiposansion.id")
    fecha: date
    personal_id: int = Field(foreign_key="personal.id")
    autoridad_id: int = Field(foreign_key="personal.id")
    fecha_comision: date
    fecha_aplicacion: date
    fecha_revision_jefe: date
    fecha_recurso: date
    dias_arresto: int
    descripcion_reglamentaria: str
