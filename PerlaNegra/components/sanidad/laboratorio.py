import reflex as rx
from typing import Callable
from datetime import date


class LaboratorioState(rx.State):
    # Valores numéricos
    glucemia: float = 0.0
    uremia: float = 0.0
    colesterol_total: float = 0.0
    hdl_colesterol: float = 0.0
    ldl_colesterol: float = 0.0
    trigliceridos: float = 0.0

    def handle_submit(self, form_data: dict):
        print("Datos del laboratorio:", form_data)
        # Implementar lógica de guardado


def laboratorio_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Laboratorio", size="3"),
            # Grupo: Valores Sanguíneos
            rx.box(
                rx.vstack(
                    rx.heading("Valores Sanguíneos", size="3"),
                    rx.form(
                        rx.text("Glucemia"),
                        rx.input(name="glucemia", min_="0", step="0.01", required=True),
                    ),
                    rx.form(
                        rx.text("Uremia"),
                        rx.input(name="uremia", min_="0", step="0.01", required=True),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Perfil Lipídico
            rx.box(
                rx.vstack(
                    rx.heading("Perfil Lipídico", size="3"),
                    rx.form(
                        rx.text("Colesterol Total"),
                        rx.input(
                            name="colesterol_total",
                            min_="0",
                            step="0.01",
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.text("HDL Colesterol"),
                        rx.input(
                            name="hdl_colesterol", min_="0", step="0.01", required=True
                        ),
                    ),
                    rx.form(
                        rx.text("LDL Colesterol"),
                        rx.input(
                            name="ldl_colesterol", min_="0", step="0.01", required=True
                        ),
                    ),
                    rx.form(
                        rx.text("Triglicéridos"),
                        rx.input(
                            name="trigliceridos", min_="0", step="0.01", required=True
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Análisis Varios
            rx.box(
                rx.vstack(
                    rx.heading("Otros Análisis", size="3"),
                    rx.form(
                        rx.text("Eritrosedimentación"),
                        rx.input(name="eritrosedimentacion"),
                    ),
                    rx.form(
                        rx.text("HIV"),
                        rx.input(name="hiv"),
                    ),
                    rx.form(
                        rx.text("VDRL"),
                        rx.input(name="vdrl"),
                    ),
                    rx.form(
                        rx.text("Hepatograma"),
                        rx.text_area(name="hepatograma"),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Análisis de Orina y Toxicológico
            rx.box(
                rx.vstack(
                    rx.heading("Análisis Complementarios", size="3"),
                    rx.form(
                        rx.text("Orina Completa"),
                        rx.text_area(name="orina_completa_texto"),
                    ),
                    rx.form(
                        rx.text("Toxicológico"),
                        rx.text_area(name="toxicologico_texto"),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Fecha y Observaciones
            rx.box(
                rx.vstack(
                    rx.form(
                        rx.text("Fecha"),
                        rx.input(
                            type_="date",
                            name="fecha",
                            default_value=date.today().isoformat(),
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.text("Observaciones"),
                        rx.text_area(name="observaciones"),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            rx.button(
                "Guardar Laboratorio",
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
