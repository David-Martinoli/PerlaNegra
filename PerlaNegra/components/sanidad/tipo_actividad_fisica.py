import reflex as rx
from typing import Callable


class TipoActividadFisicaState(rx.State):
    def handle_submit(self, form_data: dict):
        print("Datos actividad física:", form_data)
        # Implementar lógica de guardado


def tipo_actividad_fisica_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Tipo de Actividad Física", size="3"),
            rx.box(
                rx.vstack(
                    rx.form(
                        rx.text("Nombre de la Actividad"),
                        rx.input(
                            name="nombre",
                            placeholder="Ej: Natación, Fútbol, etc.",
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.text("Observaciones"),
                        rx.text_area(
                            name="observacion",
                            placeholder="Detalles adicionales sobre la actividad",
                            min_height="100px",
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            rx.button(
                "Guardar Actividad Física",
                type_="submit",
                width="100%",
                colorScheme="blue",
            ),
            spacing="4",
            width="100%",
            padding="4",
        ),
        on_submit=on_submit,
    )
