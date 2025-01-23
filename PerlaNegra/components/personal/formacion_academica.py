import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.formacion_academica import FormacionAcademica


class FormacionAcademicaState(rx.State):
    # Estado inicial
    nombre_titulo: str = ""
    descripcion: str = ""
    fecha_egreso: date = date.today()
    personal_id: int = 0
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def formacion_academica_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Formación Académica", size="2", mb=4),
            rx.form(
                rx.text("Nombre del Título"),
                rx.input(
                    name="nombre_titulo", placeholder="Ingrese el nombre del título"
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Descripción"),
                rx.text_area(
                    placeholder="Ingrese la descripción",
                    name="descripcion",
                    min_height="100px",
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Egreso"),
                rx.input(
                    type_="date",
                    name="fecha_egreso",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
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
                "Guardar Formación Académica",
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
        on_submit=FormacionAcademicaState.handle_submit,
    )


@template(
    route="/p/formacion_academica",
    title="Formación Académica",
    on_load=ProtectedState.on_load,
)
def formacion_academica_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            formacion_academica_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
