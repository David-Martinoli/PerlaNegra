import reflex as rx
from .. import styles
from ..templates import template

from ..components.auth.state import SessionState
from ..components.auth.login_form import login_form
from ..components.auth.register_form import register_form


@template(route="/", title="Inicio")
def index() -> rx.Component:
    #rx.text(rx.Var())

    form_to_show = rx.cond(
        SessionState.autenticated_state,
        rx.text("autenticado"), rx.cond(
            SessionState.SHOW_LOGIN_OR_REGISTER,
            login_form(),
            register_form()))

    return rx.vstack(
        form_to_show,
        rx.center(
            opacity="0.8",
            spacing="2",
            direction="row",
            width="100%",
        ),
        spacing="6",
        width="100%",
    )
