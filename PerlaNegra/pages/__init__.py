from .index import index
from .settings import settings
from .sanidad_dashboard import sanidad_dashboard

# SANIDAD
from ..components.sanidad.cardiologico import cardiologico_form
from ..components.sanidad.declaracion_jurada import declaracion_jurada_form
from ..components.sanidad.ergometria import ergometria_form
from ..components.sanidad.escaneo_anexo import escaneo_anexo_form
from ..components.sanidad.examen_medico import examen_medico_form
from ..components.sanidad.laboratorio import laboratorio_form
from ..components.sanidad.odontologico import odontologico_form
from ..components.sanidad.profesional_paciente import profesional_paciente_form
from ..components.sanidad.programa_salud import programa_salud_form
from ..components.sanidad.prueba_hemograma import prueba_hemograma_form
from ..components.sanidad.tipo_actividad_fisica import tipo_actividad_fisica_form


# PERSONAL
from ..components.personal.actuacion_disciplinaria_scan import (
    actuacion_disciplinaria_scan_form,
)
from ..components.personal.actuacion_disciplinaria import actuacion_disciplinaria_form
from ..components.personal.actuacion_scan import actuacion_scan_form
from ..components.personal.actuacion import actuacion_form
from ..components.personal.atributo_clave import atributo_clave_page
from ..components.personal.atributo_personal import atributo_personal_form
from ..components.personal.calificacion import calificacion_form
from ..components.personal.categoria_personal import categoria_personal_form
from ..components.personal.clase_formacion_academica import (
    clase_formacion_academica_form,
)
from ..components.personal.clase import clase_form
from ..components.personal.compania import compania_form
from ..components.personal.cuadro import cuadro_form
from ..components.personal.direccion import direccion_form
from ..components.personal.estado_civil import estado_civil_page
from ..components.personal.familiar import familiar_form
from ..components.personal.felicitacion import felicitacion_form
from ..components.personal.formacion_academica import formacion_academica_form
from ..components.personal.inasistencia_motivo import inasistencia_motivo_form
from ..components.personal.inasistencia import inasistencia_form
from ..components.personal.movimiento_personal import movimiento_personal_form
from ..components.personal.personal_r import personal_r_form
from ..components.personal.personal_s import personal_s_form
from ..components.personal.personal_seguro import personal_seguro_form
from ..components.personal.personal import personal_form
from ..components.personal.sancion_scan import sancion_scan_form
from ..components.personal.sancion import sancion_form
from ..components.personal.seccion import seccion_form
from ..components.personal.seguro import seguro_form
from ..components.personal.telefono import telefono_form
from ..components.personal.tipo_sancion import tipo_sancion_form
from ..components.personal.unidad import unidad_form
from ..components.personal.vinculo_familiar import vinculo_familiar_form
