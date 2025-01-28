import reflex as rx
from sqlmodel import Field, func, Relationship
from datetime import date, datetime
from ..mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Importaciones condicionales para evitar circulares
    from .personal import Personal
    from .clase import Clase
    from .categoria_personal import CategoriaPersonal


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
    clase_id: int | None = Field(foreign_key="clase.id")  # civil o militar

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
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now()},
    )

    # Relaciones
    personals_personal_relation: list["Personal"] = Relationship(
        back_populates="personal_personals_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personals_clase_relation: "Clase" = Relationship(
        back_populates="clase_personals_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )
    personals_categoria_personal_relation: "CategoriaPersonal" = Relationship(
        back_populates="categoria_personal_personals_relation",
        sa_relationship_kwargs={"lazy": "joined"},
    )

    @property
    def antiguedad(self) -> int:
        """Retorna la antigüedad en años desde la fecha de ingreso."""
        today = date.today()
        return (today - self.fecha_ingreso).days // 365

    @property
    def antiguedad_unidad(self) -> int:
        """Retorna la antigüedad en años en la unidad actual."""
        today = date.today()
        return (today - self.fecha_ingreso_unidad).days // 365
