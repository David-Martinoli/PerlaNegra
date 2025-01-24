import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.actuacion_disciplinaria_scan import (
    ActuacionDisciplinariaScan,
)


class ActuacionDisciplinariaScanState(rx.State):
    # Estado inicial
    imagen: str = ""
    descripcion: str = ""
    actuacion_disciplinaria_id: int | None | None = 0
    fecha_creacion: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def actuacion_disciplinaria_scan_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Actuación Disciplinaria Scan", size="2", mb=4),
            rx.form(
                rx.text("Imagen"),
                rx.input(name="imagen", placeholder="Ingrese la URL de la imagen"),
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
                rx.text("ID Actuación Disciplinaria"),
                rx.input(name="actuacion_disciplinaria_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="fecha_creacion",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Actuación Disciplinaria",
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
        on_submit=ActuacionDisciplinariaScanState.handle_submit,
    )


@template(
    route="/p/actuacion_disciplinaria_scan",
    title="Actuación Disciplinaria Scan",
    on_load=ProtectedState.on_load,
)
def actuacion_disciplinaria_scan_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            actuacion_disciplinaria_scan_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
