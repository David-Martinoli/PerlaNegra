import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .examen_medico import ExamenMedico
    from .ergometria import Ergometria
    from .declaracion_jurada import DeclaracionJurada


class Cardiologico(rx.Model, TimestampMixin, table=True):
    """Modelo para exámenes cardiológicos."""

    __tablename__ = "cardiologico"

    id: int | None = Field(default=None, primary_key=True)
    examen_medico_id: int | None = Field(foreign_key="examenmedico.id")
    ergometria_id: int | None = Field(foreign_key="ergometria.id")

    ecg: str = Field(default="", max_length=500)
    radiologia: str = Field(default="", max_length=500)
    otros: str = Field(default="", max_length=500)
    fecha: date = Field()
    observaciones: str | None = Field(default=None, max_length=1000)

    # Relaciones
    cardiologico_examen_medico_relation: "ExamenMedico" = Relationship(
        back_populates="examen_medico_cardiologico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    cardiologico_ergometria_relation: "Ergometria" = Relationship(
        back_populates="ergometria_cardiologico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    cardiologico_declaracion_jurada_relation: "DeclaracionJurada" = Relationship(
        back_populates="declaracion_jurada_cardiologico_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    # @validator("fecha")
    # def validar_fecha(cls, v):
    #    if v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"Cardiologico(id={self.id}, fecha={self.fecha})"
