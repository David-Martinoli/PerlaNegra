import reflex as rx
from datetime import datetime
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.vinculo_familiar import VinculoFamiliar


class VinculoFamiliarState(rx.State):
    vinculos: list[VinculoFamiliar] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_nombre: str = ""

    add_modal_open: bool = False
    add_nombre: str = ""

    def handle_key_add(self, key: str):
        if key == "Enter":
            self.create_vinculo()
            self.close_add_dialog()

    def handle_key_edit(self, key: str):
        if key == "Enter":
            self.update_vinculo()
            self.close_edit_dialog()

    def cargar_vinculos(self):
        try:
            with rx.session() as session:
                query = select(VinculoFamiliar)
                results = session.exec(query).all()
                self.vinculos = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar vínculos: {e}")

    def delete_vinculo(self, vinculo_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(VinculoFamiliar).where(VinculoFamiliar.id == vinculo_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_vinculos()
        except Exception as e:
            print(f"Error al eliminar el vínculo: {e}")

    def open_edit_dialog(self, vinculo_id: int):
        self.edit_id = vinculo_id
        with rx.session() as session:
            record = session.exec(
                select(VinculoFamiliar).where(VinculoFamiliar.id == vinculo_id)
            ).first()
            if record:
                self.edit_nombre = record.nombre
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False

    def update_vinculo(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(VinculoFamiliar).where(
                            VinculoFamiliar.id == self.edit_id
                        )
                    ).first()
                    if record:
                        record.nombre = self.edit_nombre
                        session.add(record)
                        session.commit()
                self.cargar_vinculos()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.close_edit_dialog()

    def create_vinculo(self):
        try:
            with rx.session() as session:
                nuevo_vinculo = VinculoFamiliar(
                    nombre=self.add_nombre, created_at=datetime.now()
                )
                session.add(nuevo_vinculo)
                session.commit()
            self.cargar_vinculos()
        except Exception as e:
            print(f"Error al crear vínculo: {e}")
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
def editar_vinculo(item: VinculoFamiliar) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: VinculoFamiliarState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Vínculo Familiar"),
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
                    on_change=lambda val: VinculoFamiliarState.set_edit_nombre(val),
                    on_key_down=VinculoFamiliarState.handle_key_edit,
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
                    rx.button("Guardar", on_click=VinculoFamiliarState.update_vinculo)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=VinculoFamiliarState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_vinculo(item: VinculoFamiliar) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Vínculo: {item.nombre}"),
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
                        on_click=lambda: VinculoFamiliarState.delete_vinculo(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@rx.event
def agregar_vinculo() -> rx.Component:
    VinculoFamiliarState.add_nombre = ""

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Vínculo Familiar"),
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
                    value=VinculoFamiliarState.add_nombre,
                    placeholder="Ingrese el nombre",
                    on_change=VinculoFamiliarState.set_add_nombre,
                    on_key_down=VinculoFamiliarState.handle_key_add,
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
                    rx.button("Guardar", on_click=VinculoFamiliarState.create_vinculo)
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=VinculoFamiliarState.add_modal_open,
        ),
    )


@rx.event
def lista_vinculos() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.hstack("Acciones"),
                            rx.hstack(agregar_vinculo()),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    VinculoFamiliarState.vinculos,
                    lambda item: rx.table.row(
                        rx.table.cell(item.nombre),
                        rx.table.cell(
                            rx.hstack(
                                editar_vinculo(item),
                                eliminar_vinculo(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=VinculoFamiliarState.cargar_vinculos,
    )


@template(
    route="/p/vinculo_familiar",
    title="Vínculo Familiar",
    on_load=ProtectedState.on_load,
)
def vinculo_familiar_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Vínculos Familiares", size="8"),
        lista_vinculos(),
        padding="4",
        spacing="4",
        width="100%",
    )
