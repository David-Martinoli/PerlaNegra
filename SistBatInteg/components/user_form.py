import reflex as rx
from ..database.models.permisos.usuario import Usuario
from ..database.services.usuario_service import UsuarioService


class UserState(rx.State):
    usuario: list[Usuario]

    @rx.event(background=True)
    async def get_all_usuario(self):
        async with self:
            self.usuario = UsuarioService.select_all_usuario()


def usuario_component() -> rx.Component:
    UserState.get_all_usuario()

    return rx.card(
        rx.vstack(
            rx.heading("Información del Usuario", size="3"),
            rx.form(
                rx.text("Nombre de Usuario"),
                rx.input(placeholder="Ingrese nombre de usuario", size="1"),
            ),
            rx.form(
                rx.text("Contraseña"),
                rx.input(type="password",
                         placeholder="Ingrese contraseña", size="1"),
            ),
            rx.form(
                rx.text("ID de Personal"),
                rx.input(type="number",
                         placeholder="Ingrese ID de personal", size="1"),
            ),
            rx.hstack(
                rx.button("Guardar", color_scheme="blue"),
                rx.button("Cancelar", variant="outline"),
                spacing="4",
            ),
            spacing="4",
            padding="6",
            width="100%",
        ),
        width="container.md",
    ),
    tabla_usuarios(UserState.usuario)


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


def row_table(user: Usuario) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.nombre_usuario),
        rx.table.cell(user.hash_contrasena),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar")
        )),
    )
