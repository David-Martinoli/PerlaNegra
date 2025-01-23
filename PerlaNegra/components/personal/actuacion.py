import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.actuacion import Actuacion


class ActuacionState(rx.State):
    # Estado inicial
    personal_id: int = 0
    numero_experiente: str = ""
    causa: str = ""
    fecha_inicio: date = date.today()
    fecha_fin: date = date.today()
    estado_tramite: str = ""
    actuante_id: int = 0

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def actuacion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Actuación", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Número Experiente"),
                rx.input(
                    name="numero_experiente", placeholder="Ingrese el número experiente"
                ),
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
                rx.text("Estado de Trámite"),
                rx.input(
                    name="estado_tramite", placeholder="Ingrese el estado del trámite"
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Actuante"),
                rx.input(name="actuante_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.button(
                "Guardar Actuación",
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
        on_submit=ActuacionState.handle_submit,
    )


@template(
    route="/p/actuacion",
    title="Actuación",
    on_load=ProtectedState.on_load,
)
def actuacion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            actuacion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
