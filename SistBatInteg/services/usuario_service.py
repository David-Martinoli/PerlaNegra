from ..database.models.permisos.usuario import Usuario
from datetime import datetime, timezone
from typing import Optional, Tuple

class UsuarioService:
    @staticmethod
    async def crear_usuario(
        nombre_usuario: str,
        contrasena: str,
        personal_id: int
    ) -> Tuple[Optional[Usuario], str]:
        """
        Crea un nuevo usuario en la base de datos.
        
        Returns:
            Tupla (Usuario, mensaje_error). Si hay error, Usuario será None
        """
        try:
            # Verificar si el usuario ya existe
            usuario_existente = await Usuario.select().where(
                Usuario.nombre_usuario == nombre_usuario
            ).execute().first()
            
            if usuario_existente:
                return None, "El nombre de usuario ya está en uso"
                
            # Crear nuevo usuario
            nuevo_usuario = Usuario(
                nombre_usuario=nombre_usuario,
                hash_contrasena=contrasena,
                personal_id=personal_id,
                creado_en=datetime.now(timezone.utc),
                cambiar_contrasena=False
            )
            
            # Guardar en la base de datos
            await nuevo_usuario.save()
            return nuevo_usuario, ""
            
        except Exception as e:
            error_msg = f"Error en la base de datos: {str(e)}"
            print(error_msg)  # Para logging
            return None, error_msg