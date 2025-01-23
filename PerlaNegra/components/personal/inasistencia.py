import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.inasistencia import Inasistencia


class InasistenciaState(rx.State):
    # Estado inicial
    fecha: date = date.today()
    personal_id: int = 0
    inasistencia_motivo_id: int = 0
    motivo: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def inasistencia_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Inasistencia", size="2", mb=4),
            rx.form(
                rx.text("Fecha"),
                rx.input(
                    type_="date",
                    name="fecha",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("ID Motivo de Inasistencia"),
                rx.input(
                    name="inasistencia_motivo_id",
                    type_="number",
                    min_=1,
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Motivo"),
                rx.text_area(
                    placeholder="Ingrese el motivo",
                    name="motivo",
                    min_height="100px",
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="created_at",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Inasistencia",
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
        on_submit=InasistenciaState.handle_submit,
    )


@template(
    route="/p/inasistencia",
    title="Inasistencia",
    on_load=ProtectedState.on_load,
)
def inasistencia_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            inasistencia_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
