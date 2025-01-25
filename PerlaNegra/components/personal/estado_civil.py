import reflex as rx

from sqlmodel import select, Date, DateTime
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.estado_civil import EstadoCivil


class EstadoCivilState(rx.State):
    estados: list[EstadoCivil] = []

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)
        # Aquí iría la lógica para guardar en BD

    def cargar_estado_civil(self):
        try:
            with rx.session() as session:
                query = select(EstadoCivil)
                results = session.exec(query).all()
                self.estados = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar estados civiles: {e}")

    def delete_estado_civil(self, estado_id: int):
        try:
            with rx.session() as session:
                record = session.exec(select(EstadoCivil).where(EstadoCivil.id == estado_id)).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_estado_civil()
        except Exception as e:
            print(f"Error al eliminar el estado civil: {e}")


@rx.event
def lista_estado_civil() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                # rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Nombre"),
                # rx.table.column_header_cell("Creado"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(
                EstadoCivilState.estados,
                lambda item: rx.table.row(
                    rx.table.cell(item.nombre),
                    rx.table.cell(
                        rx.hstack(
                            rx.button("Editar", bg="blue.500", color="white"),
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button("Eliminar", bg="red.500", color="white"),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Eliminar Estado Civil"),
                                    rx.alert_dialog.description(
                                        "¿Está seguro que desea eliminar este registro? Esta acción es permanente.",
                                        size="2",
                                    ),
                                    rx.flex(
                                        rx.alert_dialog.cancel(
                                            rx.button(
                                                "Cancelar",
                                                variant="soft",
                                                color_scheme="gray",
                                            )
                                        ),
                                        rx.alert_dialog.action(
                                            rx.button(
                                                "Eliminar",
                                                color_scheme="red",
                                                on_click=lambda: EstadoCivilState.delete_estado_civil(item.id),
                                            )
                                        ),
                                        spacing="3",
                                        justify="end",
                                    ),
                                    style={"max_width": 500},
                                ),
                            ),
                            spacing="2",
                        ),
                    ),
                ),
            )
        ),
        # rx.table.body(rx.foreach(EstadoCivilState.estados)),
        on_mount=EstadoCivilState.cargar_estado_civil,
        variant="surface",
    )


@rx.event
def estado_civil_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Estado Civil", size="2", mb=4),
            rx.text("Nombre"),
            rx.input(name="nombre", placeholder="Ingrese el nombre del estado civil"),
            rx.button(
                "Guardar Estado Civil",
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
        on_submit=EstadoCivilState.handle_submit,
        is_required=True,
    )


@template(
    route="/p/estado_civil",
    title="Estado Civil",
    on_load=ProtectedState.on_load,
)
def estado_civil_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            lista_estado_civil(),
            estado_civil_form(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
