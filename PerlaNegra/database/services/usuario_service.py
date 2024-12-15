"""Módulo que contiene los servicios relacionados con la gestión de usuarios."""
import reflex as rx
from datetime import datetime, timezone
from typing import Optional, Tuple
from sqlmodel import Session, select

from ..models.permisos.usuario import Usuario


class UsuarioService(rx.State):
    """Servicio que maneja la lógica de negocio relacionada con los usuarios.

    Este servicio proporciona métodos para gestionar usuarios del sistema,
    incluyendo operaciones como creación, autenticación y actualización
    de usuarios.

    Attributes:
        No tiene atributos ya que todos sus métodos son estáticos.
    """

    name: str
    users: list[Usuario]

    @rx.event
    def select_all(self):
        with rx.session() as session:
            query = select(Usuario)
            result = session.exec(query)
            usuarios = result.scalars().all()
            return list(usuarios)

    @rx.event
    def select_user(self):
        with rx.session() as session:
            self.users = session.exec(
                Usuario.select().where(
                    Usuario.nombre_usuario.__contains__(self.name)
                )
            ).all()

    @ staticmethod
    async def crear_usuario(
        nombre_usuario: str,
        contrasena: str,
        personal_id: int
    ) -> Tuple[Optional[Usuario], str]:
        """
        Crea un nuevo usuario en la base de datos.

        Returns:
            Tupla (Usuario, mensaje_error). Si hay error, Usuario será None
        """
        try:
            # Verificar si el usuario ya existe
            usuario_existente = await Usuario.select().where(
                Usuario.nombre_usuario == nombre_usuario
            ).first()

            if usuario_existente:
                return None, "El nombre de usuario ya está en uso"

            # Crear nuevo usuario
            nuevo_usuario = Usuario(
                nombre_usuario=nombre_usuario,
                hash_contrasena=contrasena,
                personal_id=personal_id,
                creado_en=datetime.now(timezone.utc),
                cambiar_contrasena=False
            )

            # Guardar en la base de datos
            await nuevo_usuario.save()
            return nuevo_usuario, ""

        except Exception as e:
            error_msg = f"Error inesperado: {str(e)}"
            print(error_msg)
            return None, error_msg
