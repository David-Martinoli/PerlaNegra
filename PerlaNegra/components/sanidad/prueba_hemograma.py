import reflex as rx
from datetime import datetime
from sqlmodel import select
from PerlaNegra.templates import template
from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.database.models.sanidad.prueba_hemograma import PruebaHemograma


class PruebaHemogramaState(rx.State):
    pruebas: list[PruebaHemograma] = []

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_globulos_rojos: int = 0
    edit_hematocritos: int = 0
    edit_hb: int = 0
    edit_vcm: int = 0
    edit_hcm: int = 0
    edit_chcm: int = 0
    edit_rdw: int = 0
    edit_cv: int = 0
    edit_plaquetas: int = 0
    edit_globulos_blancos: int = 0
    edit_formula: str = ""

    add_modal_open: bool = False
    add_globulos_rojos: int = 0
    add_hematocritos: int = 0
    add_hb: int = 0
    add_vcm: int = 0
    add_hcm: int = 0
    add_chcm: int = 0
    add_rdw: int = 0
    add_cv: int = 0
    add_plaquetas: int = 0
    add_globulos_blancos: int = 0
    add_formula: str = ""

    def cargar_pruebas(self):
        try:
            with rx.session() as session:
                query = select(PruebaHemograma)
                results = session.exec(query).all()
                self.pruebas = [result for result in results if result is not None]
        except Exception as e:
            print(f"Error al cargar pruebas: {e}")

    def delete_prueba(self, prueba_id: int):
        try:
            with rx.session() as session:
                record = session.exec(
                    select(PruebaHemograma).where(PruebaHemograma.id == prueba_id)
                ).first()
                if record:
                    session.delete(record)
                    session.commit()
            self.cargar_pruebas()
        except Exception as e:
            print(f"Error al eliminar la prueba: {e}")

    def open_edit_dialog(self, prueba_id: int):
        with rx.session() as session:
            record = session.exec(
                select(PruebaHemograma).where(PruebaHemograma.id == prueba_id)
            ).first()
            if record:
                self.edit_id = prueba_id
                self.edit_globulos_rojos = record.globulos_rojos
                self.edit_hematocritos = record.hematocritos
                self.edit_hb = record.hb
                self.edit_vcm = record.vcm
                self.edit_hcm = record.hcm
                self.edit_chcm = record.chcm
                self.edit_rdw = record.rdw
                self.edit_cv = record.cv
                self.edit_plaquetas = record.plaquetas
                self.edit_globulos_blancos = record.globulos_blancos
                self.edit_formula = record.formula
        self.edit_modal_open = True

    def update_prueba(self):
        if self.edit_id is not None:
            try:
                with rx.session() as session:
                    record = session.exec(
                        select(PruebaHemograma).where(
                            PruebaHemograma.id == self.edit_id
                        )
                    ).first()
                    if record:
                        record.globulos_rojos = self.edit_globulos_rojos
                        record.hematocritos = self.edit_hematocritos
                        record.hb = self.edit_hb
                        record.vcm = self.edit_vcm
                        record.hcm = self.edit_hcm
                        record.chcm = self.edit_chcm
                        record.rdw = self.edit_rdw
                        record.cv = self.edit_cv
                        record.plaquetas = self.edit_plaquetas
                        record.globulos_blancos = self.edit_globulos_blancos
                        record.formula = self.edit_formula
                        session.add(record)
                        session.commit()
                self.cargar_pruebas()
            except Exception as e:
                print(f"Error al actualizar: {e}")
        self.edit_modal_open = False

    def create_prueba(self):
        try:
            with rx.session() as session:
                nueva_prueba = PruebaHemograma(
                    globulos_rojos=self.add_globulos_rojos,
                    hematocritos=self.add_hematocritos,
                    hb=self.add_hb,
                    vcm=self.add_vcm,
                    hcm=self.add_hcm,
                    chcm=self.add_chcm,
                    rdw=self.add_rdw,
                    cv=self.add_cv,
                    plaquetas=self.add_plaquetas,
                    globulos_blancos=self.add_globulos_blancos,
                    formula=self.add_formula,
                    created_at=datetime.now(),
                )
                session.add(nueva_prueba)
                session.commit()
            self.cargar_pruebas()
        except Exception as e:
            print(f"Error al crear prueba: {e}")
        self.add_modal_open = False

    # Eventos para actualizar campos de edición
    @rx.event
    def set_edit_globulos_rojos(self, value: int):
        self.edit_globulos_rojos = value

    @rx.event
    def set_edit_hematocritos(self, value: int):
        self.edit_hematocritos = value

    @rx.event
    def set_edit_hb(self, value: int):
        self.edit_hb = value

    @rx.event
    def set_edit_vcm(self, value: int):
        self.edit_vcm = value

    @rx.event
    def set_edit_hcm(self, value: int):
        self.edit_hcm = value

    @rx.event
    def set_edit_chcm(self, value: int):
        self.edit_chcm = value

    @rx.event
    def set_edit_rdw(self, value: int):
        self.edit_rdw = value

    @rx.event
    def set_edit_cv(self, value: int):
        self.edit_cv = value

    @rx.event
    def set_edit_plaquetas(self, value: int):
        self.edit_plaquetas = value

    @rx.event
    def set_edit_globulos_blancos(self, value: int):
        self.edit_globulos_blancos = value

    @rx.event
    def set_edit_formula(self, value: str):
        self.edit_formula = value

    # Eventos para actualizar campos de adición
    @rx.event
    def set_add_globulos_rojos(self, value: int):
        self.add_globulos_rojos = value

    @rx.event
    def set_add_hematocritos(self, value: int):
        self.add_hematocritos = value

    @rx.event
    def set_add_hb(self, value: int):
        self.add_hb = value

    @rx.event
    def set_add_vcm(self, value: int):
        self.add_vcm = value

    @rx.event
    def set_add_hcm(self, value: int):
        self.add_hcm = value

    @rx.event
    def set_add_chcm(self, value: int):
        self.add_chcm = value

    @rx.event
    def set_add_rdw(self, value: int):
        self.add_rdw = value

    @rx.event
    def set_add_cv(self, value: int):
        self.add_cv = value

    @rx.event
    def set_add_plaquetas(self, value: int):
        self.add_plaquetas = value

    @rx.event
    def set_add_globulos_blancos(self, value: int):
        self.add_globulos_blancos = value

    @rx.event
    def set_add_formula(self, value: str):
        self.add_formula = value


