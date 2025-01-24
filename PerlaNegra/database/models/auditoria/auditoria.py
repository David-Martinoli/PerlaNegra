import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class Auditoria(rx.Model, TimestampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tabla_afectada: str
    registro_id: int | None
    campo_modificado: str = ""
    valor_anterior: str = ""
    valor_nuevo: str = ""
    modificado_por: str = ""
    fecha_modificacion: datetime = datetime.now(timezone.utc)
