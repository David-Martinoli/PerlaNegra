import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.unidad import Unidad


class UnidadState(rx.State):
    # Estado inicial
    nombre: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def unidad_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Unidad", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(
                    name="nombre",
                    placeholder="Ingrese el nombre de la unidad",
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="datetime-local",
                    name="created_at",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Unidad",
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
        on_submit=UnidadState.handle_submit,
    )


@template(
    route="/p/unidad",
    title="Unidad",
    on_load=ProtectedState.on_load,
)
def unidad_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            unidad_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
