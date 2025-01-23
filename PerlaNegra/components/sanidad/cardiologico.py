import reflex as rx
from datetime import date
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState


class CardiologicoState(rx.State):
    # Estado inicial
    ecg: str = ""
    ergometria_id: int = 0
    radiologia: str = ""
    otros: str = ""
    fecha: date = date.today()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def cardiologico_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Examen Cardiológico", size="2", mb=4),
            rx.form(
                rx.text("ECG"),
                rx.text_area(
                    placeholder="Ingrese resultados del ECG",
                    name="ecg",
                    min_height="100px",
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Ergometría"),
                rx.input(name="ergometria_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Radiología"),
                rx.text_area(
                    placeholder="Ingrese resultados radiológicos",
                    name="radiologia",
                    min_height="100px",
                ),
            ),
            rx.form(
                rx.text("Otros hallazgos"),
                rx.text_area(
                    placeholder="Ingrese otros hallazgos relevantes",
                    name="otros",
                    min_height="100px",
                ),
            ),
            rx.form(
                rx.text("Fecha"),
                rx.input(
                    type_="date",
                    name="fecha",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Examen Cardiológico",
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
        on_submit=CardiologicoState.handle_submit,
    )


@template(
    route="/s/cardiologico",
    title="Examen Cardiológico",
    on_load=ProtectedState.on_load,
)
def cardiologico_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            cardiologico_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
