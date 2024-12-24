import reflex as rx
import reflex_local_auth

from ..components.auth.state import ProtectedState, SessionState
from ..templates import template

from ..components.auth_old.local_auth_state import LocalAuthState


@template(route="/", title="Inicio", on_load=ProtectedState.on_load)
@reflex_local_auth.require_login
def index() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.cond(
                SessionState.is_authenticated,
                # LocalAuthState.is_authenticated,
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
