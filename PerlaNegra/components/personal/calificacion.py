import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.calificacion import Calificacion


class CalificacionState(rx.State):
    # Estado inicial
    personal_id: int | None = 0
    val1: int = 0
    val2: int = 0
    val3: int = 0
    val4: int = 0
    val5: int = 0
    promedio: float = 0.0
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def calificacion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Calificación", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor 1"),
                rx.input(name="val1", type_="number", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor 2"),
                rx.input(name="val2", type_="number", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor 3"),
                rx.input(name="val3", type_="number", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor 4"),
                rx.input(name="val4", type_="number", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor 5"),
                rx.input(name="val5", type_="number", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Promedio"),
                rx.input(name="promedio", type_="number", step="0.01", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="created_at",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Calificación",
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
        on_submit=CalificacionState.handle_submit,
    )


@template(
    route="/p/calificacion",
    title="Calificación",
    on_load=ProtectedState.on_load,
)
def calificacion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            calificacion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
