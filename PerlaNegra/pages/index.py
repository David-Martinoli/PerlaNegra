import reflex as rx
from ..templates import template

from ..components.auth.local_auth_state import LocalAuthState


@template(route="/", title="Inicio")
def index() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.cond(
                LocalAuthState.is_authenticated,
                rx.text("autenticado"),
                rx.text("Not authenticated"),  # Show temporary message
            ),
            opacity="0.8",
            spacing="2",
            direction="row",
            width="100%",
            justify="center",
            align="center",
        ),
        spacing="6",
        width="100%",
        justify="center",
        align="center",
    )
