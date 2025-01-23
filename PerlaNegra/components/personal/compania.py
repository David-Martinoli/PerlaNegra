import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.compania import Compania


class CompaniaState(rx.State):
    # Estado inicial
    unidad_id: int = 0
    nombre: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def compania_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Compañía", size="2", mb=4),
            rx.form(
                rx.text("ID Unidad"),
                rx.input(name="unidad_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre", placeholder="Ingrese el nombre de la compañía"),
                is_required=True,
            ),
            rx.button(
                "Guardar Compañía",
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
        on_submit=CompaniaState.handle_submit,
    )


@template(
    route="/p/compania",
    title="Compañía",
    on_load=ProtectedState.on_load,
)
def compania_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            compania_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
