import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.telefono import Telefono


class TelefonoState(rx.State):
    # Estado inicial
    personal_id: int | None = 0
    numero_telefono: str = ""
    tipo_telefono: str = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def telefono_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Teléfono", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Número de Teléfono"),
                rx.input(
                    name="numero_telefono",
                    placeholder="Ingrese el número de teléfono",
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Tipo de Teléfono"),
                rx.input(
                    name="tipo_telefono", placeholder="Ingrese el tipo de teléfono"
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
            rx.form(
                rx.text("Fecha de Actualización"),
                rx.input(
                    type_="datetime-local",
                    name="updated_at",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Teléfono",
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
        on_submit=TelefonoState.handle_submit,
    )


@template(
    route="/p/telefono",
    title="Teléfono",
    on_load=ProtectedState.on_load,
)
def telefono_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            telefono_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
