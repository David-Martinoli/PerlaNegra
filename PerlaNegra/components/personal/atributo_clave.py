import reflex as rx
from sqlmodel import select
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.atributo_clave import AtributoClave


class AtributoClaveState(rx.State):
    atributos: list[AtributoClave] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_clave: str = ""

    add_modal_open: bool = False
    add_clave: str = ""

    def cargar_atributos(self):
        try:
            with rx.session() as session:
                query = select(AtributoClave)
                results = session.exec(query).all()
                self.atributos = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar atributos clave: {e}")

    def delete_atributo(self, atributo_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(AtributoClave).where(AtributoClave.id == atributo_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_atributos()
        except Exception as e:
            print(f"Error al eliminar el atributo: {e}")

    def open_edit_dialog(self, atributo_id: int):
        self.edit_id = atributo_id
        with rx.session() as session:
            record = session.exec(
                select(AtributoClave).where(AtributoClave.id == atributo_id)
            ).first()
            if record:
                self.edit_clave = record.clave
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_atributo(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(AtributoClave).where(AtributoClave.id == self.edit_id)
                    ).first()
                    if record:
                        record.clave = self.edit_clave
                        session.add(record)
                        session.commit()
                self.cargar_atributos()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def open_add_dialog(self):
        self.add_modal_open = True
        self.add_clave = ""

    def close_add_dialog(self):
        self.add_modal_open = False

    def create_atributo(self):
        try:
            with rx.session() as session:
                nuevo_atributo = AtributoClave(clave=self.add_clave)
                session.add(nuevo_atributo)
                session.commit()
            self.cargar_atributos()
        except Exception as e:
            print(f"Error al crear atributo: {e}")
        self.close_add_dialog()

    @rx.event
    def set_edit_clave(self, value: str):
        self.edit_clave = value

    @rx.event
    def set_add_clave(self, value: str):
        self.add_clave = value


@rx.event
def editar_atributo(item: AtributoClave) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar", on_click=lambda: AtributoClaveState.open_edit_dialog(item.id)
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Atributo Clave"),
            rx.dialog.description(
                "Modifique el registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Clave", as_="div", size="2", margin_bottom="4px", weight="bold"
                ),
                rx.input(
                    default_value=item.clave,
                    placeholder="Ingrese el nombre del atributo",
                    on_change=lambda val: AtributoClaveState.set_edit_clave(val),
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
                    rx.button("Guardar", on_click=AtributoClaveState.update_atributo)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=AtributoClaveState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_atributo(item: AtributoClave) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Atributo Clave: {item.clave}"),
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
                        on_click=lambda: AtributoClaveState.delete_atributo(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_atributo() -> rx.Component:
    AtributoClaveState.add_clave = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Atributo Clave"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Clave", as_="div", size="2", margin_bottom="4px", weight="bold"
                ),
                rx.input(
                    value=AtributoClaveState.add_clave,
                    placeholder="Ingrese la clave",
                    on_change=AtributoClaveState.set_add_clave,
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
                    rx.button("Guardar", on_click=AtributoClaveState.create_atributo)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=AtributoClaveState.add_modal_open,
        ),
    )


@rx.event
def lista_atributos() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Clave"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_atributo()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    AtributoClaveState.atributos,
                    lambda item: rx.table.row(
                        rx.table.cell(item.clave),
                        rx.table.cell(
                            rx.hstack(
                                editar_atributo(item),
                                eliminar_atributo(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=AtributoClaveState.cargar_atributos,
    )


@template(
    route="/p/atributo_clave", title="Atributo Clave", on_load=ProtectedState.on_load
)
def atributo_clave_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Atributo Clave", size="8"),
        lista_atributos(),
        padding="4",
        spacing="4",
        width="100%",
    )
