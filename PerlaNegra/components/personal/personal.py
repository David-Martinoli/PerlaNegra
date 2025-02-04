import reflex as rx
from datetime import date
from sqlmodel import select
from ...templates import template
from ...components.auth.state import ProtectedState
from ...database.models.personal.personal import Personal
from ...database.models.personal.personal_r import PersonalR 
from ...database.models.personal.personal_s import PersonalS

class PersonalCrudState(rx.State):
    """Estado para gestionar el CRUD de personal."""
    
    # Lista de registros
    personal_list: list[Personal] = []
    


    # Estados para edición

    edit_modal_open: bool = False
    edit_id: int | None = None
    edit_personalR_id: int | None = None
    edit_personalS_id: int | None = None
    edit_activo: bool = True

    # Estados para agregar
    add_modal_open: bool = False
    
    # PersonalR fields
    add_nombre: str = ""
    add_apellido: str = ""
    add_dni: str = ""
    add_fecha_nacimiento: str = date.today().isoformat()
    add_estado_civil_id: int = 1
    
    # PersonalS fields
    add_legajo: str = ""
    add_fecha_ingreso: str = date.today().isoformat()
    add_categoria_id: int | None = None
    add_grado: str = ""

    def cargar_personal(self):
        """Carga la lista de personal con sus relaciones."""
        with rx.session() as session:
            query = select(Personal, PersonalS, PersonalR).join(PersonalS).join(PersonalR)
            self.personal_list = session.exec(query).all()

    def create_personal(self):
        """Crea un nuevo registro de personal con sus relaciones."""
        try:
            with rx.session() as session:
                # Crear PersonalR
                nuevo_r = PersonalR(
                    nombre=self.add_nombre,
                    apellido=self.add_apellido,
                    dni=self.add_dni,
                    fecha_nacimiento=date.fromisoformat(self.add_fecha_nacimiento),
                    estado_civil_id=self.add_estado_civil_id
                )
                session.add(nuevo_r)
                session.flush()  # Obtener ID

                # Crear PersonalS
                nuevo_s = PersonalS(
                    nombre=self.add_nombre,
                    apellido=self.add_apellido,
                    numero_legajo=self.add_legajo,
                    fecha_ingreso=date.fromisoformat(self.add_fecha_ingreso),
                    categoria_personal_id=self.add_categoria_id,
                    grado=self.add_grado,
                    fecha_ingreso_unidad=date.today(),
                    fecha_ultimo_ascenso=date.today()
                )
                session.add(nuevo_s)
                session.flush()  # Obtener ID

                # Crear Personal vinculando ambos
                nuevo_personal = Personal(
                    personalR_id=nuevo_r.id,
                    personalS_id=nuevo_s.id,
                    activo=True
                )
                session.add(nuevo_personal)
                session.commit()
                
            self.cargar_personal()
            self.close_add_dialog()
        except Exception as e:
            print(f"Error al crear personal: {e}")

    def update_personal(self):
        """Actualiza un registro existente."""
        if not self.edit_id:
            return
            
        try:
            with rx.session() as session:
                personal = session.get(Personal, self.edit_id)
                if personal:
                    personal.activo = self.edit_activo
                    session.add(personal)
                    session.commit()
                    
            self.cargar_personal()
            self.close_edit_dialog()
        except Exception as e:
            print(f"Error al actualizar personal: {e}")

    def delete_personal(self, personal_id: int):
        """Elimina un registro de personal."""
        try:
            with rx.session() as session:
                personal = session.get(Personal, personal_id)
                if personal:
                    session.delete(personal)
                    session.commit()
            self.cargar_personal()
        except Exception as e:
            print(f"Error al eliminar personal: {e}")

    # Métodos para manejar modales
    def open_add_dialog(self):
        self.add_modal_open = True
        self._reset_add_form()

    def close_add_dialog(self):
        self.add_modal_open = False

    def open_edit_dialog(self, personal: Personal):
        self.edit_id = personal.id
        self.edit_activo = personal.activo
        self.edit_modal_open = True

    def close_edit_dialog(self):
        self.edit_modal_open = False
        
    def _reset_add_form(self):
        """Resetea el formulario de agregar."""
        self.add_nombre = ""
        self.add_apellido = ""
        self.add_dni = ""
        self.add_fecha_nacimiento = date.today().isoformat()
        self.add_estado_civil_id = 1
        self.add_legajo = ""
        self.add_fecha_ingreso = date.today().isoformat()
        self.add_categoria_id = None
        self.add_grado = ""

    # Event handlers para campos del formulario
    @rx.event
    def set_add_nombre(self, value: str):
        self.add_nombre = value

    @rx.event
    def set_add_apellido(self, value: str):
        self.add_apellido = value
        
    # ... otros setters similares para cada campo

