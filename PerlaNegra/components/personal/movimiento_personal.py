import reflex as rx
from datetime import datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.movimiento_personal import MovimientoPersonal


class MovimientoPersonalState(rx.State):
    # Estado inicial
    personal_id: int | None = 0
    compania_id: int | None = 0
    seccion_id: int | None = 0
    fecha_inicio: datetime = datetime.now()
    fecha_fin: datetime = datetime.now()
    motivo: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def movimiento_personal_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Movimiento Personal", size="2", mb=4),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("ID Compañía"),
                rx.input(name="compania_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("ID Sección"),
                rx.input(name="seccion_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Fecha de Inicio"),
                rx.input(
                    type_="datetime-local",
                    name="fecha_inicio",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha de Fin"),
                rx.input(
                    type_="datetime-local",
                    name="fecha_fin",
                    default_value=datetime.now().strftime("%Y-%m-%dT%H:%M"),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Motivo"),
                rx.text_area(
                    placeholder="Ingrese el motivo del movimiento",
                    name="motivo",
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
                "Guardar Movimiento Personal",
                type_="submit",
                width="100%",
                bg="blue.500",
                color="white",
                mt=4,
            ),
            spacing="4",
            width="100%",
            max_width="800px",
        ),
        on_submit=MovimientoPersonalState.handle_submit,
    )


@template(
    route="/p/movimiento_personal",
    title="Movimiento Personal",
    on_load=ProtectedState.on_load,
)
def movimiento_personal_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            movimiento_personal_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
