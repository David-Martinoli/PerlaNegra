import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .personal import Personal


class Direccion(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar direcciones del personal.

    Attributes:
        calle: Nombre de calle y número
        ciudad: Ciudad/Localidad
        estado: Estado/Provincia
        codigo_postal: Código postal
        pais: País
    """

    __tablename__ = "direccion"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")  # personalR
    # Campos obligatorios
    calle: str = Field(..., min_length=3, max_length=200)
    ciudad: str = Field(..., min_length=2, max_length=100)

    # Campos opcionales
    estado: str = Field(default="", max_length=100)
    codigo_postal: str = Field(default="", max_length=10)
    pais: str = Field(default="Argentina", max_length=50)

    tipo_direccion: str = ""
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=True,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    personal_direccion_relation: "Personal" = Relationship(
        back_populates="direccion_personal_relation",
    )

    # @validator("codigo_postal")
    # def validar_cp(cls, v):
    #     return v.strip().upper()

    def __repr__(self) -> str:
        return f"Direccion({self.calle}, {self.ciudad})"
