"""Módulo que define el modelo de Usuario para el sistema."""

from datetime import datetime, timezone
import reflex as rx
from sqlmodel import Field, func
from typing import Optional
from ..mixins.timestamp_mixin import TimestampMixin


class Usuario(TimestampMixin, rx.Model, table=True):
    """Modelo que representa un usuario del sistema.

    Attributes:
        id (int): Identificador único del usuario
        personal_id (int | None): ID del personal asociado al usuario
        nombre_usuario (str): Nombre de usuario para iniciar sesión
        hash_contrasena (str): Hash de la contraseña del usuario
        cambiar_contrasena (bool): Indica si el usuario debe cambiar su contraseña
        created_at (datetime): Fecha y hora de creación del usuario
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    personal_id: Optional[int] = Field(
        nullable=True, default=None
    )  # foreign_key='personal.id'
    nombre_usuario: str = Field(nullable=False)
    hash_contrasena: str = Field(nullable=False)
    cambiar_contrasena: bool = Field(default=False)
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": "CURRENT_TIMESTAMP"},
        default_factory=lambda: datetime.now(timezone.utc),
    )
    # expiration: datetime

    """
    cambiar_contrasena: bool = Field(
        default=False,
        nullable=False,
        server_default=text('0')
    )

    created_at: datetime = Field(default=lambda: datetime.now(timezone.utc))
    """
