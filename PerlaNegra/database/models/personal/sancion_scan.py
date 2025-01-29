import reflex as rx
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


class SancionScan(rx.Model, TimestampMixin, table=True):
    __tablename__ = "sancionscan"
    id: int | None = Field(default=None, primary_key=True)
    sancion_id: int | None = Field(foreign_key="sancion.id")
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
    sancion_scan_sancion_relation: "Sancion" = Relationship(
        back_populates="sancion_sancion_scan_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    @property
    def ruta_completa(self) -> Path:
        """Retorna la ruta completa del archivo."""
        return Path(self.ruta_archivo_imagen) / self.nombre_archivo_imagen

    @property
    def url(self) -> str:
        return f"{UPLOAD_PATH}{self.ruta_archivo_imagen}{self.nombre_archivo_imagen}"
