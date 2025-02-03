import reflex as rx
from datetime import datetime
from sqlmodel import select
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.personal.calificacion import Calificacion


class CalificacionState(rx.State):
    calificaciones: list[Calificacion] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_personal_id: int = 0
    edit_val1: int = 0
    edit_val2: int = 0
    edit_val3: int = 0
    edit_val4: int = 0
    edit_val5: int = 0
    edit_promedio: float = 0.0

    add_modal_open: bool = False
    add_personal_id: int = 0
    add_val1: int = 0
    add_val2: int = 0
    add_val3: int = 0
    add_val4: int = 0
    add_val5: int = 0
    add_promedio: float = 0.0

    def cargar_calificaciones(self):
        try:
            with rx.session() as session:
                query = select(Calificacion)
                results = session.exec(query).all()
                self.calificaciones = [
                    result for result in results if result is not None
                ]
        except Exception as e:
            print(f"Error al cargar calificaciones: {e}")

    def delete_calificacion(self, calificacion_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(Calificacion).where(Calificacion.id == calificacion_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_calificaciones()
        except Exception as e:
            print(f"Error al eliminar la calificación: {e}")

    def open_edit_dialog(self, calificacion_id: int):
        with rx.session() as session:
            record = session.exec(
                select(Calificacion).where(Calificacion.id == calificacion_id)
            ).first()
            if record:
                self.edit_id = calificacion_id
                self.edit_personal_id = record.personal_id
                self.edit_val1 = record.val1
                self.edit_val2 = record.val2
                self.edit_val3 = record.val3
                self.edit_val4 = record.val4
                self.edit_val5 = record.val5
                self.edit_promedio = record.promedio
        self.edit_modal_open = True

    def update_calificacion(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(Calificacion).where(Calificacion.id == self.edit_id)
                    ).first()
                    if record:
                        record.personal_id = self.edit_personal_id
                        record.val1 = self.edit_val1
                        record.val2 = self.edit_val2
                        record.val3 = self.edit_val3
                        record.val4 = self.edit_val4
                        record.val5 = self.edit_val5
                        record.promedio = self.edit_promedio
                        session.add(record)
                        session.commit()
                self.cargar_calificaciones()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.edit_modal_open = False

    def create_calificacion(self):
        try:
            with rx.session() as session:
                nueva_calificacion = Calificacion(
                    personal_id=self.add_personal_id,
                    val1=self.add_val1,
                    val2=self.add_val2,
                    val3=self.add_val3,
                    val4=self.add_val4,
                    val5=self.add_val5,
                    promedio=self.add_promedio,
                    created_at=datetime.now(),
                )
                session.add(nueva_calificacion)
                session.commit()
            self.cargar_calificaciones()
        except Exception as e:
            print(f"Error al crear calificación: {e}")
        self.add_modal_open = False

    # Eventos para actualizar campos
    @rx.event
    def set_edit_personal_id(self, value: int):
        self.edit_personal_id = value

    @rx.event
    def set_edit_val1(self, value: int):
        self.edit_val1 = value

    @rx.event
    def set_edit_val2(self, value: int):
        self.edit_val2 = value

    @rx.event
    def set_edit_val3(self, value: int):
        self.edit_val3 = value

    @rx.event
    def set_edit_val4(self, value: int):
        self.edit_val4 = value

    @rx.event
    def set_edit_val5(self, value: int):
        self.edit_val5 = value

    @rx.event
    def set_edit_promedio(self, value: float):
        self.edit_promedio = value

    @rx.event
    def set_add_personal_id(self, value: int):
        self.add_personal_id = value

    @rx.event
    def set_add_val1(self, value: int):
        self.add_val1 = value

    @rx.event
    def set_add_val2(self, value: int):
        self.add_val2 = value

    @rx.event
    def set_add_val3(self, value: int):
        self.add_val3 = value

    @rx.event
    def set_add_val4(self, value: int):
        self.add_val4 = value

    @rx.event
    def set_add_val5(self, value: int):
        self.add_val5 = value

    @rx.event
    def set_add_promedio(self, value: float):
        self.add_promedio = value


@rx.event
def editar_calificacion(item: Calificacion) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar", on_click=lambda: CalificacionState.open_edit_dialog(item.id)
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Calificación"),
            rx.dialog.description(
                "Modifique los valores de la calificación.",
                size="2",
                margin_bottom="16px",
            ),
            rx.table.root(
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("ID Personal"),
                        rx.table.cell(
                            rx.input(
                                placeholder="ID Personal",
                                type_="number",
                                value=item.personal_id,
                                on_change=CalificacionState.set_edit_personal_id,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 1"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 1",
                                type_="number",
                                value=item.val1,
                                on_change=CalificacionState.set_edit_val1,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 2"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 2",
                                type_="number",
                                value=item.val2,
                                on_change=CalificacionState.set_edit_val2,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 3"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 3",
                                type_="number",
                                value=item.val3,
                                on_change=CalificacionState.set_edit_val3,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 4"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 4",
                                type_="number",
                                value=item.val4,
                                on_change=CalificacionState.set_edit_val4,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 5"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 5",
                                type_="number",
                                value=item.val5,
                                on_change=CalificacionState.set_edit_val5,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Promedio"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Promedio",
                                type_="number",
                                step="0.01",
                                value=item.promedio,
                                on_change=CalificacionState.set_edit_promedio,
                            ),
                        ),
                    ),
                ),
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button(
                        "Guardar",
                        on_click=CalificacionState.update_calificacion,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=CalificacionState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_calificacion(item: Calificacion) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Calificación #{item.id}"),
            rx.alert_dialog.description(
                "¿Está seguro que desea eliminar esta calificación? Esta acción es permanente.",
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
                        on_click=lambda: CalificacionState.delete_calificacion(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )


@rx.event
def agregar_calificacion() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Calificación"),
            rx.dialog.description(
                "Ingrese los valores de la nueva calificación.",
                size="2",
                margin_bottom="16px",
            ),
            rx.table.root(
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("ID Personal"),
                        rx.table.cell(
                            rx.input(
                                placeholder="ID Personal",
                                type_="number",
                                on_change=CalificacionState.set_add_personal_id,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 1"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 1",
                                type_="number",
                                on_change=CalificacionState.set_add_val1,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 2"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 2",
                                type_="number",
                                on_change=CalificacionState.set_add_val2,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 3"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 3",
                                type_="number",
                                on_change=CalificacionState.set_add_val3,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 4"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 4",
                                type_="number",
                                on_change=CalificacionState.set_add_val4,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Valor 5"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Valor 5",
                                type_="number",
                                on_change=CalificacionState.set_add_val5,
                            ),
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Promedio"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Promedio",
                                type_="number",
                                step="0.01",
                                on_change=CalificacionState.set_add_promedio,
                            ),
                        ),
                    ),
                ),
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button(
                        "Guardar",
                        on_click=CalificacionState.create_calificacion,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=CalificacionState.add_modal_open,
        ),
    )


@rx.event
def lista_calificaciones() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID Personal"),
                    rx.table.column_header_cell("Val 1"),
                    rx.table.column_header_cell("Val 2"),
                    rx.table.column_header_cell("Val 3"),
                    rx.table.column_header_cell("Val 4"),
                    rx.table.column_header_cell("Val 5"),
                    rx.table.column_header_cell("Promedio"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_calificacion()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    CalificacionState.calificaciones,
                    lambda item: rx.table.row(
                        rx.table.cell(item.personal_id),
                        rx.table.cell(item.val1),
                        rx.table.cell(item.val2),
                        rx.table.cell(item.val3),
                        rx.table.cell(item.val4),
                        rx.table.cell(item.val5),
                        rx.table.cell(f"{item.promedio:.2f}"),
                        rx.table.cell(
                            rx.hstack(
                                editar_calificacion(item),
                                eliminar_calificacion(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=CalificacionState.cargar_calificaciones,
    )


@template(
    route="/p/calificacion",
    title="Calificación",
    on_load=ProtectedState.on_load,
)
def calificacion_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Calificaciones", size="8"),
        lista_calificaciones(),
        padding="4",
        spacing="4",
        width="100%",
    )
