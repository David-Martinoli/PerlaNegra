import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

#     para datos supuestos agrego campos genericos
#     en estos campos se puede almacenar la informacion que se requiera
#     segun la necedad que tenga cada unidad o equipo */


# /* Nombre del atributo que se le agrega al personal */
class AtributoClave(rx.Model, TimestampMixin, table=True):
    __tablename__ = "atributoclave"
    id: int | None = Field(default=None, primary_key=True)
    clave: str
