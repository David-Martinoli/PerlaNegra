from enum import Enum
import reflex as rx

# from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, func, Relationship
from datetime import date, datetime

# from PerlaNegra.database.models.personal.personal import Personal

# from ..personal.personal import Personal
from ..mixins.timestamp_mixin import TimestampMixin
from ..config_scan_models import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, UPLOAD_PATH
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class TipoFelicitacion(str, Enum):
    DESEMPEÑO = "DESEMPEÑO"
    SERVICIO = "SERVICIO"
    MERITO = "MERITO"
    HONOR = "HONOR"


class Felicitacion(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar felicitaciones del personal.

    Attributes:
        fecha: Fecha de la felicitación
        causa: Motivo principal
        descripcion: Detalle de la felicitación
        tipo: Tipo de felicitación
    """

    __tablename__ = "felicitacion"
    id: int | None = Field(default=None, primary_key=True)
    quien_impone: int = Field(foreign_key="personal.id")
    personal_id: int | None = Field(foreign_key="personal.id")

    fecha: date
    causa: str = Field(max_length=200)
    descripcion: str = Field(max_length=1000)
    tipo: TipoFelicitacion = Field(default=TipoFelicitacion.DESEMPEÑO)

    ruta_archivo_imagen: str | None = None
    nombre_archivo_imagen: str | None = None
    nombre_original: str = Field(max_length=255)
    hash_md5: str | None = Field(default=None)

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
    personal_quien_impone_felicitacion_relation: "Personal" = Relationship(
        back_populates="felicitacion_personal_quien_impone_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.quien_impone",
        },
    )
    personal_personal_felicitacion_relation: "Personal" = Relationship(
        back_populates="personal_felicitacion_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.personal_id",
        },
    )

    # @validator("causa", "descripcion")
    # def validar_texto(cls, v):
    #    return v.strip()

    def __repr__(self) -> str:
        return f"Felicitacion(personal_id={self.personal_id}, tipo={self.tipo})"
