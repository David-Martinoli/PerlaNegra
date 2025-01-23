import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.tipo_sancion import TipoSancion


class TipoSancionState(rx.State):
    # Estado inicial
    nombre: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def tipo_sancion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Tipo de Sanción", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(
                    name="nombre",
                    placeholder="Ingrese el nombre del tipo de sanción",
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
                "Guardar Tipo de Sanción",
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
        on_submit=TipoSancionState.handle_submit,
    )


@template(
    route="/p/tipo_sancion",
    title="Tipo de Sanción",
    on_load=ProtectedState.on_load,
)
def tipo_sancion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            tipo_sancion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
