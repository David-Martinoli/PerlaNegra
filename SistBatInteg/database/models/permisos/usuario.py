import reflex as rx
from datetime import datetime, UTC

class Usuario(rx.Model, table=True):
    id: int = rx.Field(primary_key=True)
    personal_id: int = rx.Field(foreign_key='personal.id')
    nombre_usuario: str
    hash_contrasena: str
    cambiar_contrasena: bool = False
    creado_en: datetime = datetime.now(datetime.UTC)