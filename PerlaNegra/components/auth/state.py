import reflex as rx

# import reflex_local_auth
# import sqlmodel

from sqlmodel import select

# from sqlmodel import Field, Relationship
from ...database.models.permisos.usuario import Usuario


class SessionState(rx.State):
    SHOW_LOGIN_OR_REGISTER: bool = True
    AUTENTICATED_STATE: bool = False
    USER_NAME_FOR_LOGIN: str = ""
    PASSWORD_FOR_LOGIN: str = ""

    @rx.event
    def toggle_form(self):
        self.SHOW_LOGIN_OR_REGISTER = not self.SHOW_LOGIN_OR_REGISTER

    @rx.var(cache=True)
    def autenticated_state(self) -> bool:
        if self.AUTENTICATED_STATE:
            return True
        return False

    @rx.event
    def aut(self) -> bool:
        return self.AUTENTICATED_STATE

    @rx.var(cache=True)
    def autenticate(self) -> bool:
        with rx.session() as session:
            result = session.exec(
                # select(Usuario).where(
                #    Usuario.nombre_usuario == userName and Usuario.hash_contrasena == password
                Usuario.select().where(
                    Usuario.nombre_usuario == self.USER_NAME_FOR_LOGIN
                    and Usuario.hash_contrasena == self.PASSWORD_FOR_LOGIN
                )
            ).first()

            if result.nombre_usuario != "":
                self.AUTENTICATED_STATE = True
                return True

            self.AUTENTICATED_STATE = False
            return False


'''
class SessionState(reflex_local_auth.LocalAuthState):
    @rx.cached_var
    def my_userinfo_id(self) -> str | None:
        if self.authenticated_user_info is None:
            return None
        return self.authenticated_user_info.id

    @rx.cached_var
    def my_user_id(self) -> str | None:
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.id

    @rx.cached_var
    def authenticated_username(self) -> str | None:
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username

    @rx.cached_var
    def authenticated_user_info(self) -> Usuario | None:
        if self.authenticated_user.id < 0:
            return None
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(Usuario).where(
                    Usuario.id == self.authenticated_user.id
                ),
            ).one_or_none()
            if result is None:
                return None
            # database lookup
            # result.user
            # user_obj = result.user
            # print(result.user)
            return result

    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.is_authenticated)
        print(self.authenticated_user_info)

    def perform_logout(self):
        self.do_logout()
        return rx.redirect("/")


class MyRegisterState(reflex_local_auth.RegistrationState):
    def handle_registration(
        self, form_data
    ) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        """Handle registration form on_submit.

        Set error_message appropriately based on validation results.

        Args:
            form_data: A dict of form fields and values.
        """
        username = form_data["username"]
        password = form_data["password"]
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return self.new_user_id

    def handle_registration_email(self, form_data):
        new_user_id = self.handle_registration(form_data)
        if new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    Usuario(
                        email=form_data["email"],
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
        return type(self).successful_registration
'''
