import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class DeclaracionJurada(rx.Model, TimestampMixin, table=True):
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
