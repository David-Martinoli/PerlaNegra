import reflex as rx
from typing import Callable
from datetime import date


class OdontologicoState(rx.State):
    def handle_submit(self, form_data: dict):
        print("Datos odontológicos:", form_data)
        # Implementar lógica de guardado


def odontologico_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            # Encabezado
            rx.heading("Examen Odontológico", size="3"),
            # Grupo: Examen General
            rx.box(
                rx.vstack(
                    rx.heading("Examen Dental", size="3"),
                    rx.form(
                        rx.text("Examen Odontológico"),
                        rx.text_area(
                            name="examen_odontologico",
                            placeholder="Detalle del examen odontológico",
                            min_height="150px",
                            required=True,
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Observaciones
            rx.box(
                rx.vstack(
                    rx.heading("Observaciones", size="3"),
                    rx.form(
                        rx.text("Observaciones Odontológicas"),
                        rx.text_area(
                            name="observacion_odontologica",
                            placeholder="Observaciones adicionales",
                            min_height="150px",
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Fecha
            rx.box(
                rx.vstack(
                    rx.form(
                        rx.text("Fecha del Odontograma"),
                        rx.input(
                            type_="date",
                            name="fecha_odontograma",
                            default_value=date.today().isoformat(),
                            required=True,
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Botón de envío
            rx.button(
                "Guardar Examen Odontológico",
                type_="submit",
                width="100%",
                colorScheme="blue",
            ),
            spacing="4",
            width="100%",
            padding="4",
        ),
        on_submit=on_submit,
        reset_on_submit=True,
    )
