# Configuración de DB, URLs, etc.

from reflex import Config

DATABASE_URL = "sqlite:///your_database_name.db"  # Cambiar por el motor de tu base de datos
config = Config(database_url=DATABASE_URL)