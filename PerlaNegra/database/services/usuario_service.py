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

    @rx.event
    def login_handle_submit(self, form_data: dict[str, Any]):
        if self.aut:
            self.router.page.path == "/"
        else:
            UsuarioService.login(self, form_data)

    @rx.event
    def login(self, form_data: dict[str, Any]):
        user = self.get_user_by_username(form_data["nombre_usuario"])
        print(form_data)
        if user:
            if user.hash_contrasena == form_data["contrasena"]:
                return user
        return None

    @rx.event
    def add_user(self, form_data: dict[str, Any]):
        get_user_by_username = self.get_user_by_username(form_data["nombre_usuario"])
        if not get_user_by_username:
            self._create_user(form_data)

    # privada, no debe ser llamada desde fuera de la clase
    def _create_user(self, form_data: dict[str, Any]):
        with rx.session() as session:
            self.user = Usuario(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)

    def get_user(self, user_id: int) -> Usuario | None:
        with rx.session() as session:
            return session.get(Usuario, user_id)

    def get_user_by_username(self, username: str) -> Usuario | None:
        with rx.session() as session:
            return session.exec(
                Usuario.select().where(Usuario.nombre_usuario == username)
            ).first()

    """
    def select_all(self):
        with rx.session() as session:
            query = select(Usuario)
            result = session.exec(query)
            usuarios = result.scalars().all()
            return list(usuarios)
    """

    @rx.event
    def select_user(self):
        with rx.session() as session:
            self.users = session.exec(
                Usuario.select().where(Usuario.nombre_usuario.__contains__(self.name))
            ).all()

    @staticmethod
    @rx.event
    def crear_usuario(self):
        with rx.session() as session:
            session.add(Usuario(nombre_usuario=self.user, hash_contrasena=self.passw))
            session.commit()
