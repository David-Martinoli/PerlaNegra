import reflex as rx
from typing import Callable


class EscaneoAnexoState(rx.State):
    """Estado para manejar el formulario de escaneo anexo."""

    archivo_seleccionado: str = ""

    def handle_file_change(self, file: str):
        self.archivo_seleccionado = file


@rx.event
def escaneo_anexo_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            # Encabezado
            rx.heading("Escaneo Anexo", size="3"),
            # Formulario principal
            rx.box(
                rx.vstack(
                    rx.heading("Subir Archivo", size="3"),
                    rx.form(
                        rx.form("Nombre del Archivo"),
                        rx.input(
                            placeholder="Nombre del archivo",
                            name="nombre_archivo",
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.form("Seleccionar Archivo"),
                        rx.upload(
                            rx.text(
                                "Arrastre un archivo o haga click para seleccionar"
                            ),
                            name="archivo",
                            multiple=True,
                            accept={
                                "application/pdf": [".pdf"],
                                "image/*": [".png", ".jpg", ".jpeg"],
                            },
                            # on_change=EscaneoAnexoState.handle_file_change,
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Botón de envío
            rx.button(
                "Guardar Anexo",
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
