from .index import index
from .settings import settings

# from .sanidad_dashboard import sanidad_dashboard

# SANIDAD
from ..components.sanidad.cardiologico import cardiologico_page
from ..components.sanidad.declaracion_jurada import declaracion_jurada_form
from ..components.sanidad.ergometria import ergometria_page
from ..components.sanidad.escaneo_anexo import escaneo_anexo_form
from ..components.sanidad.examen_medico import examen_medico_form
from ..components.sanidad.laboratorio import laboratorio_form
from ..components.sanidad.odontologico import odontologico_form
from ..components.sanidad.profesional_paciente import profesional_paciente_page
from ..components.sanidad.programa_salud import programa_salud_page
from ..components.sanidad.prueba_hemograma import prueba_hemograma_page
from ..components.sanidad.tipo_actividad_fisica import tipo_actividad_fisica_page
from ..components.sanidad.enfermedad import enfermedad_page
from ..components.sanidad.sintoma import sintoma_page
from ..components.sanidad.tiempo_revision import tiempo_revision_page
from ..components.sanidad.vacuna import vacuna_page


# PERSONAL
from ..components.personal.actuacion_disciplinaria_scan import (
    actuacion_disciplinaria_scan_form,
)
from ..components.personal.actuacion_disciplinaria import actuacion_disciplinaria_page
from ..components.personal.actuacion_scan import actuacion_scan_page
from ..components.personal.actuacion import actuacion_page
from ..components.personal.atributo_clave import atributo_clave_page
from ..components.personal.atributo_personal import atributo_personal_form
from ..components.personal.calificacion import calificacion_page
from ..components.personal.categoria_personal import categoria_personal_page
from ..components.personal.clase_formacion_academica import (
    clase_formacion_academica_page,
)
from ..components.personal.clase import clase_page
from ..components.personal.compania import compania_page
from ..components.personal.cuadro import cuadro_page
from ..components.personal.direccion import direccion_page
from ..components.personal.estado_civil import estado_civil_page
from ..components.personal.familiar import familiar_page
from ..components.personal.felicitacion import felicitacion_page
from ..components.personal.formacion_academica import formacion_academica_page
from ..components.personal.inasistencia_motivo import inasistencia_motivo_page
from ..components.personal.inasistencia import inasistencia_page
from ..components.personal.movimiento_personal import movimiento_personal_page
from ..components.personal.personal_r import personal_r_page
from ..components.personal.personal_s import personal_s_page
from ..components.personal.personal_seguro import personal_seguro_page
from ..components.personal.personal import personal_page
from ..components.personal.sancion_scan import sancion_scan_page
from ..components.personal.sancion import sancion_page
from ..components.personal.seccion import seccion_page
from ..components.personal.seguro import seguro_page
from ..components.personal.telefono import telefono_page
from ..components.personal.tipo_sancion import tipo_sancion_page
from ..components.personal.unidad import unidad_page
from ..components.personal.vinculo_familiar import vinculo_familiar_page
