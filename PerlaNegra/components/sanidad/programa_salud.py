import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.sanidad.programa_salud import ProgramaSalud


class ProgramaSaludState(rx.State):
    nombre: str = ""
    tiempo_revision_id: int | None = 0

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def programa_salud_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Programa de Salud", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre"),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Tiempo de Revisión"),
                rx.input(name="tiempo_revision_id", min_=1),
                is_required=True,
            ),
            rx.button(
                "Guardar Programa de Salud",
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
        on_submit=ProgramaSaludState.handle_submit,
    )


@template(
    route="/s/programa-salud",
    title="Programa de Salud",
    on_load=ProtectedState.on_load,
)
def programa_salud_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            programa_salud_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
