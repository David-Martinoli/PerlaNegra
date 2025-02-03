import reflex as rx
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.clase_formacion_academica import (
    ClaseFormacionAcademica,
)


class ClaseFormacionAcademicaState(rx.State):
    clases: list[ClaseFormacionAcademica] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_clase()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_clase()
            self.close_edit_dialog()

    def cargar_clases(self):
        try:
            with rx.session() as session:
                query = select(ClaseFormacionAcademica)
                results = session.exec(query).all()
                self.clases = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar clases: {e}")

    def delete_clase(self, clase_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(ClaseFormacionAcademica).where(
                        ClaseFormacionAcademica.id == clase_id
                    )
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_clases()
        except Exception as e:
            print(f"Error al eliminar la clase: {e}")

    def open_edit_dialog(self, clase_id: int):
        self.edit_id = clase_id
        with rx.session() as session:
            record = session.exec(
                select(ClaseFormacionAcademica).where(
                    ClaseFormacionAcademica.id == clase_id
                )
            ).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_clase(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(ClaseFormacionAcademica).where(
                            ClaseFormacionAcademica.id == self.edit_id
                        )
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_clases()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def close_add_dialog(self):
        self.add_modal_open = False

    def create_clase(self):
        try:
            with rx.session() as session:
                nueva_clase = ClaseFormacionAcademica(nombre=self.add_nombre)
                session.add(nueva_clase)
                session.commit()
            self.cargar_clases()
        except Exception as e:
            print(f"Error al crear clase: {e}")
        self.close_add_dialog()

    @rx.event
    def set_edit_nombre(self, value: str):
        self.edit_nombre = value

    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value


@rx.event
def editar_clase(item: ClaseFormacionAcademica) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: ClaseFormacionAcademicaState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Clase de Formación"),
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
                    on_change=lambda val: ClaseFormacionAcademicaState.set_edit_nombre(
                        val
                    ),
                    on_key_down=ClaseFormacionAcademicaState.handle_key_edit,
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
                    rx.button(
                        "Guardar", on_click=ClaseFormacionAcademicaState.update_clase
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=ClaseFormacionAcademicaState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_clase(item: ClaseFormacionAcademica) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Clase: {item.nombre}"),
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
                        on_click=lambda: ClaseFormacionAcademicaState.delete_clase(
                            item.id
                        ),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_clase() -> rx.Component:
    ClaseFormacionAcademicaState.add_nombre = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Clase de Formación"),
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
                    value=ClaseFormacionAcademicaState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=ClaseFormacionAcademicaState.set_add_nombre,
                    on_key_down=ClaseFormacionAcademicaState.handle_key_add,
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
                    rx.button(
                        "Guardar", on_click=ClaseFormacionAcademicaState.create_clase
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=ClaseFormacionAcademicaState.add_modal_open,
        ),
    )


@rx.event
def lista_clases() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_clase()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    ClaseFormacionAcademicaState.clases,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_clase(item),
                                eliminar_clase(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=ClaseFormacionAcademicaState.cargar_clases,
    )


@template(
    route="/p/clase_formacion_academica",
    title="Clase de Formación Académica",
    on_load=ProtectedState.on_load,
)
def clase_formacion_academica_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Clase de Formación Académica", size="8"),
        lista_clases(),
        padding="4",
        spacing="4",
        width="100%",
    )
