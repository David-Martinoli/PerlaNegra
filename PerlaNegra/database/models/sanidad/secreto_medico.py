import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


## agregar tabla de secreto medico a los pacientes segun profesional.
## un profesional no debe leer la informacion almacenada de otro profesional
class SecretoMedico(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    profesional_id: int = Field(foreign_key="personal.id")
    paciente_id: int = Field(foreign_key="personal.id")
    descripcion: str

