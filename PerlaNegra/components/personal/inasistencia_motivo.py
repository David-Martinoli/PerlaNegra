import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.inasistencia_motivo import InasistenciaMotivo


class InasistenciaMotivoState(rx.State):
    # Estado inicial
    nombre: str = ""
    descripcion: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def inasistencia_motivo_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Motivo de Inasistencia", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre", placeholder="Ingrese el nombre del motivo"),
                is_required=True,
            ),
            rx.form(
                rx.text("Descripción"),
                rx.text_area(
                    placeholder="Ingrese la descripción",
                    name="descripcion",
                    min_height="100px",
                ),
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
                "Guardar Motivo de Inasistencia",
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
        on_submit=InasistenciaMotivoState.handle_submit,
    )


@template(
    route="/p/inasistencia_motivo",
    title="Motivo de Inasistencia",
    on_load=ProtectedState.on_load,
)
def inasistencia_motivo_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            inasistencia_motivo_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
