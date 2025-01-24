import reflex as rx
import uuid  # https://docs.python.org/3/library/uuid.html
from sqlmodel import Field
from datetime import datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class ActuacionDisciplinariaScan(rx.Model, TimestampMixin, table=True):
    # id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)       # PARA USO CON UUID
    id: int | None = Field(default=None, primary_key=True)
    imagen: str
    descripcion: str
    actuacion_disciplinaria_id: int | None = Field(
        foreign_key="actuaciondisciplinaria.id"
    )
    created_at: datetime | None = Field(
        default=None,
        nullable=True,
        sa_column_kwargs={"default": datetime.now(timezone.utc)},
    )
