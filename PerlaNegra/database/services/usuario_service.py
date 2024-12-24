import reflex as rx
from typing import Any

from ..models.permisos.usuario import Usuario
from ...components.auth_old.local_auth_state import LocalAuthState


class UsuarioService(rx.State):
    user: Usuario | None = None

    def add_user(self, form_data: dict[str, Any]):
        get_user_by_username = self.get_user_by_username(form_data["nombre_usuario"])
        if not get_user_by_username:
            self._create_user(form_data)
            return True
        return False

    # privada, no debe ser llamada desde fuera de la clase
    def _create_user(self, form_data: dict[str, Any]):
        with rx.session() as session:
            self.user = Usuario(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)

            # LocalAuthState.AUTENTICATED_STATE = True
            # print(LocalAuthState.AUTENTICATED_STATE)

    def get_user(self, user_id: int) -> Usuario | None:
        with rx.session() as session:
            return session.get(Usuario, user_id)

    def get_user_by_username(self, username: str) -> Usuario | None:
        with rx.session() as session:
            return session.exec(
                Usuario.select().where(Usuario.nombre_usuario == username)
            ).first()
