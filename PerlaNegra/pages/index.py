import reflex as rx
from .. import styles
from ..templates import template

from ..components.login_form import login_default
from ..components.user_form import index_usuario_component


class LoginState(rx.State):
    logged_in: bool = False

    @rx.event
    def toggle_login(self):
        self.logged_in = not self.logged_in


def tab_content_header() -> rx.Component:
    return rx.hstack(
        align="center",
        width="100%",
        spacing="4",
    )


def show_login():
    return rx.box(
        rx.cond(
            LoginState.logged_in,
            rx.heading("Logged In"),
            rx.heading("Not Logged In"),
        ),
        rx.button(
            "Toggle Login", on_click=LoginState.toggle_login
        ),
    )

# on_load=StatsState.randomize_data


@template(route="/", title="Inicio")
def index() -> rx.Component:
    """The overview page.

    Returns:
        The UI for the overview page.
    """
    return rx.vstack(
        login_default(),
        index_usuario_component(),
        show_login()
    )