@rx.event
def editar_prueba(item: PruebaHemograma) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Editar",
                on_click=lambda: PruebaHemogramaState.open_edit_dialog(item.id),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Prueba de Hemograma"),
            rx.dialog.description(
                "Modifique los valores de la prueba.",
                size="2",
                margin_bottom="16px",
            ),
            rx.table.root(
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("Glóbulos Rojos"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.globulos_rojos,
                                on_change=PruebaHemogramaState.set_edit_globulos_rojos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Hematocritos"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.hematocritos,
                                on_change=PruebaHemogramaState.set_edit_hematocritos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("HB"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.hb,
                                on_change=PruebaHemogramaState.set_edit_hb,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("VCM"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.vcm,
                                on_change=PruebaHemogramaState.set_edit_vcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("HCM"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.hcm,
                                on_change=PruebaHemogramaState.set_edit_hcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("CHCM"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.chcm,
                                on_change=PruebaHemogramaState.set_edit_chcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("RDW"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.rdw,
                                on_change=PruebaHemogramaState.set_edit_rdw,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("CV"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.cv,
                                on_change=PruebaHemogramaState.set_edit_cv,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Plaquetas"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.plaquetas,
                                on_change=PruebaHemogramaState.set_edit_plaquetas,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Glóbulos Blancos"),
                        rx.table.cell(
                            rx.input(
                                type_="number",
                                value=item.globulos_blancos,
                                on_change=PruebaHemogramaState.set_edit_globulos_blancos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Fórmula"),
                        rx.table.cell(
                            rx.input(
                                value=item.formula,
                                on_change=PruebaHemogramaState.set_edit_formula,
                            )
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
                        on_click=PruebaHemogramaState.update_prueba,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=PruebaHemogramaState.edit_modal_open,
        ),
    )


@rx.event
def eliminar_prueba(item: PruebaHemograma) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Prueba #{item.id}"),
            rx.alert_dialog.description(
                "¿Está seguro que desea eliminar esta prueba? Esta acción es permanente.",
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
                        on_click=lambda: PruebaHemogramaState.delete_prueba(item.id),
                    )
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )


@rx.event
def agregar_prueba() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26)),
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Prueba de Hemograma"),
            rx.dialog.description(
                "Ingrese los valores de la nueva prueba.",
                size="2",
                margin_bottom="16px",
            ),
            rx.table.root(
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("Glóbulos Rojos"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Glóbulos Rojos",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_globulos_rojos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Hematocritos"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Hematocritos",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_hematocritos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("HB"),
                        rx.table.cell(
                            rx.input(
                                placeholder="HB",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_hb,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("VCM"),
                        rx.table.cell(
                            rx.input(
                                placeholder="VCM",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_vcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("HCM"),
                        rx.table.cell(
                            rx.input(
                                placeholder="HCM",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_hcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("CHCM"),
                        rx.table.cell(
                            rx.input(
                                placeholder="CHCM",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_chcm,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("RDW"),
                        rx.table.cell(
                            rx.input(
                                placeholder="RDW",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_rdw,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("CV"),
                        rx.table.cell(
                            rx.input(
                                placeholder="CV",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_cv,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Plaquetas"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Plaquetas",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_plaquetas,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Glóbulos Blancos"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Glóbulos Blancos",
                                type_="number",
                                on_change=PruebaHemogramaState.set_add_globulos_blancos,
                            )
                        ),
                    ),
                    rx.table.row(
                        rx.table.cell("Fórmula"),
                        rx.table.cell(
                            rx.input(
                                placeholder="Fórmula",
                                on_change=PruebaHemogramaState.set_add_formula,
                            )
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
                        on_click=PruebaHemogramaState.create_prueba,
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            is_open=PruebaHemogramaState.add_modal_open,
        ),
    )


@rx.event
def lista_pruebas() -> rx.Component:
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Glóbulos Rojos"),
                    rx.table.column_header_cell("Hematocritos"),
                    rx.table.column_header_cell("HB"),
                    rx.table.column_header_cell("VCM"),
                    rx.table.column_header_cell("HCM"),
                    rx.table.column_header_cell("CHCM"),
                    rx.table.column_header_cell("RDW"),
                    rx.table.column_header_cell("CV"),
                    rx.table.column_header_cell("Plaquetas"),
                    rx.table.column_header_cell("Glóbulos Blancos"),
                    rx.table.column_header_cell("Fórmula"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text("Acciones"),
                            agregar_prueba(),
                        ),
                    ),
                )
            ),
            rx.table.body(
                rx.foreach(
                    PruebaHemogramaState.pruebas,
                    lambda item: rx.table.row(
                        rx.table.cell(item.globulos_rojos),
                        rx.table.cell(item.hematocritos),
                        rx.table.cell(item.hb),
                        rx.table.cell(item.vcm),
                        rx.table.cell(item.hcm),
                        rx.table.cell(item.chcm),
                        rx.table.cell(item.rdw),
                        rx.table.cell(item.cv),
                        rx.table.cell(item.plaquetas),
                        rx.table.cell(item.globulos_blancos),
                        rx.table.cell(item.formula),
                        rx.table.cell(
                            rx.hstack(
                                editar_prueba(item),
                                eliminar_prueba(item),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
            variant="surface",
        ),
        on_mount=PruebaHemogramaState.cargar_pruebas,
    )


@template(
    route="/s/prueba_hemograma",
    title="Prueba de Hemograma",
    on_load=ProtectedState.on_load,
)
def prueba_hemograma_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Pruebas de Hemograma", size="8"),
        lista_pruebas(),
        padding="4",
        spacing="4",
        width="100%",
    )
