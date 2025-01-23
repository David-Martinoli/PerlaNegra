import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.seccion import Seccion


class SeccionState(rx.State):
    # Estado inicial
    compania_id: int = 0
    nombre: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def seccion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Sección", size="2", mb=4),
            rx.form(
                rx.text("ID Compañía"),
                rx.input(name="compania_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Nombre"),
                rx.input(
                    name="nombre",
                    placeholder="Ingrese el nombre de la sección",
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
                "Guardar Sección",
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
        on_submit=SeccionState.handle_submit,
    )


@template(
    route="/p/seccion",
    title="Sección",
    on_load=ProtectedState.on_load,
)
def seccion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            seccion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
