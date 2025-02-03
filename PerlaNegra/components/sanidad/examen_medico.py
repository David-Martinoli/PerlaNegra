import reflex as rx
from typing import Callable


class ExamenMedicoState(rx.State):
    peso: float = 0.0
    talla: float = 0.0
    imc: float = 0.0

    def hre_hacer_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        # Aquí procesas los datos del formulario
        print("Datos recibidos:", form_data)
        # Implementar la lógica para guardar en la base de datos

    def calcular_imc(self):
        if self.talla > 0 and self.peso > 0:
            self.imc = round(self.peso / (self.talla * self.talla), 2)

    def handle_peso_change(self, value: str):
        try:
            self.peso = float(value)
            self.calcular_imc()
        except ValueError:
            pass

    def handle_talla_change(self, value: str):
        try:
            self.talla = float(value)
            self.calcular_imc()
        except ValueError:
            pass


def examen_medico_form(on_submit: Callable) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Examen Médico", size="3"),
            rx.box(
                rx.vstack(
                    rx.heading("Medidas Corporales", size="3"),
                    rx.form(
                        rx.text("Peso (kg)"),
                        rx.input(
                            name="peso",
                            on_change=ExamenMedicoState.handle_peso_change,
                            placeholder="Ingrese el peso",
                            min_="0",
                            step="0.1",
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.text("Talla (m)"),
                        rx.input(
                            name="talla",
                            on_change=ExamenMedicoState.handle_talla_change,
                            placeholder="Ingrese la talla en metros",
                            min_="0",
                            step="0.01",
                            required=True,
                        ),
                    ),
                    rx.form(
                        rx.text("IMC"),
                        rx.text(
                            ExamenMedicoState.imc, color="blue.500", font_weight="bold"
                        ),
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            rx.button(
                "Guardar Examen Médico",
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
