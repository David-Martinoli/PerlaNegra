import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class AtributoPersonal(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    clave_id: int = rx.Field(foreign_key='atributo_clave.id')
    valor: str