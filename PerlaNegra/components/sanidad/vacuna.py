import reflex as rx
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.sanidad.vacuna import Vacuna


class VacunaState(rx.State):
    vacunas: list[Vacuna] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""
    edit_descripcion: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""
    add_descripcion: str = ""

    delete_modal_open: bool = False

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_vacuna()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_vacuna()
            self.close_edit_dialog()

    def cargar_vacunas(self):
        try:
            with rx.session() as session:
                query = select(Vacuna)
                results = session.exec(query).all()
                self.vacunas = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar vacunas: {e}")

    def delete_vacuna(self, vacuna_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(Vacuna).where(Vacuna.id == vacuna_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_vacunas()
        except Exception as e:
            print(f"Error al eliminar la vacuna: {e}")

    def open_edit_dialog(self, vacuna_id: int):
        self.edit_id = vacuna_id
        with rx.session() as session:
            record = session.exec(
                select(Vacuna).where(Vacuna.id == vacuna_id)
            ).first()
            if record:
                self.edit_nombre = record.nombre
                self.edit_descripcion = record.descripcion
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_vacuna(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(Vacuna).where(Vacuna.id == self.edit_id)
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        record.descripcion = self.edit_descripcion
                        session.add(record)
                        session.commit()
                self.cargar_vacunas()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def open_add_dialog(self):
        self.add_modal_open = True
        self.add_nombre = ""
        self.add_descripcion = ""

    def close_add_dialog(self):
        self.add_modal_open = False

    def create_vacuna(self):
        try:
            with rx.session() as session:
                nueva_vacuna = Vacuna(
                    nombre=self.add_nombre,
                    descripcion=self.add_descripcion,
                )
                session.add(nueva_vacuna)
                session.commit()
            self.cargar_vacunas()
        except Exception as e:
            print(f"Error al crear vacuna: {e}")
        self.close_add_dialog()

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
def editar_vacuna(item: Vacuna) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: VacunaState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Vacuna"),
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
                    on_change=VacunaState.set_edit_nombre,
                    on_key_down=VacunaState.handle_key_edit,
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
                    on_change=VacunaState.set_edit_descripcion,
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
                        on_click=VacunaState.update_vacuna,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=VacunaState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_vacuna(item: Vacuna) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Vacuna: {item.nombre}"),
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
                        on_click=lambda: VacunaState.delete_vacuna(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )


@rx.event
def agregar_vacuna() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Vacuna"),
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
                    value=VacunaState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=VacunaState.set_add_nombre,
                    on_key_down=VacunaState.handle_key_add,
                ),
                rx.text(
                    "Descripción",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    value=VacunaState.add_descripcion,
                    placeholder="Ingrese la descripción",
                    on_change=VacunaState.set_add_descripcion,
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
                        on_click=VacunaState.create_vacuna,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=VacunaState.add_modal_open,
        ),
    )


@rx.event
def lista_vacunas() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Descripción"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text("Acciones"),
                            agregar_vacuna(),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    VacunaState.vacunas,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(item.descripcion),
                        rx.table.cell(
                            rx.hstack(
                                editar_vacuna(item),
                                eliminar_vacuna(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=VacunaState.cargar_vacunas,
    )


@template(
    route="/s/vacuna",
    title="Vacunas",
    on_load=ProtectedState.on_load,
)
def vacuna_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Vacunas", size="8"),
        lista_vacunas(),
        padding="4",
        spacing="4",
        width="100%",
    )
