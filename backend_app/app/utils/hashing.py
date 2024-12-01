# Archivo para manejar el hashing de contraseñas.

# Hashear contraseñas con una librería segura como bcrypt.
#Verificar contraseñas al compararlas con el hash almacenado.

from passlib.context import CryptContext
from typing import Optional

# Configurar el contexto de Passlib con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> Optional[str]:
    """
    Genera el hash de una contraseña.
    
    :param password: Contraseña en texto plano.
    :return: Contraseña hasheada o None si falla el hashing.
    """
    try:
        return pwd_context.hash(password)
    except Exception as e:
        # Puedes manejar errores de forma más específica si es necesario
        print(f"Error al generar el hash de la contraseña: {e}")
        return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    
    :param plain_password: Contraseña en texto plano.
    :param hashed_password: Contraseña hasheada.
    :return: True si coinciden, False de lo contrario.
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        # Puedes manejar errores de forma más específica si es necesario
        print(f"Error al verificar la contraseña: {e}")
        return False
