from enum import Enum
from pathlib import Path


ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
UPLOAD_PATH = Path("uploads/actuaciones")


class TipoDocumentoActuacion(str, Enum):
    RESOLUCION = "resolucion"
    INFORME = "informe"
    ANEXO = "anexo"
    OTRO = "otro"
