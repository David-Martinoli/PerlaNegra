import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.actuacion_disciplinaria import (
    ActuacionDisciplinaria,
)


class ActuacionDisciplinariaState(rx.State):
    # Estado inicial
    numero_experiente: str = ""
    fecha_inicio: date = date.today()
    fecha_fin: date = date.today()
    personal_id: int | None = 0
    actuante_id: int | None = 0
    causa: str = ""
    observacion: str = ""
    created_at: date = date.today()
    updated_at: date = date.today()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def actuacion_disciplinaria_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Actuación Disciplinaria", size="2", mb=4),
            rx.form(
                rx.text("Número Experiente"),
                rx.input(
                    name="numero_experiente", placeholder="Ingrese el número experiente"
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Inicio"),
                rx.input(
                    type_="date",
                    name="fecha_inicio",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Fin"),
                rx.input(
                    type_="date",
                    name="fecha_fin",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Actuante"),
                rx.input(name="actuante_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Causa"),
                rx.text_area(
                    placeholder="Ingrese la causa",
                    name="causa",
                    min_height="100px",
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Observación"),
                rx.text_area(
                    placeholder="Ingrese la observación",
                    name="observacion",
                    min_height="100px",
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Actuación Disciplinaria",
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
        on_submit=ActuacionDisciplinariaState.handle_submit,
    )


@template(
    route="/p/actuacion_disciplinaria",
    title="Actuación Disciplinaria",
    on_load=ProtectedState.on_load,
)
def actuacion_disciplinaria_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            actuacion_disciplinaria_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
