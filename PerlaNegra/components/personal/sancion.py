import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.sancion import Sancion


class SancionState(rx.State):
    # Estado inicial
    motivo: str = ""
    tipo_sancion_id: int | None = 0
    fecha: date = date.today()
    personal_id: int | None = 0
    autoridad_id: int | None = 0
    fecha_comision: date = date.today()
    fecha_aplicacion: date = date.today()
    fecha_revision_jefe: date = date.today()
    fecha_recurso: date = date.today()
    dias_arresto: int = 0
    descripcion_reglamentaria: str = ""
    created_at: datetime = datetime.now()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def sancion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Sanción", size="2", mb=4),
            rx.form(
                rx.text("Motivo"),
                rx.input(
                    name="motivo", placeholder="Ingrese el motivo", is_required=True
                ),
            ),
            rx.form(
                rx.text("ID Tipo Sanción"),
                rx.input(
                    name="tipo_sancion_id", type_="number", min_=1, is_required=True
                ),
            ),
            rx.form(
                rx.text("Fecha"),
                rx.input(
                    type_="date",
                    name="fecha",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("ID Autoridad"),
                rx.input(name="autoridad_id", type_="number", min_=1, is_required=True),
            ),
            rx.form(
                rx.text("Fecha Comisión"),
                rx.input(
                    type_="date",
                    name="fecha_comision",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha Aplicación"),
                rx.input(
                    type_="date",
                    name="fecha_aplicacion",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha Revisión Jefe"),
                rx.input(
                    type_="date",
                    name="fecha_revision_jefe",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Fecha Recurso"),
                rx.input(
                    type_="date",
                    name="fecha_recurso",
                    default_value=date.today().isoformat(),
                    is_required=True,
                ),
            ),
            rx.form(
                rx.text("Días Arresto"),
                rx.input(name="dias_arresto", type_="number", min_=0, is_required=True),
            ),
            rx.form(
                rx.text("Descripción Reglamentaria"),
                rx.text_area(
                    placeholder="Ingrese la descripción reglamentaria",
                    name="descripcion_reglamentaria",
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
                "Guardar Sanción",
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
        on_submit=SancionState.handle_submit,
    )


@template(
    route="/p/sancion",
    title="Sanción",
    on_load=ProtectedState.on_load,
)
def sancion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            sancion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
