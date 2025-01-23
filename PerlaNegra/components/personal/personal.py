import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.personal import Personal


class PersonalState(rx.State):
    # Estado inicial
    personalR_id: int = 0
    personalS_id: int = 0
    fecha_creacion: date = date.today()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def personal_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Información Personal", size="2", mb=4),
            rx.form(
                rx.text("ID Personal R"),
                rx.input(name="personalR_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal S"),
                rx.input(name="personalS_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="fecha_creacion",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Información Personal",
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
        on_submit=PersonalState.handle_submit,
    )


@template(
    route="/p/personal",
    title="Información Personal",
    on_load=ProtectedState.on_load,
)
def personal_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            personal_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
