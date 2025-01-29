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
    __tablename__ = "cardiologico"
    id: int | None = Field(default=None, primary_key=True)
    examen_medico_id: int | None = Field(foreign_key="examenmedico.id")
    ecg: str = ""
    ergometria_id: int | None = Field(foreign_key="ergometria.id")
    radiologia: str = ""
    otros: str = ""
    fecha: date

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
