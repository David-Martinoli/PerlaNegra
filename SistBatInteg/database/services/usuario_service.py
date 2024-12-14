"""Módulo que contiene los servicios relacionados con la gestión de usuarios."""

from datetime import datetime, timezone
from typing import Optional, Tuple

from ..models.permisos.usuario import Usuario
from ..repository.usuario_repository import select_all


class UsuarioService:
    """Servicio que maneja la lógica de negocio relacionada con los usuarios.

    Este servicio proporciona métodos para gestionar usuarios del sistema,
    incluyendo operaciones como creación, autenticación y actualización
    de usuarios.

    Attributes:
        No tiene atributos ya que todos sus métodos son estáticos.
    """
    async def select_all_usuario():
        usuarios = select_all()
        print(usuarios)
        return usuarios

    @staticmethod
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
