import reflex as rx
from typing import Callable


class PruebaHemogramaState(rx.State):
    def handle_submit(self, form_data: dict):
        print("Datos del hemograma:", form_data)
        # Implementar lógica de guardado


def prueba_hemograma_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Prueba de Hemograma", size="3"),
            # Grupo: Glóbulos y Hematocrito
            rx.box(
                rx.vstack(
                    rx.heading("Glóbulos y Hematocrito", size="3"),
                    rx.form(
                        rx.text("Glóbulos Rojos"),
                        rx.input(name="globulos_rojos", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("Hematocritos"),
                        rx.input(name="hematocritos", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("Hemoglobina (Hb)"),
                        rx.input(name="hb", min_="0", required=True),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Índices Hematimétricos
            rx.box(
                rx.vstack(
                    rx.heading("Índices Hematimétricos", size="3"),
                    rx.form(
                        rx.text("VCM"),
                        rx.input(name="vcm", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("HCM"),
                        rx.input(name="hcm", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("CHCM"),
                        rx.input(name="chcm", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("RDW"),
                        rx.input(name="rdw", min_="0", required=True),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Plaquetas y Glóbulos Blancos
            rx.box(
                rx.vstack(
                    rx.heading("Plaquetas y Glóbulos Blancos", size="3"),
                    rx.form(
                        rx.text("Plaquetas"),
                        rx.input(name="plaquetas", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("Glóbulos Blancos"),
                        rx.input(name="globulos_blancos", min_="0", required=True),
                    ),
                    rx.form(
                        rx.text("Fórmula"),
                        rx.text_area(name="formula", placeholder="Ingrese la fórmula"),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            rx.button(
                "Guardar Hemograma",
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
