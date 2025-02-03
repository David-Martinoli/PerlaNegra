import reflex as rx
from typing import Callable


class DeclaracionJuradaState(rx.State):
    medicacion_recetada: bool = False

    def toggle_medicacion(self):
        self.medicacion_recetada = not self.medicacion_recetada


@rx.event
def declaracion_jurada_form(on_submit: Callable) -> rx.Component:
    """Formulario para la Declaración Jurada de Sanidad.

    Args:
        on_submit: Función callback que se ejecuta al enviar el formulario
    """
    return rx.form(
        rx.vstack(
            # Datos generales
            rx.heading("Declaración Jurada de Sanidad", size="3"),
            # Grupo: Síntomas respiratorios y cardiovasculares
            rx.box(
                rx.vstack(
                    rx.heading("Síntomas Respiratorios y Cardiovasculares", size="3"),
                    rx.checkbox("Fatiga fácil", name="fatiga_facil"),
                    rx.checkbox("Falta de aire", name="falta_aire"),
                    rx.checkbox("Tos crónica", name="tos_cronica"),
                    rx.checkbox("Hipertensión", name="hipertension"),
                    rx.checkbox("Dolor en el pecho", name="dolor_pecho"),
                    rx.checkbox("Palpitaciones", name="palpitaciones"),
                    rx.checkbox("Edemas", name="edemas"),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Condiciones médicas generales
            rx.box(
                rx.vstack(
                    rx.heading("Condiciones Médicas", size="3"),
                    rx.checkbox("Anemia", name="anemia"),
                    rx.checkbox("Diabetes", name="diabetes"),
                    rx.checkbox("COVID-19", name="covid19"),
                    rx.checkbox(
                        "Medicación recetada",
                        name="medicacion_recetada",
                        on_change=DeclaracionJuradaState.toggle_medicacion,
                    ),
                    rx.text_area(
                        placeholder="Especifique medicación recetada",
                        name="texto_medicacion_recetada",
                        is_disabled=~DeclaracionJuradaState.medicacion_recetada,
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Síntomas y condiciones adicionales
            rx.box(
                rx.vstack(
                    rx.heading("Otros Síntomas", size="3"),
                    rx.checkbox("Sangrado anormal", name="sangrado_anormal"),
                    rx.checkbox("Hemorragias", name="hemorragias"),
                    rx.checkbox("Dolor abdominal", name="dolor_abdominal"),
                    rx.checkbox("Dolor al orinar", name="dolor_orinar"),
                    rx.checkbox("Esguinces", name="esguinces"),
                    rx.checkbox("Fracturas", name="fracturas"),
                    rx.checkbox("Lumbago", name="lumbago"),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Condiciones especiales
            rx.box(
                rx.vstack(
                    rx.heading("Condiciones Especiales", size="3"),
                    rx.checkbox("Cirugías", name="cirugias"),
                    rx.checkbox("Embarazo", name="embarazo"),
                    rx.checkbox("Internaciones", name="internaciones"),
                    rx.checkbox(
                        "Medicación no recetada", name="medicacion_no_recetada"
                    ),
                    rx.checkbox(
                        "Complicaciones en embarazo", name="complicaciones_embarazo"
                    ),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Grupo: Condiciones neurológicas/psicológicas
            rx.box(
                rx.vstack(
                    rx.heading("Condiciones Neurológicas", size="3"),
                    rx.checkbox("Cefaleas", name="cefaleas"),
                    rx.checkbox("Desmayos", name="desmayos"),
                    rx.checkbox("Epilepsia", name="epilepsia"),
                    rx.checkbox("Depresión", name="depresion"),
                    rx.checkbox("Vértigos", name="vertigos"),
                ),
                padding="4",
                border_width="1px",
                border_radius="md",
            ),
            # Botón de envío
            rx.button(
                "Enviar Declaración Jurada",
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
