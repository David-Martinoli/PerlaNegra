# from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy import create_engine
from sqlmodel import create_engine
from reflex import Config


DATABASE_URL = "sqlite:///mydatabase.db"
# db_url: str = "sqlite:///:memory:"
config = Config(
    app_name="SistBatInteg",
    database_url=DATABASE_URL
)


# engine = create_engine(DATABASE_URL, echo=True)
# Session = scoped_session(sessionmaker(bind=engine))


# def get_session():
#    return Session()


def connect():
    engine = create_engine(DATABASE_URL)
    return engine
