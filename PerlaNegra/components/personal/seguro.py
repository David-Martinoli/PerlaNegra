import reflex as rx
from datetime import datetime
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.seguro import Seguro


class SeguroState(rx.State):
    seguros: list[Seguro] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    edit_descripcion: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""
    add_descripcion: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_seguro()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_seguro()
            self.close_edit_dialog()

    def cargar_seguros(self):
        try:
            with rx.session() as session:
                query = select(Seguro)
                results = session.exec(query).all()
                self.seguros = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar seguros: {e}")

    def delete_seguro(self, seguro_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(Seguro).where(Seguro.id == seguro_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_seguros()
        except Exception as e:
            print(f"Error al eliminar el seguro: {e}")

    def open_edit_dialog(self, seguro_id: int):
        self.edit_id = seguro_id
        with rx.session() as session:
            record = session.exec(select(Seguro).where(Seguro.id == seguro_id)).first()
            if record:
                self.edit_nombre = record.nombre
                self.edit_descripcion = record.descripcion
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_seguro(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(Seguro).where(Seguro.id == self.edit_id)
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        record.descripcion = self.edit_descripcion
                        session.add(record)
                        session.commit()
                self.cargar_seguros()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_seguro(self):
        try:
            with rx.session() as session:
                nuevo_seguro = Seguro(
                    nombre=self.add_nombre,
                    descripcion=self.add_descripcion,
                    created_at=datetime.now(),
                )
                session.add(nuevo_seguro)
                session.commit()
            self.cargar_seguros()
        except Exception as e:
            print(f"Error al crear seguro: {e}")
        self.close_add_dialog()

    def close_add_dialog(self):
        self.add_modal_open = False

    @rx.event
    def set_edit_nombre(self, value: str):
        self.edit_nombre = value

    @rx.event
    def set_edit_descripcion(self, value: str):
        self.edit_descripcion = value

    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value

    @rx.event
    def set_add_descripcion(self, value: str):
        self.add_descripcion = value


@rx.event
def editar_seguro(item: Seguro) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar", on_click=lambda: SeguroState.open_edit_dialog(item.id))
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Seguro"),
            rx.dialog.description(
                "Modifique el registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"
                ),
                rx.input(
                    default_value=item.nombre,
                    placeholder="Ingrese el nombre",
                    on_change=lambda val: SeguroState.set_edit_nombre(val),
                    on_key_down=SeguroState.handle_key_edit,
                    # autofocus=True,
                ),
                rx.text(
                    "Descripción",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    default_value=item.descripcion,
                    placeholder="Ingrese la descripción",
                    on_change=lambda val: SeguroState.set_edit_descripcion(val),
                    min_height="100px",
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", on_click=SeguroState.update_seguro)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=SeguroState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_seguro(item: Seguro) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Seguro: {item.nombre}"),
            rx.alert_dialog.description(
                "¿Está seguro que desea eliminar este registro? Esta acción es permanente.",
                size="2",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancelar", variant="soft", color_scheme="gray")
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Eliminar",
                        color_scheme="red",
                        on_click=lambda: SeguroState.delete_seguro(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_seguro() -> rx.Component:
    SeguroState.add_nombre = ""
    SeguroState.add_descripcion = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Seguro"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"
                ),
                rx.input(
                    value=SeguroState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=SeguroState.set_add_nombre,
                    on_key_down=SeguroState.handle_key_add,
                    # autofocus=True,
                ),
                rx.text(
                    "Descripción",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    value=SeguroState.add_descripcion,
                    placeholder="Ingrese la descripción",
                    on_change=SeguroState.set_add_descripcion,
                    min_height="100px",
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", on_click=SeguroState.create_seguro)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=SeguroState.add_modal_open,
        ),
    )


@rx.event
def lista_seguros() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Descripción"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_seguro()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    SeguroState.seguros,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(item.descripcion),
                        rx.table.cell(
                            rx.hstack(
                                editar_seguro(item),
                                eliminar_seguro(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=SeguroState.cargar_seguros,
    )


@template(route="/p/seguro", title="Seguro", on_load=ProtectedState.on_load)
def seguro_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Seguros", size="8"),
        lista_seguros(),
        padding="4",
        spacing="4",
        width="100%",
    )
