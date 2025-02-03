import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.personal_r import PersonalR


class PersonalRState(rx.State):
    # Estado inicial
    nombre: str = ""
    apellido: str = ""
    fecha_nacimiento: date = date.today()
    dni: str = ""
    estado_civil_id: int | None = 0
    cantidad_hijos: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def personal_r_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Personal Responsable", size="2", mb=4),
            rx.form(
                rx.text("Nombre"),
                rx.input(
                    name="nombre", placeholder="Ingrese el nombre", is_required=True
                ),
            ),
            rx.form(
                rx.text("Apellido"),
                rx.input(
                    name="apellido", placeholder="Ingrese el apellido", is_required=True
                ),
            ),
            rx.form(
                rx.text("Fecha de Nacimiento"),
                rx.input(
                    type_="date",
                    name="fecha_nacimiento",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("DNI"),
                rx.input(name="dni", placeholder="Ingrese el DNI", is_required=True),
            ),
            rx.form(
                rx.text("ID Estado Civil"),
                rx.input(
                    name="estado_civil_id", type_="number", min_=1, is_required=True
                ),
            ),
            rx.form(
                rx.text("Cantidad de Hijos"),
                rx.input(
                    name="cantidad_hijos", type_="number", min_=0, is_required=True
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
            rx.form(
                rx.text("Fecha de Actualización"),
                rx.input(
                    type_="date",
                    name="updated_at",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Personal Responsable",
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
        on_submit=PersonalRState.handle_submit,
    )


@template(
    route="/p/personal_r",
    title="Personal Responsable",
    on_load=ProtectedState.on_load,
)
def personal_r_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            personal_r_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
