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
    __tablename__ = "atributoclave"
    id: int | None = Field(default=None, primary_key=True)
    clave: str

    # Relaciones
    atributo_clave_atributo_personal_relation: list["AtributoPersonal"] = Relationship(
        back_populates="atributo_personal_atributo_clave_relation"
    )
