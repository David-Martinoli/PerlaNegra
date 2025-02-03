"""Welcome to Reflex!."""

0
# Import all the pages.
import reflex_local_auth

from .components.auth.pages import my_logout_page
from .pages import *
from . import styles

import reflex as rx


# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)

app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    reflex_local_auth.pages.register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

app.add_page(
    my_logout_page,
    route="log_out",
    title="Logout",
)
