import reflex as rx
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.atributo_personal import AtributoPersonal


class AtributoPersonalState(rx.State):
    # Estado inicial
    personal_id: int | None = 0
    clave_id: int | None = 0
    valor: str = ""

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def atributo_personal_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Atributo Personal", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Clave"),
                rx.input(name="clave_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Valor"),
                rx.input(name="valor", placeholder="Ingrese el valor"),
                is_required=True,
            ),
            rx.button(
                "Guardar Atributo Personal",
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
        on_submit=AtributoPersonalState.handle_submit,
    )


@template(
    route="/p/atributo_personal",
    title="Atributo Personal",
    on_load=ProtectedState.on_load,
)
def atributo_personal_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            atributo_personal_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
