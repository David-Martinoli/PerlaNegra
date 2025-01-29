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
    __tablename__ = "declaracionjurada"
    id: int | None = Field(default=None, primary_key=True)
    personal_id: int | None = Field(foreign_key="personal.id")
    fatiga_facil: bool = False
    falta_aire: bool = False
    tos_cronica: bool = False
    hipertension: bool = False
    dolor_pecho: bool = False
    palpitaciones: bool = False
    edemas: bool = False
    anemia: bool = False
    diabetes: bool = False
    covid19: bool = False
    medicacion_recetada: bool = False
    texto_medicacion_recetada: str = ""
    sangrado_anormal: bool = False
    hemorragias: bool = False
    dolor_abdominal: bool = False
    dolor_orinar: bool = False
    esguinces: bool = False
    fracturas: bool = False
    lumbago: bool = False
    cirugias: bool = False
    embarazo: bool = False
    internaciones: bool = False
    medicacion_no_recetada: bool = False
    complicaciones_embarazo: bool = False
    cefaleas: bool = False
    desmayos: bool = False
    epilepsia: bool = False
    depresion: bool = False
    vertigos: bool = False
    insomnio: bool = False
    consumo_tabaco: bool = False
    cantidad_tabaco: str = ""
    consumo_alcohol: bool = False
    consumo_drogas: bool = False
    requirio_oxigeno: bool = False
    actividad_fisica_id: int | None = Field(foreign_key="tipoactividadfisica.id")
    otros_antecedentes: str = ""
    fecha_anexo: date
    fecha_hora_carga: datetime = datetime.now(timezone.utc)
    tiempo_caducidad: int = 0
    examen_medico_id: int | None = Field(foreign_key="examenmedico.id")
    laboratorio_id: int | None = Field(foreign_key="laboratorio.id")
    cardiologicos_id: int | None = Field(foreign_key="cardiologico.id")

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
