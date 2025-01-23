import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.personal_seguro import PersonalSeguro


class PersonalSeguroState(rx.State):
    # Estado inicial
    personal_id: int = 0
    seguro_id: int = 0
    fecha_asignacion: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def personal_seguro_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Personal Seguro", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("ID Seguro"),
                rx.input(name="seguro_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Fecha de Asignación"),
                rx.input(
                    type_="datetime-local",
                    name="fecha_asignacion",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Personal Seguro",
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
        on_submit=PersonalSeguroState.handle_submit,
    )


@template(
    route="/p/personal_seguro",
    title="Personal Seguro",
    on_load=ProtectedState.on_load,
)
def personal_seguro_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            personal_seguro_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
