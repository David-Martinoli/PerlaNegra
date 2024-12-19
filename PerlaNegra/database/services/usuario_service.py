"""Módulo que contiene los servicios relacionados con la gestión de usuarios."""
import reflex as rx
from datetime import datetime, timezone
from typing import Optional, Tuple
from sqlmodel import Session, select
from typing import Any

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

    user: str
    passw: str

    user: Usuario | None = None

    def add_user(self, form_data: dict[str, Any]):
        with rx.session() as session:
            self.user = Usuario(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)

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

    @staticmethod
    @rx.event
    def crear_usuario(self):
        with rx.session() as session:
            session.add(Usuario(nombre_usuario=self.user,
                        hash_contrasena=self.passw
                                )
                        )
            session.commit()

    @ staticmethod
    def crear_usuario2(
        nombre_usuario: str,
        contrasena: str,
    ) -> Tuple[Optional[Usuario], str]:
        """
        Crea un nuevo usuario en la base de datos.

        Returns:
            Tupla (Usuario, mensaje_error). Si hay error, Usuario será None
        """
        try:
            # Verificar si el usuario ya existe
            usuario_existente = Usuario.select().where(
                Usuario.nombre_usuario == nombre_usuario
            ).first()

            if usuario_existente:
                return None, "El nombre de usuario ya está en uso"

            # Crear nuevo usuario
            nuevo_usuario = Usuario(
                nombre_usuario=nombre_usuario,
                hash_contrasena=contrasena,
                # personal_id=personal_id,
                creado_en=datetime.now(timezone.utc),
                cambiar_contrasena=False
            )

            # Guardar en la base de datos
            nuevo_usuario.save()
            return nuevo_usuario, ""

        except Exception as e:
            error_msg = f"Error inesperado: {str(e)}"
            print(error_msg)
            return None, error_msg
