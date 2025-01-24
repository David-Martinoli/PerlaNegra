import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.cuadro import Cuadro


class CuadroState(rx.State):
    # Estado inicial
    categoria_personal_id: int | None = 0
    nombre: str = ""
    iniciales: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def cuadro_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Cuadro", size="2", mb=4),
            rx.form(
                rx.text("ID Categoría Personal"),
                rx.input(name="categoria_personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre", placeholder="Ingrese el nombre del cuadro"),
                is_required=True,
            ),
            rx.form(
                rx.text("Iniciales"),
                rx.input(name="iniciales", placeholder="Ingrese las iniciales"),
                is_required=True,
            ),
            rx.button(
                "Guardar Cuadro",
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
        on_submit=CuadroState.handle_submit,
    )


@template(
    route="/p/cuadro",
    title="Cuadro",
    on_load=ProtectedState.on_load,
)
def cuadro_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            cuadro_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
