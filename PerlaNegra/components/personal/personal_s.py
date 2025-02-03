import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.personal_s import PersonalS


class PersonalSState(rx.State):
    # Estado inicial
    nombre: str = ""
    apellido: str = ""
    fecha_ingreso: date = date.today()
    fecha_ingreso_unidad: date = date.today()
    fecha_ultimo_ascenso: date = date.today()
    numero_legajo: str = ""
    categoria_personal_id: int | None = 0
    especialidad: str = ""
    grado: str = ""
    cuadro: str = ""
    en_campo: str = ""
    nou: str = ""
    funcion: str = ""
    clase_id: int | None = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def personal_s_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Movimiento Personal", size="2", mb=4),
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
                rx.text("Fecha de Ingreso"),
                rx.input(
                    type_="date",
                    name="fecha_ingreso",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Ingreso a Unidad"),
                rx.input(
                    type_="date",
                    name="fecha_ingreso_unidad",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Último Ascenso"),
                rx.input(
                    type_="date",
                    name="fecha_ultimo_ascenso",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Número de Legajo"),
                rx.input(
                    name="numero_legajo",
                    placeholder="Ingrese el número de legajo",
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("ID Categoría Personal"),
                rx.input(
                    name="categoria_personal_id",
                    type_="number",
                    min_=1,
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Especialidad"),
                rx.input(name="especialidad", placeholder="Ingrese la especialidad"),
            ),
            rx.form(
                rx.text("Grado"),
                rx.input(name="grado", placeholder="Ingrese el grado"),
            ),
            rx.form(
                rx.text("Cuadro"),
                rx.input(name="cuadro", placeholder="Ingrese el cuadro"),
            ),
            rx.form(
                rx.text("En Campo"),
                rx.input(name="en_campo", placeholder="Ingrese en campo"),
            ),
            rx.form(
                rx.text("NOU"),
                rx.input(name="nou", placeholder="Ingrese el NUE"),
            ),
            rx.form(
                rx.text("Función"),
                rx.input(name="funcion", placeholder="Ingrese la función"),
            ),
            rx.form(
                rx.text("ID Clase"),
                rx.input(name="clase_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="datetime-local",
                    name="created_at",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Actualización"),
                rx.input(
                    type_="datetime-local",
                    name="updated_at",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.button(
                "Guardar Movimiento Personal",
                type_="submit",
                width="100%",
                bg="blue.500",
                color="white",
                mt=4,
            ),
            spacing="4",
            width="100%",
            max_width="800px",
        ),
        on_submit=PersonalSState.handle_submit,
    )


@template(
    route="/p/personal_s",
    title="Movimiento Personal",
    on_load=ProtectedState.on_load,
)
def personal_s_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            personal_s_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
