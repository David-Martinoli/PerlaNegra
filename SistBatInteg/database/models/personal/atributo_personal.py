import reflex as rx
from datetime import date, datetime

class AtributoPersonal(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    clave_id: int = rx.Field(foreign_key='atributo_clave.id')
    valor: str