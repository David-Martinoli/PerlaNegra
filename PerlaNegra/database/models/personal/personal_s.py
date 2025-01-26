import reflex as rx
from sqlmodel import Field, func
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalS(rx.Model, TimestampMixin, table=True):
    __tablename__ = "personals"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    fecha_ingreso: date
    fecha_ingreso_unidad: date
    fecha_ultimo_ascenso: date
    numero_legajo: str
    categoria_personal_id: int | None = Field(foreign_key="categoriapersonal.id")
    especialidad: str = ""
    grado: str = ""  #
    cuadro: str = ""  # E
    en_campo: str = ""  # 08
    nou: str = ""  # 0000
    funcion = ""
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = datetime.now(timezone.utc)
    clase_id: int | None = Field(foreign_key="clase.id")  # civil o militar
