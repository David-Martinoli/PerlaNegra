import reflex as rx

from ... import styles
from ...templates import template


from ...database.services.usuario_service import UsuarioService


@template(route="/sign_in", title="Sign in")
def sign_in() -> rx.Component:
    return rx.form(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.heading(
                        "Sign in to your account",
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
                        "User name",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        name="nombre_usuario",
                        placeholder="Your user name here",
                        type="text",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        # rx.link("Forgot password?",href="#",size="3",),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        name="hash_contrasena",
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%", type="submit"),
                rx.center(
                    rx.text("New here?", size="3"),
                    rx.link(
                        "Sign up",
                        href="#",
                        size="3",
                        on_click=rx.redirect("/sign_up"),
                    ),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width="28em",
            size="4",
            width="100%",
        ),
        # on_submit=UsuarioService.login,
        # on_submit=UsuarioService.login_handle_submit,
        reset_on_submit=True,
    )
