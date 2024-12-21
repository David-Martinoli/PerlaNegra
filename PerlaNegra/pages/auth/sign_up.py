from ... import styles
from ...templates import template

import reflex as rx
import re

from ...components.auth.local_auth_state import LocalAuthState
from ...database.services.usuario_service import UsuarioService


class RegisterState(rx.State):
    user_name: str = ""
    password: str = ""
    confirm_password: str = ""
    messages = []
    registration_message: str = ""

    SHOW_PASSWORD: bool = False

    @rx.var
    def password_validation_messages(self) -> list[str]:
        messages = []
        pass1 = self.password
        pass2 = self.confirm_password

        if not pass1 or not pass2:
            messages.append("Both password fields are required.")
            return messages

        if pass1 != pass2:
            messages.append("Passwords do not match.")

        if len(pass1) < 6:
            messages.append("Password must be at least 6 characters long.")

        # if not re.search(r"[A-Z]", pass1):
        #    messages.append(
        #        "Password must contain at least one uppercase letter.")

        if not re.search(r"[a-z]", pass1):
            messages.append("Password must contain at least one lowercase letter.")

        if not re.search(r"[0-9]", pass1):
            messages.append("Password must contain at least one number.")

        if re.search(r"\s", pass1):
            messages.append("Password cannot contain spaces.")

        # if not re.search(r"[!@#$%^&*()_+\-=$$$${};':\"\\|,.<>\/?]", pass1):
        #    messages.append(
        #        "Password must contain at least one special character.")

        return messages

    @rx.var
    def show_password(self) -> bool:
        return not self.SHOW_PASSWORD

    @rx.event
    def set_show_password(self, value: bool):
        self.SHOW_PASSWORD = value

    @rx.var
    def is_password_valid(self) -> bool:
        return not self.password_validation_messages

    @rx.event
    def update_password(self, value: str):
        self.password = value

    @rx.event
    def update_confirm_password(self, value: str):
        self.confirm_password = value

    @rx.var
    def is_passwords_equal(self) -> bool:
        return self.password == self.confirm_password

    @rx.event
    def set_password(self, value: str):
        self.password = value

    @rx.event
    def set_confirm_password(self, value: str):
        self.password = value

    @rx.event
    def set_user_name(self, value: str):
        self.user_name = value


@template(route="/sign_up", title="Sign Up")
def sign_up() -> rx.Component:
    return rx.form(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.heading(
                        "Create an account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Username",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        name="nombre_usuario",
                        placeholder="your username",
                        on_change=RegisterState.set_user_name,
                        type="text",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        name="hash_contrasena",
                        placeholder="Enter your password",
                        type=rx.cond(RegisterState.SHOW_PASSWORD, "text", "password"),
                        size="3",
                        width="100%",
                        on_change=RegisterState.set_password,
                        style={
                            "border": "2px solid "
                            + rx.cond(RegisterState.is_passwords_equal, "green", "red")
                        },
                    ),
                    rx.unordered_list(
                        rx.foreach(
                            RegisterState.password_validation_messages,
                            lambda msg: rx.list_item(msg),
                        )
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Repeat Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Repeat your password",
                        type=rx.cond(RegisterState.SHOW_PASSWORD, "text", "password"),
                        size="3",
                        width="100%",
                        on_change=RegisterState.set_confirm_password,
                        style={
                            "border": "2px solid "
                            + rx.cond(RegisterState.is_passwords_equal, "green", "red")
                        },
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Mostrar contraseñas",
                        default_checked=RegisterState.SHOW_PASSWORD,
                        spacing="2",
                        on_change=RegisterState.set_show_password,
                    ),
                    width="100%",
                ),
                rx.button(
                    "Register",
                    size="3",
                    width="100%",
                    type="submit",
                    disabled=rx.cond(RegisterState.is_passwords_equal, True, False),
                ),
                rx.text(
                    RegisterState.registration_message,
                    size="3",
                    color=rx.cond(RegisterState.registration_message, "green", "red"),
                    text_align="center",
                    width="100%",
                ),
                rx.center(
                    rx.text("Already registered?", size="3"),
                    rx.link(
                        "Sign in",
                        href="#",
                        size="3",
                        on_click=rx.redirect("/sign_in"),
                    ),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
        ),
        max_width="28em",
        size="4",
        width="100%",
        on_submit=UsuarioService.add_user,
        reset_on_submit=True,
    )
