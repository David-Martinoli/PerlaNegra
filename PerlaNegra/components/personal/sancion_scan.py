import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.sancion_scan import SancionScan


class SancionScanState(rx.State):
    # Estado inicial
    sancion_id: int = 0
    imagen: str = ""
    descripcion: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def sancion_scan_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Sanción Scan", size="2", mb=4),
            rx.form(
                rx.text("ID Sanción"),
                rx.input(name="sancion_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Imagen"),
                rx.input(
                    name="imagen",
                    placeholder="Ingrese la URL de la imagen",
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Descripción"),
                rx.text_area(
                    placeholder="Ingrese la descripción",
                    name="descripcion",
                    min_height="100px",
                    is_required=True,
                ),
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
            rx.button(
                "Guardar Sanción Scan",
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
        on_submit=SancionScanState.handle_submit,
    )


@template(
    route="/p/sancion_scan",
    title="Sanción Scan",
    on_load=ProtectedState.on_load,
)
def sancion_scan_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            sancion_scan_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
