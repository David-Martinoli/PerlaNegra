import reflex as rx
from sqlmodel import Field, Relationship
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atributo_personal import AtributoPersonal

#     para datos supuestos agrego campos genericos
#     en estos campos se puede almacenar la informacion que se requiera
#     segun la necedad que tenga cada unidad o equipo */


# /* Nombre del atributo que se le agrega al personal */
# /* esto, juunto a atributo clave, son una representacion de un diccionario */1


class AtributoClave(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar claves de atributos del personal.

    Attributes:
        clave: Identificador único del atributo
        descripcion: Descripción del atributo
        activo: Estado del atributo
    """

    __tablename__ = "atributoclave"
    id: int | None = Field(default=None, primary_key=True)
    clave: str = Field(min_length=2, max_length=50, unique=True)
    descripcion: str | None = Field(default=None, max_length=200)
    activo: bool = Field(default=True)

    # Relaciones
    atributo_clave_atributo_personal_relation: list["AtributoPersonal"] = Relationship(
        back_populates="atributo_personal_atributo_clave_relation",
        sa_relationship_kwargs={"lazy": "selectin", "cascade": "all, delete-orphan"},
    )

    # @validator("clave")
    # def validar_clave(cls, v):
    #    """Valida formato de clave."""
    #    if not v.isalnum():
    #        raise ValueError("La clave debe ser alfanumérica")
    #    return v.upper()

    def __repr__(self) -> str:
        return f"AtributoClave(clave={self.clave})"
