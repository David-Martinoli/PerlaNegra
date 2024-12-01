import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from sqlalchemy import text
from ..mixins.timestamp_mixin import TimestampMixin
from alembic import op

class Usuario(TimestampMixin, rx.Model, table=True):
    id: int = Field(primary_key=True)
    personal_id: int | None = Field(nullable=True, default=None) # foreign_key='personal.id'
    nombre_usuario: str = Field(nullable=False)
    hash_contrasena: str = Field(nullable=False)
    cambiar_contrasena: bool = Field(default=False)
    creado_en: datetime = Field(default=lambda: datetime.now(timezone.utc))
    
    '''	
    cambiar_contrasena: bool = Field(
        default=False,
        nullable=False,
        server_default=text('0')
    )
    
    creado_en: datetime = Field(default=lambda: datetime.now(timezone.utc))
    '''