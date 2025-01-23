import reflex as rx
from datetime import date, datetime
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.felicitacion import Felicitacion


class FelicitacionState(rx.State):
    # Estado inicial
    quien_impone: int = 0
    fecha: date = date.today()
    causa: str = ""
    descripcion: str = ""
    imagen: str = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    personal_id: int = 0

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD


@rx.event
def felicitacion_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Felicitación", size="2", mb=4),
            rx.form(
                rx.text("ID Personal que Impones"),
                rx.input(name="quien_impone", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha"),
                rx.input(
                    type_="date",
                    name="fecha",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Causa"),
                rx.input(name="causa", placeholder="Ingrese la causa"),
                is_required=True,
            ),
            rx.form(
                rx.text("Descripción"),
                rx.text_area(
                    placeholder="Ingrese la descripción",
                    name="descripcion",
                    min_height="100px",
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Imagen"),
                rx.input(name="imagen", placeholder="Ingrese la URL de la imagen"),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal"),
                rx.input(name="personal_id", type_="number", min_=1),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="created_at",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                ),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Actualización"),
                rx.input(
                    type_="date",
                    name="updated_at",
                    default_value=datetime.now().strftime("%Y-%m-%d"),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Felicitación",
                type_="submit",
                width="100%",
                bg="blue.500",
                color="white",
                mt=4,
            ),
            spacing="4",
            width="100%",
            max_width="600px",
        ),
        on_submit=FelicitacionState.handle_submit,
    )


@template(
    route="/p/felicitacion",
    title="Felicitación",
    on_load=ProtectedState.on_load,
)
def felicitacion_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            felicitacion_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
