import reflex as rx
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.sanidad.tiempo_revision import TiempoRevision


class TiempoRevisionState(rx.State):
    tiempos: list[TiempoRevision] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_valor: float = 0.0

    add_modal_open: bool = False
    add_valor: float = 0.0

    delete_modal_open: bool = False

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_tiempo()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_tiempo()
            self.close_edit_dialog()

    def cargar_tiempos(self):
        try:
            with rx.session() as session:
                query = select(TiempoRevision)
                results = session.exec(query).all()
                self.tiempos = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar tiempos: {e}")

    def delete_tiempo(self, tiempo_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(TiempoRevision).where(TiempoRevision.id == tiempo_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_tiempos()
        except Exception as e:
            print(f"Error al eliminar el tiempo: {e}")

    def open_edit_dialog(self, tiempo_id: int):
        self.edit_id = tiempo_id
        with rx.session() as session:
            record = session.exec(
                select(TiempoRevision).where(TiempoRevision.id == tiempo_id)
            ).first()
            if record:
                self.edit_valor = record.valor
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_tiempo(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(TiempoRevision).where(TiempoRevision.id == self.edit_id)
                    ).first()
                    if record:
                        record.valor = self.edit_valor
                        session.add(record)
                        session.commit()
                self.cargar_tiempos()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def open_add_dialog(self):
        self.add_modal_open = True
        self.add_valor = 0.0

    def close_add_dialog(self):
        self.add_modal_open = False

    def create_tiempo(self):
        try:
            with rx.session() as session:
                nuevo_tiempo = TiempoRevision(valor=self.add_valor)
                session.add(nuevo_tiempo)
                session.commit()
            self.cargar_tiempos()
        except Exception as e:
            print(f"Error al crear tiempo: {e}")
        self.close_add_dialog()

    @rx.event
    def set_edit_valor(self, value: str):
        self.edit_valor = float(value.replace(",", ".")) if value else 0.0

    @rx.event
    def set_add_valor(self, value: str):
        self.add_valor = float(value.replace(",", ".")) if value else 0.0


@rx.event
def editar_tiempo(item: TiempoRevision) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: TiempoRevisionState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Tiempo de Revisión"),
            rx.dialog.description(
                "Modifique el valor del tiempo.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Tiempo (minutos)",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    default_value=f"{item.valor:.2f}",
                    type_="number",
                    step="0.01",
                    placeholder="Ingrese el tiempo en minutos",
                    on_change=TiempoRevisionState.set_edit_valor,
                    on_key_down=TiempoRevisionState.handle_key_edit,
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
                        "Guardar",
                        on_click=TiempoRevisionState.update_tiempo,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=TiempoRevisionState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_tiempo(item: TiempoRevision) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Tiempo: {item.valor} minutos"),
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
                        on_click=lambda: TiempoRevisionState.delete_tiempo(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )


@rx.event
def agregar_tiempo() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Tiempo de Revisión"),
            rx.dialog.description(
                "Ingrese el nuevo tiempo de revisión.",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Tiempo (minutos)",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    value=f"{TiempoRevisionState.add_valor:.2f}",
                    type_="number",
                    step="0.01",
                    placeholder="Ingrese el tiempo en minutos",
                    on_change=TiempoRevisionState.set_add_valor,
                    on_key_down=TiempoRevisionState.handle_key_add,
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
                        "Guardar",
                        on_click=TiempoRevisionState.create_tiempo,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=TiempoRevisionState.add_modal_open,
        ),
    )


@rx.event
def lista_tiempos() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Tiempo (minutos)"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text("Acciones"),
                            agregar_tiempo(),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    TiempoRevisionState.tiempos,
                    lambda item: rx.table.row(
                        rx.table.cell(f"{item.valor:.2f}"),
                        rx.table.cell(
                            rx.hstack(
                                editar_tiempo(item),
                                eliminar_tiempo(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=TiempoRevisionState.cargar_tiempos,
    )


@template(
    route="/s/tiempo_revision",
    title="Tiempo de Revisión",
    on_load=ProtectedState.on_load,
)
def tiempo_revision_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Tiempos de Revisión", size="8"),
        lista_tiempos(),
        padding="4",
        spacing="4",
        width="100%",
    )
