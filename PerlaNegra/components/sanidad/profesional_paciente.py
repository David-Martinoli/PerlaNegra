import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.sanidad.profesional_paciente import ProfesionalPaciente


class ProfesionalPacienteState(rx.State):
    # Estado inicial
    profesional_id: int | None = 0
    paciente_id: int | None = 0
    ceso: bool = True
    fecha_asignacion: date = date.today()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def profesional_paciente_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Asignar Profesional a Paciente", size="2", mb=4),
            rx.form(
                rx.text("ID Profesional"),
                rx.input(name="profesional_id", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Paciente"),
                rx.input(name="paciente_id", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Ceso"),
                rx.checkbox(name="ceso"),
            ),
            rx.form(
                rx.text("Fecha de Asignación"),
                rx.input(
                    type_="date",
                    name="fecha_asignacion",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Asignación",
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
        on_submit=ProfesionalPacienteState.handle_submit,
    )


@template(
    route="/s/profesional-paciente",
    title="Asignar Profesional a Paciente",
    on_load=ProtectedState.on_load,
)
def profesional_paciente_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            profesional_paciente_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
