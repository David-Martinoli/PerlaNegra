import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.direccion import Direccion


class DireccionState(rx.State):
    # Estado inicial
    personal_id: int = 0
    calle: str = ""
    ciudad: str = ""
    estado: str = ""
    codigo_postal: str = ""
    pais: str = ""
    tipo_direccion: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def direccion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Dirección", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Calle"),
                rx.input(name="calle", placeholder="Ingrese la calle"),
                is_required=True,
            ),
            rx.form(
                rx.text("Ciudad"),
                rx.input(name="ciudad", placeholder="Ingrese la ciudad"),
                is_required=True,
            ),
            rx.form(
                rx.text("Estado"),
                rx.input(name="estado", placeholder="Ingrese el estado"),
                is_required=True,
            ),
            rx.form(
                rx.text("Código Postal"),
                rx.input(name="codigo_postal", placeholder="Ingrese el código postal"),
                is_required=True,
            ),
            rx.form(
                rx.text("País"),
                rx.input(name="pais", placeholder="Ingrese el país"),
                is_required=True,
            ),
            rx.form(
                rx.text("Tipo de Dirección"),
                rx.input(
                    name="tipo_direccion", placeholder="Ingrese el tipo de dirección"
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
                "Guardar Dirección",
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
        on_submit=DireccionState.handle_submit,
    )


@template(
    route="/p/direccion",
    title="Dirección",
    on_load=ProtectedState.on_load,
)
def direccion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            direccion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
