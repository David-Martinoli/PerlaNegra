import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class ClaseFormacionAcademica(rx.Model, TimestampMixin, table=True):
    """Modelo para clasificar tipos de formación académica.

    Attributes:
        nombre: Nombre de la clase de formación
        descripcion: Descripción detallada
        activo: Estado de la clase
        orden: Orden de visualización
    """

    __tablename__ = "claseformacionacademica"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str | None = Field(default=None, max_length=500)
    activo: bool = Field(default=True)
    orden: int = Field(default=0)

    # @validator("nombre")
    # def validar_nombre(cls, v):
    #    """Normaliza el nombre."""
    #    return v.strip().upper()

    def __repr__(self) -> str:
        return f"ClaseFormacionAcademica(nombre={self.nombre})"
