import reflex as rx
import reflex_local_auth

from PerlaNegra.components.auth.state import ProtectedState
from PerlaNegra.components.sanidad.declaracion_jurada import declaracion_jurada_form
from PerlaNegra.components.sanidad.ergometria import ergometria_form
from PerlaNegra.components.sanidad.escaneo_anexo import escaneo_anexo_form
from PerlaNegra.components.sanidad.examen_medico import (
    ExamenMedicoState,
    examen_medico_form,
)
from PerlaNegra.components.sanidad.laboratorio import LaboratorioState, laboratorio_form
from PerlaNegra.components.sanidad.odontologico import (
    OdontologicoState,
    odontologico_form,
)
from PerlaNegra.components.sanidad.prueba_hemograma import (
    PruebaHemogramaState,
    prueba_hemograma_form,
)
from PerlaNegra.components.sanidad.tipo_actividad_fisica import (
    TipoActividadFisicaState,
    tipo_actividad_fisica_form,
)

from ..templates import template
from ..components.base import base_page


class EscaneoAnexoPageState(rx.State):
    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        print("Datos recibidos:", form_data)
        # Implementar lógica para guardar en BD


class SanidadState(rx.State):
    def handle_declaracion_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        # Aquí procesas los datos del formulario
        print("Datos recibidos:", form_data)
        # Implementar la lógica para guardar en la base de datos


class ErgometriaPageState(rx.State):
    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        print("Datos recibidos:", form_data)
        # Aquí implementar la lógica para guardar en BD


@template(route="/sanidad", title="Sanidad", on_load=ProtectedState.on_load)
@reflex_local_auth.require_login
def sanidad_dashboard() -> rx.Component:
    my_child = rx.vstack(
        rx.text("Sanidad Dashboard"),
        # declaracion_jurada_form(on_submit=SanidadState.handle_declaracion_submit),
        # aqui agregar la vista para un dashbaord de sanidad
    )
    return base_page(my_child)


@template(
    route="/declaracion-jurada",
    title="Declaración Jurada",
    on_load=ProtectedState.on_load,
)
def declaracion_jurada_page() -> rx.Component:
    return rx.vstack(
        declaracion_jurada_form(on_submit=SanidadState.handle_declaracion_submit),
        spacing="4",
        align_items="stretch",
    )


@template(
    route="/sanidad/ergometria", title="Ergometría", on_load=ProtectedState.on_load
)
def ergometria_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            ergometria_form(on_submit=ErgometriaPageState.handle_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


@template(
    route="/sanidad/escaneo-anexo",
    title="Escaneo Anexo",
    on_load=ProtectedState.on_load,
)
def escaneo_anexo_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            escaneo_anexo_form(on_submit=EscaneoAnexoPageState.handle_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


@template(
    route="/sanidad/examen-medico",
    title="Examen Médico",
    on_load=ProtectedState.on_load,
)
def examen_medico_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            examen_medico_form(on_submit=ExamenMedicoState.hre_hacer_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


# Agregar nueva ruta
@template(
    route="/sanidad/laboratorio", title="Laboratorio", on_load=ProtectedState.on_load
)
def laboratorio_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            laboratorio_form(on_submit=LaboratorioState.handle_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


# Agregar nueva ruta
@template(
    route="/sanidad/odontologico", title="Odontológico", on_load=ProtectedState.on_load
)
def odontologico_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            odontologico_form(on_submit=OdontologicoState.handle_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


@template(
    route="/sanidad/hemograma", title="Prueba Hemograma", on_load=ProtectedState.on_load
)
def hemograma_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            prueba_hemograma_form(on_submit=PruebaHemogramaState.handle_submit),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )


# Agregar nueva ruta
@template(
    route="/sanidad/tipo-actividad-fisica",
    title="Tipo Actividad Física",
    on_load=ProtectedState.on_load,
)
def tipo_actividad_fisica_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            tipo_actividad_fisica_form(
                on_submit=TipoActividadFisicaState.handle_submit
            ),
            width="100%",
            max_width="800px",
            spacing="4",
            py="4",
        )
    )
