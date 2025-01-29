import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal


class EstadoDental(str, Enum):
    SANO = "SANO"
    CARIES = "CARIES"
    OBTURADO = "OBTURADO"
    AUSENTE = "AUSENTE"
    PROTESIS = "PROTESIS"


class Odontologico(rx.Model, TimestampMixin, table=True):
    """Modelo para gestionar exámenes odontológicos."""

    __tablename__ = "odontologico"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    estado_general: EstadoDental = Field(default=EstadoDental.SANO)

    examen_odontologico: str = Field(default="", max_length=1200)
    observacion_odontologica: str = Field(default="", max_length=1200)
    fecha_odontograma: date = Field()

    requiere_tratamiento: bool = Field(default=False)
    proxima_revision: date | None = Field(default=None)

    # Relaciones
    odontologico_personal_relation: "Personal" = Relationship(
        back_populates="personal_odontologico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("fecha", "proxima_revision")
    # def validar_fechas(cls, v):
    #    if v and v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"Odontologico(fecha={self.fecha})"
