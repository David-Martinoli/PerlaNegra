import reflex as rx
from datetime import datetime, timezone
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin


class DeclaracionSintoma(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    declaracionjurada_id: int | None = Field(foreign_key="declaracionjurada.id")
    sintoma_id: int | None = Field(foreign_key="sintoma.id")
    respuesta: str
    gravedad: str
    observacion: str
    created_at: datetime = datetime.now(timezone.utc)
