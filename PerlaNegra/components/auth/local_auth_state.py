import reflex as rx

from ...database.models.permisos.usuario import Usuario


class LocalAuthState(rx.State):
    AUTENTICATED_USER: Usuario = Usuario(id=-1)
    AUTENTICATED_STATE: bool = False
    # USER_NAME_FOR_LOGIN: str = ""
    # PASSWORD_FOR_LOGIN: str = ""

    def _change_autenticate_state(self) -> bool:
        if self.AUTENTICATED_STATE:
            return True
        return False

    @rx.var(cache=True)
    def is_authenticated(self) -> bool:
        return self.AUTENTICATED_STATE

    def logout(self):
        self.AUTENTICATED_USER = Usuario(id=-1)
        self.AUTENTICATED_STATE = False
