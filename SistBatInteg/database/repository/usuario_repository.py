from ..models.permisos.usuario import Usuario
from ...database.connect_db import connect
from sqlmodel import Session, select


def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Usuario)
        return session.exec(query).all()
