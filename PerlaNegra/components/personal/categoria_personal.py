import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.categoria_personal import CategoriaPersonal


class CategoriaPersonalState(rx.State):
    # Estado inicial
    nombre: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def categoria_personal_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Categoría Personal", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(
                    name="nombre", placeholder="Ingrese el nombre de la categoría"
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Categoría Personal",
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
        on_submit=CategoriaPersonalState.handle_submit,
    )


@template(
    route="/p/categoria_personal",
    title="Categoría Personal",
    on_load=ProtectedState.on_load,
)
def categoria_personal_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            categoria_personal_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
