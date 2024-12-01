# Configuración de DB, URLs, etc.

from reflex import Config

DATABASE_URL = "sqlite:///mydatabase.db"
    #db_url: str = "sqlite:///:memory:" 
config = Config(database_url=DATABASE_URL)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(DATABASE_URL, echo=True)
Session = scoped_session(sessionmaker(bind=engine))

def get_session():
    return Session()