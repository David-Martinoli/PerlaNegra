import reflex as rx
from sqlmodel import Field, Relationship
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actuacion_disciplinaria import ActuacionDisciplinaria
    from .personal_r import PersonalR
    from .personal_s import PersonalS
    from .actuacion import Actuacion
    from .atributo_personal import AtributoPersonal
    from .calificacion import Calificacion
    from .direccion import Direccion
    from .familiar import Familiar
    from .felicitacion import Felicitacion
    from .formacion_academica import FormacionAcademica
    from .inasistencia import Inasistencia
    from .movimiento_personal import MovimientoPersonal
    from .personal_seguro import PersonalSeguro
    from .sancion import Sancion
    from .telefono import Telefono
    from ..sanidad.examen_medico import ExamenMedico
    from ..sanidad.declaracion_jurada import DeclaracionJurada
    from ..sanidad.odontologico import Odontologico
    from ..sanidad.profesional_paciente import ProfesionalPaciente
    from ..sanidad.secreto_medico import SecretoMedico
    from ..sanidad.vacunacion import Vacunacion


class Personal(rx.Model, TimestampMixin, table=True):
    """Modelo unificado de personal que vincula datos personales y de servicio.

    Attributes:
        id: Identificador único
        personalR_id: ID de referencia a datos personales
        personalS_id: ID de referencia a datos de servicio
        datos_personales: Relación con datos personales
        datos_servicio: Relación con datos de servicio
        actuaciones: Lista de actuaciones disciplinarias
        actuaciones_como_actuante: Lista de actuaciones donde actúa como supervisor
    """

    __tablename__ = "personal"
    id: int | None = Field(default=None, primary_key=True)
    personalR_id: int | None = Field(
        foreign_key="personalr.id", nullable=False, ondelete="RESTRICT"
    )
    personalS_id: int | None = Field(
        foreign_key="personals.id", nullable=False, ondelete="RESTRICT"
    )
    activo: bool = Field(default=True)

    # Relaciones
    personal_personals_relation: "PersonalS" = Relationship(
        back_populates="personals_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_personalr_relation: "PersonalR" = Relationship(
        back_populates="personalr_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_actuacion_disciplinaria_personalid_relation: list[
        "ActuacionDisciplinaria"
    ] = Relationship(
        back_populates="actuacion_disciplinaria_personalid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ActuacionDisciplinaria.personal_id",
            "lazy": "joined",
        },
    )
    personal_actuacion_disciplinaria_actuanteid_relation: list[
        "ActuacionDisciplinaria"
    ] = Relationship(
        back_populates="actuacion_disciplinaria_actuanteid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ActuacionDisciplinaria.actuante_id",
            "lazy": "joined",
        },
    )
    personal_actuacion_personal_relation: list["Actuacion"] = Relationship(
        back_populates="actuacion_personal_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Actuacion.personal_id",
            "lazy": "joined",
        },
    )
    personal_actuacion_actuante_relation: list["Actuacion"] = Relationship(
        back_populates="actuacion_actuante_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Actuacion.actuante_id",
            "lazy": "joined",
        },
    )
    personal_atributo_personal_relation: list["AtributoPersonal"] = Relationship(
        back_populates="atributo_personal_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_calificacion_relation: list["Calificacion"] = Relationship(
        back_populates="calificacion_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    direccion_personal_relation: list["Direccion"] = Relationship(
        back_populates="personal_direccion_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_familiar_relation: list["Familiar"] = Relationship(
        back_populates="familiar_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    felicitacion_personal_quien_impone_relation: list["Felicitacion"] = Relationship(
        back_populates="personal_quien_impone_felicitacion_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.quien_impone",
            "lazy": "joined",
        },
    )
    personal_felicitacion_personal_relation: list["Felicitacion"] = Relationship(
        back_populates="personal_personal_felicitacion_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Felicitacion.personal_id",
            "lazy": "joined",
        },
    )
    personal_formacion_academica_relation: list["FormacionAcademica"] = Relationship(
        back_populates="formacion_academica_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_inasistencia_relation: list["Inasistencia"] = Relationship(
        back_populates="inasistencia_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_movimiento_personal_relation: list["MovimientoPersonal"] = Relationship(
        back_populates="movimiento_personal_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_personal_seguro_relation: list["PersonalSeguro"] = Relationship(
        back_populates="personal_seguro_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_sancion_personal_relation: list["Sancion"] = Relationship(
        back_populates="sancion_personal_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.personal_id",
            "lazy": "joined",
        },
    )
    personal_autoridad_sancion_relation: list["Sancion"] = Relationship(
        back_populates="sancion_personal_autoridad_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Sancion.autoridad_id",
            "lazy": "joined",
        },
    )
    personal_telefono_relation: list["Telefono"] = Relationship(
        back_populates="telefono_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_examen_medico_relation: list["ExamenMedico"] = Relationship(
        back_populates="examen_medico_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_declaracion_jurada_relation: list["DeclaracionJurada"] = Relationship(
        back_populates="declaracion_jurada_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_odontologico_relation: list["Odontologico"] = Relationship(
        back_populates="odontologico_personal_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personal_profesional_paciente_profesionalid_relation: list[
        "ProfesionalPaciente"
    ] = Relationship(
        back_populates="profesional_paciente_profesionalid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "ProfesionalPaciente.profesional_id",
            "lazy": "joined",
        },
    )
    personal_profesional_paciente_pacienteid_relation: list["ProfesionalPaciente"] = (
        Relationship(
            back_populates="profesional_paciente_pacienteid_personal_relation",
            sa_relationship_kwargs={
                "foreign_keys": "ProfesionalPaciente.paciente_id",
                "lazy": "joined",
            },
        )
    )
    personal_secreto_medico_profesionalid_relation: list["SecretoMedico"] = (
        Relationship(
            back_populates="secreto_medico_profesionalid_personal_relation",
            sa_relationship_kwargs={
                "foreign_keys": "SecretoMedico.profesional_id",
                "lazy": "joined",
            },
        )
    )
    personal_secreto_medico_pacienteid_relation: list["SecretoMedico"] = Relationship(
        back_populates="secreto_medico_pacienteid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "SecretoMedico.paciente_id",
            "lazy": "joined",
        },
    )
    personal_vacunacion_profesionalid_relation: list["Vacunacion"] = Relationship(
        back_populates="vacunacion_peofesionalid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.profesional_id",
            "lazy": "joined",
        },
    )
    personal_vacunacion_personalid_relation: list["Vacunacion"] = Relationship(
        back_populates="vacunacion_personalid_personal_relation",
        sa_relationship_kwargs={
            "foreign_keys": "Vacunacion.personal_id",
            "lazy": "joined",
        },
    )

    # @property
    # def nombre_completo(self) -> str:
    #    return self.datos_personales.nombre_completo if self.datos_personales else ""

    # @property
    # def legajo(self) -> str:
    #    return self.datos_servicio.numero_legajo if self.datos_servicio else ""

    def __repr__(self) -> str:
        return f"Personal(id={self.id})"
