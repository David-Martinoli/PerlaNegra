import reflex as rx

from ...components.auth.state import SessionState


class RegisterState(rx.State):
    password: str = ""
    confirm_password: str = ""

    @rx.event
    def update_password(self, value: str):
        self.password = value

    @rx.event
    def update_confirm_password(self, value: str):
        self.confirm_password = value

    @rx.event
    def is_passwords_equal(self) -> bool:
        return self.password == self.confirm_password


def register_form() -> rx.Component:
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
                    "Create an account (register_form)",
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
                    placeholder="your username",
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
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                    on_change=RegisterState.update_password,
                    style={"border": "2px solid " +
                           ("green" if RegisterState.is_passwords_equal() else "red")},
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
                    type="password",
                    size="3",
                    width="100%",
                    on_change=RegisterState.update_confirm_password,
                    style={"border": "2px solid " +
                           ("green" if RegisterState.is_passwords_equal() else "red")},
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.box(
                rx.checkbox(
                    "Agree to Terms and Conditions",
                    default_checked=True,
                    spacing="2",
                ),
                width="100%",
            ),
            rx.button(
                "Register",
                size="3",
                width="100%",
                is_disabled=not RegisterState.is_passwords_equal(),
            ),
            rx.center(
                rx.text("Already registered?", size="3"),
                rx.link("Sign in", href="#", size="3",
                        on_click=SessionState.toggle_form),
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
    )
