import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalS(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    apellido: str
    fecha_ingreso: date
    fecha_ingreso_unidad: date
    numero_legajo: str
    categoria_personal_id: int = Field(foreign_key="categoriapersonal.id")
    arma_especialidad: str = ""
    grado: str = ""  #
    cuadro: str = ""  # E
    en_campo: str = ""  # 08
    creado_en: datetime = datetime.now(timezone.utc)
    actualizado_en: datetime = datetime.now(timezone.utc)
    clase_id: int = Field(foreign_key="clase.id")
