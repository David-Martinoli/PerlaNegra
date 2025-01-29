import reflex as rx
from pathlib import Path
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from ..config_scan_models import (
    ALLOWED_EXTENSIONS,
    MAX_FILE_SIZE,
    UPLOAD_PATH,
    TipoDocumentoActuacion,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actuacion import Actuacion


class ActuacionScan(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar documentos escaneados de actuaciones.

    Attributes:
        imagen: Ruta al archivo escaneado
        descripcion: Descripción del documento
        nombre_archivo: Nombre único del archivo
    """

    __tablename__ = "actuacionscan"
    id: int | None = Field(default=None, primary_key=True)
    actuacion_id: int | None = Field(foreign_key="actuacion.id")
    tipo: TipoDocumentoActuacion = Field(default=TipoDocumentoActuacion.OTRO)
    ruta_archivo_imagen: str | None = None
    nombre_archivo_imagen: str | None = None
    nombre_original: str = Field(max_length=255)
    descripcion: str | None = Field(default=None, max_length=500)
    hash_md5: str | None = Field(default=None)
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )

    # Relaciones
    actuacion_scan_actuacion_relation: "Actuacion" = Relationship(
        back_populates="actuacion_actuacion_scan_relation"
    )

    # Validadores
    # @validator("imagen")
    # def validar_archivo(cls, v):
    #    ext = Path(v).suffix.lower()
    #    if ext not in ALLOWED_EXTENSIONS:
    #        raise ValueError(f"Extensión no permitida. Use: {ALLOWED_EXTENSIONS}")
    #    return v

    #        @validator("archivo")
    #    def validar_archivo(cls, v):
    #        ext = Path(v).suffix.lower()
    #        if ext not in ALLOWED_EXTENSIONS:
    #            raise ValueError(f"Extensión no válida: {ext}")
    #        return v

    @property
    def ruta_completa(self) -> Path:
        """Retorna la ruta completa del archivo."""
        return Path(self.ruta_archivo_imagen) / self.nombre_archivo_imagen

    @property
    def url(self) -> str:
        return f"{UPLOAD_PATH}{self.ruta_archivo_imagen}{self.nombre_archivo_imagen}"
