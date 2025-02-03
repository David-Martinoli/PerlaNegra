import reflex as rx

from sqlmodel import select, Date, DateTime
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.estado_civil import EstadoCivil


class EstadoCivilState(rx.State):
    estados: list[EstadoCivil] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""

    delete_modal_open: bool = False

    def handle_key_add(self, key: str):
        """Maneja teclas en el modal de agregar."""
        if key == "Enter":
            self.create_estado_civil()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        """Maneja teclas en el modal de editar."""
        if key == "Enter":
            self.update_estado_civil()
            self.close_edit_dialog()

    def handle_submit(self, form_data: dict):
        """Procesa el envío del formulario."""
        print("Datos del formulario:", form_data)

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
                record = session.exec(
                    select(EstadoCivil).where(EstadoCivil.id == estado_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_estado_civil()
        except Exception as e:
            print(f"Error al eliminar el estado civil: {e}")

    def open_edit_dialog(self, estado_id: int):
        self.edit_id = estado_id
        with rx.session() as session:
            record = session.exec(
                select(EstadoCivil).where(EstadoCivil.id == estado_id)
            ).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_estado_civil(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(EstadoCivil).where(EstadoCivil.id == self.edit_id)
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_estado_civil()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def open_add_dialog(self):
        self.add_modal_open = True
        self.add_nombre = ""

    def close_add_dialog(self):
        self.add_modal_open = False

    def close_delete_dialog(self):
        self.delete_modal_open = False

    def create_estado_civil(self):
        try:
            with rx.session() as session:
                nuevo_estado = EstadoCivil(nombre=self.add_nombre)
                session.add(nuevo_estado)
                session.commit()
            self.cargar_estado_civil()
        except Exception as e:
            print(f"Error al crear estado civil: {e}")
        self.close_add_dialog()

    @rx.event
    def set_edit_nombre(self, value: str):
        self.edit_nombre = value

    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value


@rx.event
def editar_estado_civil(item: EstadoCivil) -> rx.Component:
    return (
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "Editar",
                    on_click=lambda: EstadoCivilState.open_edit_dialog(item.id),
                )
            ),
            rx.dialog.content(
                rx.dialog.title("Editar Estado Civil"),
                rx.dialog.description(
                    "Modifique el registro.",
                    size="2",
                    margin_bottom="16px",
                ),
                rx.flex(
                    rx.text(
                        "Nombre",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.input(
                        default_value=item.nombre,
                        placeholder="Ingrese el nombre",
                        on_change=lambda val: EstadoCivilState.set_edit_nombre(val),
                        on_key_down=EstadoCivilState.handle_key_edit,
                        autofocus=True,  # Enfocar automáticamente el input
                    ),
                    direction="column",
                    spacing="3",
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            color_scheme="gray",
                            variant="soft",
                        )
                    ),
                    rx.dialog.close(
                        rx.button(
                            "Guardar",
                            on_click=EstadoCivilState.update_estado_civil,
                        )
                    ),
                    
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
                is_open=EstadoCivilState.edit_modal_open,
            ),
        ),
    )


@rx.event
def eliminar_estado_civil(item: EstadoCivil) -> rx.Component:
    return (
        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button("Eliminar", bg="red.500", color="white"),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title(f"Eliminar Estado Civil: {item.nombre}"),
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
                            on_click=lambda: EstadoCivilState.delete_estado_civil(
                                item.id
                            ),
                        )
                    ),
                    spacing="3",
                    justify="end",
                ),
                style={"max_width": 500},
            ),
        ),
    )


@rx.event
def agregar_estado_civil() -> rx.Component:
    EstadoCivilState.add_nombre = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Estado Civil"),
            rx.dialog.description(
                "Ingrese los datos del nuevo registro.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Nombre",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    value=EstadoCivilState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=EstadoCivilState.set_add_nombre,
                    on_key_down=EstadoCivilState.handle_key_add,
                    autofocus=True,  # Enfocar automáticamente el input
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        color_scheme="gray",
                        variant="soft",
                    )
                ),
                rx.dialog.close(
                    rx.button(
                        "Guardar",
                        on_click=EstadoCivilState.create_estado_civil,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=EstadoCivilState.add_modal_open,  # Control directo por estado
        ),
    )


@rx.event
def lista_estado_civil() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_estado_civil()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    EstadoCivilState.estados,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_estado_civil(item),
                                eliminar_estado_civil(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=EstadoCivilState.cargar_estado_civil,
    )


@template(
    route="/p/estado_civil",
    title="Estado Civil",
    on_load=ProtectedState.on_load,
)
def estado_civil_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Estado Civil", size="8"),
        lista_estado_civil(),
        padding="4",
        spacing="4",
        width="100%",
    )
