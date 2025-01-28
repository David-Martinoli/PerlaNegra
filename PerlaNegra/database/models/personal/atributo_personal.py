import reflex as rx
from sqlmodel import Field, func, Relationship
from ..mixins.timestamp_mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .atributo_clave import AtributoClave
    from .personal import Personal


class AtributoPersonal(rx.Model, TimestampMixin, table=True):
    __tablename__ = "atributopersonal"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    clave_id: int | None = Field(foreign_key="atributoclave.id")
    valor: str

    # Relaciones
    atributo_personal_atributo_clave_relation: "AtributoClave" = Relationship(
        back_populates="atributo_clave_atributo_personal_relation"
    )
    atributo_personal_personal_relation: "Personal" = Relationship(
        back_populates="personal_atributo_personal_relation"
    )
