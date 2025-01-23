import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.clase_formacion_academica import (
    ClaseFormacionAcademica,
)


class ClaseFormacionAcademicaState(rx.State):
    # Estado inicial
    nombre: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def clase_formacion_academica_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Clase de Formación Académica", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre", placeholder="Ingrese el nombre de la clase"),
                is_required=True,
            ),
            rx.button(
                "Guardar Clase de Formación Académica",
                type_="submit",
                width="100%",
                bg="blue.500",
                color="white",
                mt=4,
            ),
            spacing="4",
            width="100%",
            max_width="600px",
        ),
        on_submit=ClaseFormacionAcademicaState.handle_submit,
    )


@template(
    route="/p/clase_formacion_academica",
    title="Clase de Formación Académica",
    on_load=ProtectedState.on_load,
)
def clase_formacion_academica_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            clase_formacion_academica_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
