import reflex as rx
from datetime import datetime
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.sanidad.enfermedad import Enfermedad


class EnfermedadState(rx.State):
    enfermedades: list[Enfermedad] = []
    
    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    edit_observacion: str = ""
    
    add_modal_open: bool = False
    add_nombre: str = ""
    add_observacion: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_enfermedad()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_enfermedad()
            self.close_edit_dialog()

    def cargar_enfermedades(self):
        try:
            with rx.session() as session:
                query = select(Enfermedad)
                results = session.exec(query).all()
                self.enfermedades = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar enfermedades: {e}")

    def delete_enfermedad(self, enfermedad_id: int):
        try:
            with rx.session() as session:
                record = session.exec(select(Enfermedad).where(Enfermedad.id == enfermedad_id)).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_enfermedades()
        except Exception as e:
            print(f"Error al eliminar la enfermedad: {e}")

    def open_edit_dialog(self, enfermedad_id: int):
        self.edit_id = enfermedad_id
        with rx.session() as session:
            record = session.exec(select(Enfermedad).where(Enfermedad.id == enfermedad_id)).first()
            if record:
                self.edit_nombre = record.nombre
                self.edit_observacion = record.observacion
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_enfermedad(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(select(Enfermedad).where(Enfermedad.id == self.edit_id)).first()
                    if record:
                        record.nombre = self.edit_nombre
                        record.observacion = self.edit_observacion
                        session.add(record)
                        session.commit()
                self.cargar_enfermedades()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_enfermedad(self):
        try:
            with rx.session() as session:
                nueva_enfermedad = Enfermedad(
                    nombre=self.add_nombre,
                    observacion=self.add_observacion
                )
                session.add(nueva_enfermedad)
                session.commit()
            self.cargar_enfermedades()
        except Exception as e:
            print(f"Error al crear enfermedad: {e}")
        self.close_add_dialog()

    def close_add_dialog(self):
        self.add_modal_open = False

    @rx.event
    def set_edit_nombre(self, value: str):
        self.edit_nombre = value

    @rx.event
    def set_edit_observacion(self, value: str):
        self.edit_observacion = value

    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value

    @rx.event
    def set_add_observacion(self, value: str):
        self.add_observacion = value


@rx.event
def editar_enfermedad(item: Enfermedad) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar", on_click=lambda: EnfermedadState.open_edit_dialog(item.id))
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Enfermedad"),
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
                    on_change=lambda val: EnfermedadState.set_edit_nombre(val),
                    on_key_down=EnfermedadState.handle_key_edit,
                    autofocus=True,
                ),
                rx.text("Observación", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.text_area(
                    default_value=item.observacion,
                    placeholder="Ingrese la observación",
                    on_change=lambda val: EnfermedadState.set_edit_observacion(val),
                    min_height="100px",
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=EnfermedadState.update_enfermedad)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=EnfermedadState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_enfermedad(item: Enfermedad) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Enfermedad: {item.nombre}"),
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
                        on_click=lambda: EnfermedadState.delete_enfermedad(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_enfermedad() -> rx.Component:
    EnfermedadState.add_nombre = ""
    EnfermedadState.add_observacion = ""
    
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Enfermedad"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text("Nombre", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.input(
                    value=EnfermedadState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=EnfermedadState.set_add_nombre,
                    on_key_down=EnfermedadState.handle_key_add,
                    autofocus=True,
                ),
                rx.text("Observación", as_="div", size="2", margin_bottom="4px", weight="bold"),
                rx.text_area(
                    value=EnfermedadState.add_observacion,
                    placeholder="Ingrese la observación",
                    on_change=EnfermedadState.set_add_observacion,
                    min_height="100px",
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(rx.button("Cancelar", color_scheme="gray", variant="soft")),
                rx.dialog.close(rx.button("Guardar", on_click=EnfermedadState.create_enfermedad)),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=EnfermedadState.add_modal_open,
        ),
    )


@rx.event
def lista_enfermedades() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Observación"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_enfermedad()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    EnfermedadState.enfermedades,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(item.observacion),
                        rx.table.cell(
                            rx.hstack(
                                editar_enfermedad(item),
                                eliminar_enfermedad(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=EnfermedadState.cargar_enfermedades,
    )


@template(route="/p/enfermedad", title="Enfermedad", on_load=ProtectedState.on_load)
def enfermedad_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Enfermedades", size="8"),
        lista_enfermedades(),
        padding="4",
        spacing="4",
        width="100%",
    )
