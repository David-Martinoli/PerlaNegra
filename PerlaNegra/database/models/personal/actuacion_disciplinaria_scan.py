import reflex as rx
from typing import TYPE_CHECKING
from datetime import datetime
from pathlib import Path

import uuid  # https://docs.python.org/3/library/uuid.html
from sqlmodel import Field, func, Relationship

# from pydantic import BaseModel, field_validator

from .actuacion_disciplinaria import ActuacionDisciplinaria
from ..mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .actuacion_disciplinaria import ActuacionDisciplinaria

ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


class ActuacionDisciplinariaScan(TimestampMixin, rx.Model, table=True):
    """Modelo para almacenar documentos escaneados de actuaciones disciplinarias.

    Attributes:
        imagen: Ruta al archivo de imagen escaneado
        descripcion: Descripción del documento
        actuacion: Relación con la actuación disciplinaria
    """

    __tablename__ = "actuaciondisciplinariascan"
    id: int | None = Field(default=None, primary_key=True)
    ruta_archivo_imagen: str | None = None
    nombre_archivo_imagen: str | None = None
    descripcion: str | None = Field(default=None, max_length=500)
    actuacion_disciplinaria_id: int | None = Field(
        foreign_key="actuaciondisciplinaria.id", index=True, nullable=False
    )
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    actuacion_disciplinaria_scan_actuacion_disciplinaria_relation: (
        "ActuacionDisciplinaria"
    ) = Relationship(
        back_populates="actuacion_disciplinaria_actuacion_isciplinaria_scan_relation",
    )

    # Validadores
    # @field_validator("imagen")
    # def validar_extension(cls, v):
    #    ext = Path(v).suffix.lower()
    #    if ext not in [".pdf", ".jpg", ".jpeg", ".png", ".webp"]:
    #        raise ValueError("Formato de archivo no permitido")
    #    return v

    @property
    def ruta_completa(self) -> Path:
        """Retorna la ruta completa del archivo."""
        return Path(self.ruta_archivo_imagen) / self.nombre_archivo_imagen
