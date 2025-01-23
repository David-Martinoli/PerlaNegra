# Sanidad
from .sanidad.profesional_paciente import ProfesionalPaciente
from .sanidad.programa_salud import ProgramaSalud
from .sanidad.prueba_hemograma import PruebaHemograma
from .sanidad.cardiologico import Cardiologico
from .sanidad.declaracion_jurada import DeclaracionJurada
from .sanidad.ergometria import Ergometria
from .sanidad.escaneo_anexo import EscaneoAnexo
from .sanidad.laboratorio import Laboratorio
from .sanidad.odontologico import Odontologico
from .sanidad.secreto_medico import SecretoMedico
from .sanidad.tiempo_revision import TiempoRevision
from .sanidad.examen_medico import ExamenMedico
from .sanidad.tipo_actividad_fisica import TipoActividadFisica
from .sanidad.declaracion_sintoma import DeclaracionSintoma
from .sanidad.enfermedad import Enfermedad
from .sanidad.programa_salud import ProgramaSalud
from .sanidad.sintoma import Sintoma
from .sanidad.vacuna import Vacuna
from .sanidad.vacunacion import Vacunacion

# Auditoria
from .auditoria.auditoria_rol import AuditoriaRol
from .auditoria.auditoria import Auditoria

# Mixins
from .mixins.timestamp_mixin import TimestampMixin

# Permisos
from .permisos.acceso_sector import AccesoSector
from .permisos.usuario import Usuario
from .permisos.usuario_rol import UsuarioRol
from .permisos.rol_permiso import RolPermiso
from .permisos.rol import Rol
from .permisos.permiso import Permiso

# Personal
from .personal.atributo_clave import AtributoClave
from .personal.atributo_personal import AtributoPersonal
from .personal.telefono import Telefono
from .personal.unidad import Unidad
from .personal.calificacion import Calificacion
from .personal.categoria_personal import CategoriaPersonal
from .personal.compania import Compania
from .personal.cuadro import Cuadro
from .personal.direccion import Direccion
from .personal.movimiento_personal import MovimientoPersonal
from .personal.personal_r import PersonalR
from .personal.personal_s import PersonalS
from .personal.personal import Personal
from .personal.actuacion import Actuacion
from .personal.actuacion_disciplinaria import ActuacionDisciplinaria
from .personal.actuacion_disciplinaria_scan import ActuacionDisciplinariaScan
from .personal.actuacion_scan import ActuacionScan
from .personal.clase_formacion_academica import ClaseFormacionAcademica
from .personal.formacion_academica import FormacionAcademica
from .personal.clase import Clase
from .personal.estado_civil import EstadoCivil
from .personal.familiar import Familiar
from .personal.felicitacion import Felicitacion
from .personal.inasistencia import Inasistencia
from .personal.inasistencia_motivo import InasistenciaMotivo
from .personal.personal_seguro import PersonalSeguro
from .personal.sancion_scan import SancionScan
from .personal.sancion import Sancion
from .personal.seccion import Seccion
from .personal.seguro import Seguro
from .personal.tipo_sancion import TipoSancion
from .personal.vinculo_familiar import VinculoFamiliar

# Models


# CONSTANTS
# FELICITACION = Felicitacion.__class__.__name__
# PERSONAL = Personal.__class__.__name__
