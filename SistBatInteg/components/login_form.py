"""Módulo que contiene el formulario de inicio de sesión.

Este módulo proporciona componentes para renderizar el formulario de inicio de sesión,
permitiendo a los usuarios autenticarse en el sistema mediante su nombre de usuario
y contraseña.

Functions:
    login_default() -> rx.Component: Renderiza el formulario de inicio de sesión 
        con los campos de usuario y contraseña.
"""

import reflex as rx
from ..database.models.permisos.usuario import Usuario


class UserState(rx.State):
    usuario: list[Usuario]
    pass


def login_default() -> rx.Component:
    """Módulo que contiene el formulario de inicio de sesión.

    Este módulo proporciona componentes para renderizar el formulario de inicio de sesión,
    permitiendo a los usuarios autenticarse en el sistema mediante su nombre de usuario
    y contraseña.

    Functions:
        login_default() -> rx.Component: Renderiza el formulario de inicio de sesión 
            con los campos de usuario y contraseña. Incluye:
            - Logo del sistema
            - Título del formulario
            - Campo de usuario
            - Campo de contraseña
            - Enlace para recuperar contraseña
            - Botón de inicio de sesión

    Returns:
        rx.Component: Un componente Reflex que contiene el formulario de login completo
            estilizado con la interfaz visual del sistema.
    """
    # UserState.
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Ingrese con su cuenta",
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
                    "Usuario",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="su usuario aquí",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
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
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Ingrese su contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )
