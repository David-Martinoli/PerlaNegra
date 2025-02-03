import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..personal.personal import Personal
    from .tipo_actividad_fisica import TipoActividadFisica
    from .examen_medico import ExamenMedico
    from .laboratorio import Laboratorio
    from .cardiologico import Cardiologico
    from .declaracion_sintoma import DeclaracionSintoma
    from .escaneo_anexo import EscaneoAnexo


class DeclaracionJurada(rx.Model, TimestampMixin, table=True):
    """Modelo para declaraciones juradas de salud."""

    __tablename__ = "declaracionjurada"

    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    actividad_fisica_id: int | None = Field(foreign_key="tipoactividadfisica.id")
    examen_medico_id: int | None = Field(foreign_key="examenmedico.id")
    laboratorio_id: int | None = Field(foreign_key="laboratorio.id")
    cardiologicos_id: int | None = Field(foreign_key="cardiologico.id")

    # Síntomas Respiratorios
    fatiga_facil: bool = Field(default=False)
    falta_aire: bool = Field(default=False)
    tos_cronica: bool = Field(default=False)

    # Cardiovascular
    hipertension: bool = Field(default=False)
    dolor_pecho: bool = Field(default=False)
    palpitaciones: bool = Field(default=False)
    edemas: bool = Field(default=False)

    # Condiciones Crónicas
    anemia: bool = Field(default=False)
    diabetes: bool = Field(default=False)
    covid19: bool = Field(default=False)

    # Medicación
    medicacion_recetada: bool = Field(default=False)
    texto_medicacion_recetada: str | None = Field(default=None, max_length=500)
    medicacion_no_recetada: bool = Field(default=False)

    # Sistema Digestivo/Urinario
    sangrado_anormal: bool = Field(default=False)
    hemorragias: bool = Field(default=False)
    dolor_abdominal: bool = Field(default=False)
    dolor_orinar: bool = Field(default=False)

    # Traumatismos/Cirugías
    esguinces: bool = Field(default=False)
    fracturas: bool = Field(default=False)
    lumbago: bool = Field(default=False)
    cirugias: bool = Field(default=False)

    # Ginecología
    embarazo: bool = Field(default=False)
    complicaciones_embarazo: bool = Field(default=False)

    internaciones: bool = Field(default=False)

    # Neurológico/Psicológico
    cefaleas: bool = Field(default=False)
    desmayos: bool = Field(default=False)
    epilepsia: bool = Field(default=False)
    depresion: bool = Field(default=False)
    vertigos: bool = Field(default=False)
    insomnio: bool = Field(default=False)

    # Hábitos
    consumo_tabaco: bool = Field(default=False)
    cantidad_tabaco: str | None = Field(default=None, max_length=500)
    consumo_alcohol: bool = Field(default=False)
    consumo_drogas: bool = Field(default=False)

    requirio_oxigeno: bool = Field(default=False)

    otros_antecedentes: str | None = Field(default=None, max_length=500)
    fecha_anexo: date = Field()
    fecha_hora_carga: datetime = datetime.now(timezone.utc)
    tiempo_caducidad: int = Field(default=0)

    observaciones: str | None = Field(default=None, max_length=1000)

    # Relaciones
    declaracion_jurada_personal_relation: "Personal" = Relationship(
        back_populates="personal_declaracion_jurada_relation"
    )
    declaracion_jurada_tipo_actividad_fisica_relation: "TipoActividadFisica" = (
        Relationship(back_populates="tipo_actividad_fisica_declaracion_jurada_relation")
    )
    declaracion_jurada_examen_medico_relation: "ExamenMedico" = Relationship(
        back_populates="examen_medico_declaracion_jurada_relation"
    )
    declaracion_jurada_laboratorio_relation: "Laboratorio" = Relationship(
        back_populates="laboratorio_declaracion_jurada_relation"
    )
    declaracion_jurada_cardiologico_relation: "Cardiologico" = Relationship(
        back_populates="cardiologico_declaracion_jurada_relation"
    )
    declaracion_jurada_declaracion_sintoma_relation: list["DeclaracionSintoma"] = (
        Relationship(back_populates="declaracion_sintoma_declaracion_jurada_relation")
    )
    declaracion_jurada_escaneo_anexo_relation: list["EscaneoAnexo"] = Relationship(
        back_populates="escaneo_anexo_declaracion_jurada_relation"
    )

    # @validator("fecha")
    # def validar_fecha(cls, v):
    #    if v > date.today():
    #        raise ValueError("La fecha no puede ser futura")
    #    return v

    def __repr__(self) -> str:
        return f"DeclaracionJurada(personal_id={self.personal_id}, fecha={self.fecha})"
