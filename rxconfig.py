import reflex as rx
from reflex import Config

class MyAppConfig(Config):
    db_url: str = "sqlite:///mydatabase.db"
    #db_url: str = "sqlite:///:memory:"
    app_name: str = "SistBatInteg"
    env: str = "dev"    # Use "prod" for production
    debug: bool = True  # Set to False in production
    #loglevel: LogLevel = LogLevel.DEFAULT
    frontend_port: int = 3000
    backend_port: int = 8000
    session_secret: str = "my_secret_key"
    # engine = rx.create_engine(DATABASE_URL, echo=True)
    #Session = rx.scoped_session(sessionmaker(bind=engine))
    #session = rx.session(db_url)
    #session.bind = rx.session(db_url, echo=True)



config = MyAppConfig()