import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actuacion_scan import ActuacionScan
    from .personal import Personal


class Actuacion(rx.Model, TimestampMixin, table=True):
    __tablename__ = "actuacion"
    id: int | None = Field(default=None, primary_key=True)

    personal_id: int | None = Field(
        foreign_key="personal.id", nullable=False, ondelete="RESTRICT"
    )
    actuante_id: int | None = Field(
        foreign_key="personal.id", nullable=False, ondelete="RESTRICT"
    )

    numero_experiente = str
    causa = str
    fecha_inicio = date
    fecha_fin = date
    estado_tramite = str

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

    # Relaciones
    actuacion_actuacion_scan_relation: list["ActuacionScan"] = Relationship(
        back_populates="actuacion_scan_actuacion_relation"
    )
    actuacion_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_personal_relation",
        sa_relationship_kwargs={"foreign_keys": "Actuacion.personal_id"},
    )
    actuacion_actuante_personal_relation: "Personal" = Relationship(
        back_populates="personal_actuacion_actuante_relation",
        sa_relationship_kwargs={"foreign_keys": "Actuacion.actuante_id"},
    )
