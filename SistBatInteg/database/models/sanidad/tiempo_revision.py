import reflex as rx
from ..mixins.timestamp_mixin import TimestampMixin

class TiempoRevision(rx.Model, TimestampMixin, table=True):
    id: int = rx.Field(primary_key=True)
    valor: float