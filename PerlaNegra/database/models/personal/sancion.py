import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal
    from .tipo_sancion import TipoSancion
    from .sancion_scan import SancionScan


# //graves leves ( gravisimas  generan actuacion disiplinaria )
class Sancion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "sancion"
    id: int | None = Field(default=None, primary_key=True)
    motivo: str
    tipo_sansion_id: int | None = Field(foreign_key="tiposancion.id")
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

    # Relaciones
    sancion_sancion_scan_relation: list["SancionScan"] = Relationship(
        back_populates="sancion_scan_sancion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    sancion_tipo_sancion_relation: "TipoSancion" = Relationship(
        back_populates="tipo_sancion_sancion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    sancion_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_sancion_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.personal_id",
            "lazy": "joined",
        },
    )
    sancion_personal_autoridad_relation: "Personal" = Relationship(
        back_populates="personal_autoridad_sancion_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.autoridad_id",
            "lazy": "joined",
        },
    )
