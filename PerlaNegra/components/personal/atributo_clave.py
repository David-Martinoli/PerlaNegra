import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.atributo_clave import AtributoClave


class AtributoClaveState(rx.State):
    # Estado inicial
    clave: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def atributo_clave_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Atributo Clave", size="2", mb=4),
            rx.form(
                rx.text("Clave"),
                rx.input(name="clave", placeholder="Ingrese la clave"),
                is_required=True,
            ),
            rx.button(
                "Guardar Atributo Clave",
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
        on_submit=AtributoClaveState.handle_submit,
    )


@template(
    route="/p/atributo_clave",
    title="Atributo Clave",
    on_load=ProtectedState.on_load,
)
def atributo_clave_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            atributo_clave_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
