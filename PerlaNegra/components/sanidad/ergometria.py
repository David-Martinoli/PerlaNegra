import reflex as rx
from typing import Callable


class ErgometriaState(rx.State):
    nombre: str = ""


@rx.event
def ergometria_form(on_submit: Callable) -> rx.Component:
    """Formulario para Ergometría.

    Args:
        on_submit: Función callback que se ejecuta al enviar el formulario
    """
    return rx.form(
        rx.vstack(
            # Encabezado
            rx.heading("Formulario de Ergometría", size="3"),
            # Datos de la ergometría
            rx.box(
                rx.vstack(
                    rx.heading("Datos de la Ergometría", size="3"),
                    rx.form(
                        rx.text("Nombre del Estudio"),
                        rx.input(
                            placeholder="Ingrese el nombre del estudio",
                            name="nombre",
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
                "Guardar Ergometría",
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
