import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .atributo_clave import AtributoClave
    from .personal import Personal


class AtributoPersonal(rx.Model, TimestampMixin, table=True):
    """Modelo para almacenar atributos específicos del personal.

    Attributes:
        personal_id: ID del personal asociado
        clave_id: ID de la clave del atributo
        valor: Valor del atributo
    """

    __tablename__ = "atributopersonal"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    clave_id: int | None = Field(foreign_key="atributoclave.id")
    valor: str = Field(max_length=200)
    activo: bool = Field(default=True)

    # Relaciones
    atributo_personal_atributo_clave_relation: "AtributoClave" = Relationship(
        back_populates="atributo_clave_atributo_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    atributo_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_atributo_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("valor")
    # def validar_valor(cls, v):
    #    if not v.strip():
    #        raise ValueError("El valor no puede estar vacío")
    #    return v.strip()

    def __repr__(self) -> str:
        return f"AtributoPersonal(valor={self.valor})"