def lista_personal() -> rx.Component:
    """Renderiza la lista de personal."""
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Legajo"),
                    rx.table.column_header_cell("Nombre Completo"),
                    rx.table.column_header_cell("DNI"),
                    rx.table.column_header_cell("Grado"),
                    rx.table.column_header_cell("Estado"),
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text("Acciones"),
                            agregar_personal()
                        )
                    ),
                )
            ),
            rx.table.body(
                #rx.foreach(
                #    PersonalCrudState.personal_list,
                #    lambda item: rx.table.row(
                #        rx.table.cell(item.personals.numero_legajo),
                #        rx.table.cell(item.personals.nombre),
                #        rx.table.cell(item.personalr.dni),
                #        rx.table.cell(item.personals.grado),
                #        rx.table.cell("Activo" if item.activo else "Inactivo"),
                #        rx.table.cell(
                #            rx.hstack(
                #                editar_personal(item),
                #                eliminar_personal(item),
                #                spacing="2",
                #            )
                #        ),
                #    ),
                #)
            ),
            variant="surface",
        ),
        on_mount=PersonalCrudState.cargar_personal,
    )

@rx.event
def agregar_personal() -> rx.Component:
    """Modal para agregar personal."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26))
        ),
        rx.dialog.content(
            rx.dialog.title("Agregar Personal"),
            rx.dialog.description(
                "Complete los datos del nuevo personal",
                size="2",
                margin_bottom="4",
            ),
            rx.flex(
                # Datos Personales
                rx.heading("Datos Personales", size="3"),
                rx.input(
                    placeholder="Nombre",
                    on_change=PersonalCrudState.set_add_nombre
                ),
                rx.input(
                    placeholder="Apellido",
                    on_change=PersonalCrudState.set_add_apellido
                ),
                rx.input(
                    placeholder="DNI",
                    #on_change=lambda v: setattr(PersonalCrudState, "add_dni", v)
                ),
                rx.input(
                    type_="date",
                    #on_change=lambda v: setattr(PersonalCrudState, "add_fecha_nacimiento", v)
                ),
                # Datos de Servicio
                rx.heading("Datos de Servicio", size="3", margin_top="4"),
                rx.input(
                    placeholder="Legajo",
                    #on_change=lambda v: setattr(PersonalCrudState, "add_legajo", v)
                ),
                rx.input(
                    placeholder="Grado",
                    #on_change=lambda v: setattr(PersonalCrudState, "add_grado", v)
                ),
                rx.input(
                    type_="date",
                    label="Fecha de Ingreso",
                    #on_change=lambda v: setattr(PersonalCrudState, "add_fecha_ingreso", v)
                ),
                direction="column",
                spacing="3"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft")
                ),
                rx.dialog.close(
                    rx.button(
                        "Guardar",
                        on_click=PersonalCrudState.create_personal
                    )
                ),
                spacing="3",
                justify="end"
            ),
            is_open=PersonalCrudState.add_modal_open
        )
    )

@rx.event
def editar_personal(personal: Personal) -> rx.Component:
    """Modal para editar personal."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar")
        ),
        rx.dialog.content(
            rx.dialog.title("Editar Personal"),
            rx.flex(
                rx.switch(
                    default_checked=personal.activo,
                    on_change=lambda v: setattr(PersonalCrudState, "edit_activo", v)
                ),
                rx.text("Activo"),
                direction="column",
                spacing="3"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft")
                ),
                rx.dialog.close(
                    rx.button(
                        "Guardar",
                        on_click=PersonalCrudState.update_personal
                    )
                ),
                spacing="3",
                justify="end"
            ),
            is_open=PersonalCrudState.edit_modal_open
        )
    )

@rx.event
def eliminar_personal(personal: Personal) -> rx.Component:
    """Modal para confirmar eliminación."""
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Eliminar", bg="red.500", color="white")
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Eliminar Personal"),
            rx.alert_dialog.description(
                f"¿Está seguro de eliminar a {personal.personal_personalr_relation.nombre_completo}?"
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancelar", variant="soft")
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Eliminar",
                        bg="red.500",
                        color="white",
                        on_click=lambda: PersonalCrudState.delete_personal(personal.id)
                    )
                ),
                spacing="3",
                justify="end"
            )
        )
    )

@template(
    route="/p/personal",
    title="Gestión de Personal",
    on_load=ProtectedState.on_load,
)
def personal_page() -> rx.Component:
    """Página principal de gestión de personal."""
    return rx.center(
        rx.vstack(
            rx.heading("Gestión de Personal", size="3"),
            lista_personal(),
            padding="4",
            spacing="4",
            width="100%",
        )
    )
