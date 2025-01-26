import reflex as rx
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


## agregar tabla de secreto medico a los pacientes segun profesional.
## un profesional no debe leer la informacion almacenada de otro profesional
class SecretoMedico(rx.Model, TimestampMixin, table=True):
    __tablename__ = "secretomedico"
    id: int | None = Field(default=None, primary_key=True)
    profesional_id: int | None = Field(foreign_key="personal.id")
    paciente_id: int | None = Field(foreign_key="personal.id")
    descripcion: str
