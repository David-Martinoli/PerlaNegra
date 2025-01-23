import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.actuacion_scan import ActuacionScan


class ActuacionScanState(rx.State):
    # Estado inicial
    actuacion_id: int = 0
    imagen: str = ""
    descripcion: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def actuacion_scan_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Actuación Scan", size="2", mb=4),
            rx.form(
                rx.text("ID de Actuación"),
                rx.input(name="actuacion_id", type_="number", min_=1),
                is_required=True,
            ),
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
            rx.button(
                "Guardar Actuación Scan",
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
        on_submit=ActuacionScanState.handle_submit,
    )


@template(
    route="/p/actuacion_scan",
    title="Actuación Scan",
    on_load=ProtectedState.on_load,
)
def actuacion_scan_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            actuacion_scan_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
