import reflex as rx
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.categoria_personal import CategoriaPersonal


class CategoriaPersonalState(rx.State):
    categorias: list[CategoriaPersonal] = []
    
    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    
    add_modal_open: bool = False
    add_nombre: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_categoria()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_categoria()
            self.close_edit_dialog()

    def cargar_categorias(self):
        try:
            with rx.session() as session:
                query = select(CategoriaPersonal)
                results = session.exec(query).all()
                self.categorias = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar categorías: {e}")

    def delete_categoria(self, categoria_id: int):
        try:
            with rx.session() as session:
                record = session.exec(select(CategoriaPersonal).where(CategoriaPersonal.id == categoria_id)).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_categorias()
        except Exception as e:
            print(f"Error al eliminar la categoría: {e}")

    def open_edit_dialog(self, categoria_id: int):
        self.edit_id = categoria_id
        with rx.session() as session:
            record = session.exec(select(CategoriaPersonal).where(CategoriaPersonal.id == categoria_id)).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_categoria(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(select(CategoriaPersonal).where(CategoriaPersonal.id == self.edit_id)).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_categorias()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_categoria(self):
        try:
            with rx.session() as session:
                nueva_categoria = CategoriaPersonal(nombre=self.add_nombre)
                session.add(nueva_categoria)
                session.commit()
            self.cargar_categorias()
        except Exception as e:
            print(f"Error al crear categoría: {e}")
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
def editar_categoria(item: CategoriaPersonal) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar", on_click=lambda: CategoriaPersonalState.open_edit_dialog(item.id))
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Categoría Personal"),
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
                    on_change=lambda val: CategoriaPersonalState.set_edit_nombre(val),
                    on_key_down=CategoriaPersonalState.handle_key_edit,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=CategoriaPersonalState.update_categoria)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=CategoriaPersonalState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_categoria(item: CategoriaPersonal) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Categoría: {item.nombre}"),
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
                        on_click=lambda: CategoriaPersonalState.delete_categoria(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_categoria() -> rx.Component:
    CategoriaPersonalState.add_nombre = ""
    
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Categoría Personal"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text("Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.input(
                    value=CategoriaPersonalState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=CategoriaPersonalState.set_add_nombre,
                    on_key_down=CategoriaPersonalState.handle_key_add,
                    autofocus=True,
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=CategoriaPersonalState.create_categoria)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=CategoriaPersonalState.add_modal_open,
        ),
    )


@rx.event
def lista_categorias() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_categoria()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    CategoriaPersonalState.categorias,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_categoria(item),
                                eliminar_categoria(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=CategoriaPersonalState.cargar_categorias,
    )


@template(route="/p/categoria_personal", title="Categoría Personal", on_load=ProtectedState.on_load)
def categoria_personal_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Categoría Personal", size="8"),
        lista_categorias(),
        padding="4",
        spacing="4",
        width="100%",
    )
