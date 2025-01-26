import reflex as rx
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.sanidad.tipo_actividad_fisica import TipoActividadFisica


class TipoActividadFisicaState(rx.State):
    tipos: list[TipoActividadFisica] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    edit_observacion: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""
    add_observacion: str = ""

    delete_modal_open: bool = False

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_tipo()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_tipo()
            self.close_edit_dialog()

    def cargar_tipos(self):
        try:
            with rx.session() as session:
                query = select(TipoActividadFisica)
                results = session.exec(query).all()
                self.tipos = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar tipos: {e}")

    def delete_tipo(self, tipo_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(TipoActividadFisica).where(TipoActividadFisica.id == tipo_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_tipos()
        except Exception as e:
            print(f"Error al eliminar el tipo: {e}")

    def open_edit_dialog(self, tipo_id: int):
        self.edit_id = tipo_id
        with rx.session() as session:
            record = session.exec(
                select(TipoActividadFisica).where(TipoActividadFisica.id == tipo_id)
            ).first()
            if record:
                self.edit_nombre = record.nombre
                self.edit_observacion = record.observacion
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_tipo(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(TipoActividadFisica).where(
                            TipoActividadFisica.id == self.edit_id
                        )
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        record.observacion = self.edit_observacion
                        session.add(record)
                        session.commit()
                self.cargar_tipos()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def open_add_dialog(self):
        self.add_modal_open = True
        self.add_nombre = ""
        self.add_observacion = ""

    def close_add_dialog(self):
        self.add_modal_open = False

    def create_tipo(self):
        try:
            with rx.session() as session:
                nuevo_tipo = TipoActividadFisica(
                    nombre=self.add_nombre,
                    observacion=self.add_observacion,
                )
                session.add(nuevo_tipo)
                session.commit()
            self.cargar_tipos()
        except Exception as e:
            print(f"Error al crear tipo: {e}")
        self.close_add_dialog()

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
def editar_tipo(item: TipoActividadFisica) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: TipoActividadFisicaState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Tipo de Actividad Física"),
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
                    on_change=TipoActividadFisicaState.set_edit_nombre,
                    on_key_down=TipoActividadFisicaState.handle_key_edit,
                ),
                rx.text(
                    "Observación",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    default_value=item.observacion,
                    placeholder="Ingrese la observación",
                    on_change=TipoActividadFisicaState.set_edit_observacion,
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
                        "Guardar",
                        on_click=TipoActividadFisicaState.update_tipo,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=TipoActividadFisicaState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_tipo(item: TipoActividadFisica) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Tipo: {item.nombre}"),
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
                        on_click=lambda: TipoActividadFisicaState.delete_tipo(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )


@rx.event
def agregar_tipo() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Tipo de Actividad Física"),
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
                    value=TipoActividadFisicaState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=TipoActividadFisicaState.set_add_nombre,
                    on_key_down=TipoActividadFisicaState.handle_key_add,
                ),
                rx.text(
                    "Observación",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    value=TipoActividadFisicaState.add_observacion,
                    placeholder="Ingrese la observación",
                    on_change=TipoActividadFisicaState.set_add_observacion,
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
                        "Guardar",
                        on_click=TipoActividadFisicaState.create_tipo,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=TipoActividadFisicaState.add_modal_open,
        ),
    )


@rx.event
def lista_tipos() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Observación"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text("Acciones"),
                            agregar_tipo(),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    TipoActividadFisicaState.tipos,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(item.observacion),
                        rx.table.cell(
                            rx.hstack(
                                editar_tipo(item),
                                eliminar_tipo(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=TipoActividadFisicaState.cargar_tipos,
    )


@template(
    route="/s/tipo_actividad_fisica",
    title="Tipos de Actividad Física",
    on_load=ProtectedState.on_load,
)
def tipo_actividad_fisica_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Tipos de Actividad Física", size="8"),
        lista_tipos(),
        padding="4",
        spacing="4",
        width="100%",
    )
