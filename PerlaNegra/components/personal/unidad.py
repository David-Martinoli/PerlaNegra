import reflex as rx
from datetime import datetime
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.unidad import Unidad


class UnidadState(rx.State):
    unidades: list[Unidad] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_unidad()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_unidad()
            self.close_edit_dialog()

    def cargar_unidades(self):
        try:
            with rx.session() as session:
                query = select(Unidad)
                results = session.exec(query).all()
                self.unidades = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar unidades: {e}")

    def delete_unidad(self, unidad_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(Unidad).where(Unidad.id == unidad_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_unidades()
        except Exception as e:
            print(f"Error al eliminar la unidad: {e}")

    def open_edit_dialog(self, unidad_id: int):
        self.edit_id = unidad_id
        with rx.session() as session:
            record = session.exec(select(Unidad).where(Unidad.id == unidad_id)).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_unidad(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(Unidad).where(Unidad.id == self.edit_id)
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_unidades()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_unidad(self):
        try:
            with rx.session() as session:
                nueva_unidad = Unidad(nombre=self.add_nombre, created_at=datetime.now())
                session.add(nueva_unidad)
                session.commit()
            self.cargar_unidades()
        except Exception as e:
            print(f"Error al crear unidad: {e}")
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
def editar_unidad(item: Unidad) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar", on_click=lambda: UnidadState.open_edit_dialog(item.id))
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Unidad"),
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
                    on_change=lambda val: UnidadState.set_edit_nombre(val),
                    on_key_down=UnidadState.handle_key_edit,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", on_click=UnidadState.update_unidad)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=UnidadState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_unidad(item: Unidad) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Unidad: {item.nombre}"),
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
                        on_click=lambda: UnidadState.delete_unidad(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_unidad() -> rx.Component:
    UnidadState.add_nombre = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Unidad"),
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
                    value=UnidadState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=UnidadState.set_add_nombre,
                    on_key_down=UnidadState.handle_key_add,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", on_click=UnidadState.create_unidad)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=UnidadState.add_modal_open,
        ),
    )


@rx.event
def lista_unidades() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_unidad()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    UnidadState.unidades,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_unidad(item),
                                eliminar_unidad(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=UnidadState.cargar_unidades,
    )


@template(route="/p/unidad", title="Unidad", on_load=ProtectedState.on_load)
def unidad_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Unidades", size="8"),
        lista_unidades(),
        padding="4",
        spacing="4",
        width="100%",
    )
