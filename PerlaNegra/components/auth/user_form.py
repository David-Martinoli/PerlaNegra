import reflex as rx
from ...database.models.permisos.usuario import Usuario
from ...database.services.usuario_service import UsuarioService


def tabla_usuarios(list_user: list[Usuario]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Contraseña"),
                rx.table.column_header_cell("Accion"),
            )
        ),
        rx.table.body(
            rx.foreach(list_user, row_table)
        )
    )


def show_user(user: Usuario):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.nombre_usuario),
        rx.table.cell(user.hash_contrasena),
    )


def row_table(user: Usuario) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.nombre_usuario),
        rx.table.cell(user.hash_contrasena),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar")
        )),
    )


def usuario_component() -> rx.Component:
    UserState.get_all_usuario()
    return tabla_usuarios(UsuarioService.select_all())


class UserState(rx.State):
    usuario: list[Usuario] = []

    @rx.event
    def get_all_usuario(self):
        # try:
        usuarios = UsuarioService.select_all()
        with self:  # Usar el administrador de contexto
            self.usuario = usuarios
        # except Exception as e:
        #    print(f"Error al obtener usuarios: {e} 002")
        #    self.usuario = []


def index_usuario_component() -> rx.Component:
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Username"),
                    rx.table.column_header_cell("Password"),
                ),
            ),
            rx.table.body(
                rx.cond(
                    UserState.usuario,  # Si hay usuarios
                    rx.foreach(
                        UserState.usuario, show_user
                    ),
                    rx.text("No hay usuarios")  # Si no hay usuarios
                )
            ),
            width="100%",
        ),
        on_mount=UserState.get_all_usuario,
    )
