import reflex as rx
from datetime import datetime
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.sanidad.ergometria import Ergometria


class ErgometriaState(rx.State):
    ergometrias: list[Ergometria] = []
    
    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    
    add_modal_open: bool = False
    add_nombre: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_ergometria()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_ergometria()
            self.close_edit_dialog()

    def cargar_ergometrias(self):
        try:
            with rx.session() as session:
                query = select(Ergometria)
                results = session.exec(query).all()
                self.ergometrias = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar ergometrías: {e}")

    def delete_ergometria(self, ergometria_id: int):
        try:
            with rx.session() as session:
                record = session.exec(select(Ergometria).where(Ergometria.id == ergometria_id)).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_ergometrias()
        except Exception as e:
            print(f"Error al eliminar la ergometría: {e}")

    def open_edit_dialog(self, ergometria_id: int):
        self.edit_id = ergometria_id
        with rx.session() as session:
            record = session.exec(select(Ergometria).where(Ergometria.id == ergometria_id)).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_ergometria(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(select(Ergometria).where(Ergometria.id == self.edit_id)).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_ergometrias()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_ergometria(self):
        try:
            with rx.session() as session:
                nueva_ergometria = Ergometria(nombre=self.add_nombre)
                session.add(nueva_ergometria)
                session.commit()
            self.cargar_ergometrias()
        except Exception as e:
            print(f"Error al crear ergometría: {e}")
        self.close_add_dialog()

    def close_add_dialog(self):
        self.add_modal_open = False

    @rx.event
    def set_edit_nombre(self, value: str):
        self.edit_nombre = value

    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value


@rx.event
def editar_ergometria(item: Ergometria) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar", on_click=lambda: ErgometriaState.open_edit_dialog(item.id))
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Ergometría"),
            rx.dialog.description(
                "Modifique el registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text("Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.input(
                    default_value=item.nombre,
                    placeholder="Ingrese el nombre",
                    on_change=lambda val: ErgometriaState.set_edit_nombre(val),
                    on_key_down=ErgometriaState.handle_key_edit,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=ErgometriaState.update_ergometria)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=ErgometriaState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_ergometria(item: Ergometria) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Ergometría: {item.nombre}"),
            rx.alert_dialog.description(
                "¿Está seguro que desea eliminar este registro? Esta acción es permanente.",
                size="2",
            ),
            rx.flex(
                rx.alert_dialog.cancel(rx.button("Cancelar", variant="soft", color_scheme="gray")),
                rx.alert_dialog.action(
                    rx.button(
                        "Eliminar",
                        color_scheme="red",
                        on_click=lambda: ErgometriaState.delete_ergometria(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_ergometria() -> rx.Component:
    ErgometriaState.add_nombre = ""
    
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Ergometría"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text("Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.input(
                    value=ErgometriaState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=ErgometriaState.set_add_nombre,
                    on_key_down=ErgometriaState.handle_key_add,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=ErgometriaState.create_ergometria)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=ErgometriaState.add_modal_open,
        ),
    )


@rx.event
def lista_ergometrias() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_ergometria()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    ErgometriaState.ergometrias,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_ergometria(item),
                                eliminar_ergometria(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=ErgometriaState.cargar_ergometrias,
    )


@template(route="/p/ergometria", title="Ergometría", on_load=ProtectedState.on_load)
def ergometria_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Ergometrías", size="8"),
        lista_ergometrias(),
        padding="4",
        spacing="4",
        width="100%",
    )
