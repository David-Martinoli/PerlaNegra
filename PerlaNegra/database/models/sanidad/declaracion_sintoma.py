import reflex as rx
from datetime import datetime, timezone
from sqlmodel import Field, func
from ..mixins.timestamp_mixin import TimestampMixin


class DeclaracionSintoma(rx.Model, TimestampMixin, table=True):
    __tablename__ = "declaracionsintoma"
    id: int | None = Field(default=None, primary_key=True)
    declaracionjurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    sintoma_id: int | None = Field(foreign_key="sintoma.id")
    respuesta: str
    gravedad: str
    observacion: str
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"server_default": func.now()},
    )
