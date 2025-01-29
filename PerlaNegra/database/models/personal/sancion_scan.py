from enum import Enum
import reflex as rx
import hashlib
from pathlib import Path
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from ..config_scan_models import (
    ALLOWED_EXTENSIONS,
    MAX_FILE_SIZE,
    UPLOAD_PATH,
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sancion import Sancion


class TipoDocumentoSancion(str, Enum):
    RESOLUCION = "resolucion"
    DESCARGO = "descargo"
    INFORME = "informe"
    OTRO = "otro"


class SancionScan(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar documentos escaneados de sanciones."""

    __tablename__ = "sancionscan"

    id: int | None = Field(default=None, primary_key=True)
    sancion_id: int | None = Field(foreign_key="sancion.id")

    # Campos de archivo
    ruta_archivo_imagen: str | None = Field(default=None)
    nombre_archivo_imagen: str | None = Field(default=None)
    nombre_original: str | None = Field(max_length=255, default=None)
    descripcion: str | None = Field(default=None, max_length=500)
    hash_md5: str | None = Field(default=None)

    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    sancion_scan_sancion_relation: "Sancion" = Relationship(
        back_populates="sancion_sancion_scan_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("ruta_archivo")
    # def validar_archivo(cls, v):
    #    ext = Path(v).suffix.lower()
    #    if ext not in ALLOWED_EXTENSIONS:
    #        raise ValueError(f"Extensión no permitida: {ext}")
    #    return v

    def calcular_hash(self, contenido: bytes) -> str:
        """Calcula el hash MD5 del contenido."""
        return hashlib.md5(contenido).hexdigest()

    @property
    def ruta_completa(self) -> Path:
        """Retorna la ruta completa del archivo."""
        return Path(self.ruta_archivo_imagen) / self.nombre_archivo_imagen

    @property
    def url(self) -> str:
        return f"{UPLOAD_PATH}{self.ruta_archivo_imagen}{self.nombre_archivo_imagen}"

    def __repr__(self) -> str:
        return f"SancionScan(sancion_id={self.sancion_id})"
