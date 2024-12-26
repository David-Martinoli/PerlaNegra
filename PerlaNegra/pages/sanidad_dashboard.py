import reflex as rx
import reflex_local_auth

from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.components.sanidad.declaracion_jurada import declaracion_jurada_form

from ..templates import template
from ..components.base import base_page


class SanidadState(rx.State):
    def handle_declaracion_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        # Aquí procesas los datos del formulario
        print("Datos recibidos:", form_data)
        # Implementar la lógica para guardar en la base de datos


@template(route="/sanidad", title="Sanidad", on_load=ProtectedState.on_load)
@reflex_local_auth.require_login
def sanidad_dashboard() -> rx.Component:
    my_child = rx.vstack(
        rx.text("Sanidad Dashboard"),
        declaracion_jurada_form(on_submit=SanidadState.handle_declaracion_submit),
        # aqui agregar la vista para un dashbaord de sanidad
    )
    return base_page(my_child)

"""
@template(route="/declaracion-jurada", title="Declaración Jurada", on_load=ProtectedState.on_load)
def declaracion_jurada_page() -> rx.Component:
    return rx.vstack(
        declaracion_jurada_form(on_submit=SanidadState.handle_declaracion_submit),
        spacing="4",
        align_items="stretch",
    )
"""
