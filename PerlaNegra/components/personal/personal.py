import reflex as rx
from datetime import date
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.personal import Personal


class PersonalState(rx.State):
    # Estado inicial
    personalR_id: int | None = 0
    personalS_id: int | None = 0
    # fecha_creacion: date = date.today()

    usuarios: list[Personal] = []

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en

        self.cargar_personal()

    def cargar_personal(self):
        with rx.session() as session:
            query = select(Personal)
            results = session.exec(query).all()
            self.usuarios = results


def mostrar_personal(item: Personal) -> rx.Component:
    """Renderiza una fila de la tabla para un registro de Personal."""
    # if item.created_at:
    #    fecha_str = item.created_at.strftime("%Y-%m-%d %H:%M:%S")
    # else:
    #    fecha_str = "N/A"

    return rx.table.row(
        rx.table.cell(str(item.personalR_id)),
        rx.table.cell(str(item.personalS_id)),
        # rx.table.cell(str(item.created_at)),
    )


@rx.event
def personal_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Información Personal", size="2", mb=4),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("ID Personal R"),
                        rx.table.column_header_cell("ID Personal S"),
                        rx.table.column_header_cell("Fecha de Creación"),
                    ),
                ),
                rx.table.body(rx.foreach(PersonalState.usuarios, mostrar_personal)),
                on_mount=PersonalState.cargar_personal,
                variant="surface",
                size="3",
                overflow_y="auto",
                max_height="60vh",
            ),
            rx.heading("Información Personal", size="2", mb=4),
            rx.form(
                rx.text("ID Personal R"),
                rx.input(name="personalR_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("ID Personal S"),
                rx.input(name="personalS_id", min_=0),
                is_required=True,
            ),
            rx.form(
                rx.text("Fecha de Creación"),
                rx.input(
                    type_="date",
                    name="fecha_creacion",
                    default_value=date.today().isoformat(),
                ),
                is_required=True,
            ),
            rx.button(
                "Guardar Información Personal",
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
        on_submit=PersonalState.handle_submit,
    )


@template(
    route="/p/personal",
    title="Información Personal",
    on_load=ProtectedState.on_load,
)
def personal_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            personal_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
