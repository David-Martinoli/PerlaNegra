import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class AtributoPersonal(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    personal_id: int = Field(foreign_key='personal.id')
    clave_id: int = Field(foreign_key='atributoclave.id')
    valor: str