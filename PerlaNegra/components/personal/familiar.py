import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.familiar import Familiar


class FamiliarState(rx.State):
    # Estado inicial
    nombre: str = ""
    apellido: str = ""
    personal_id: int = 0
    dni: str = ""
    nacionalidad: str = ""
    fecha_nacimiento: date = date.today()
    vinculo_familiar_id: int = 0
    fecha_vinculo: date = date.today()
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def familiar_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Familiar", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(name="nombre", placeholder="Ingrese el nombre"),
                is_required=True,
            ),
            rx.form(
                rx.text("Apellido"),
                rx.input(name="apellido", placeholder="Ingrese el apellido"),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("DNI"),
                rx.input(name="dni", placeholder="Ingrese el DNI"),
                is_required=True,
            ),
            rx.form(
                rx.text("Nacionalidad"),
                rx.input(name="nacionalidad", placeholder="Ingrese la nacionalidad"),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Nacimiento"),
                rx.input(
                    type_="date",
                    name="fecha_nacimiento",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Vínculo Familiar"),
                rx.input(name="vinculo_familiar_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Vínculo"),
                rx.input(
                    type_="date",
                    name="fecha_vinculo",
                    default_value=date.today().isoformat(),
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
                "Guardar Familiar",
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
        on_submit=FamiliarState.handle_submit,
    )


@template(
    route="/p/familiar",
    title="Familiar",
    on_load=ProtectedState.on_load,
)
def familiar_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            familiar_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
