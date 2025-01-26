import reflex as rx
from typing import TYPE_CHECKING
from datetime import datetime

import uuid  # https://docs.python.org/3/library/uuid.html
from sqlmodel import Field, func, Relationship

from .actuacion_disciplinaria import ActuacionDisciplinaria
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria import ActuacionDisciplinaria


class ActuacionDisciplinariaScan(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar documentos escaneados de actuaciones disciplinarias.

    Attributes:
        imagen: Ruta al archivo de imagen escaneado
        descripcion: Descripción del documento
        actuacion: Relación con la actuación disciplinaria
    """

    __tablename__ = "actuaciondisciplinariascan"
    id: int | None = Field(default=None, primary_key=True)
    imagen: str
    descripcion: str
    actuacion_disciplinaria_id: int | None = Field(
        foreign_key="actuaciondisciplinaria.id", index=True, nullable=False
    )
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    actuacion: "ActuacionDisciplinaria" = Relationship(back_populates="scans")
