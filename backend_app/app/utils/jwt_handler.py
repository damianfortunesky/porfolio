# Archivo para manejar la lógica de generación y validación de tokens JWT.

# Responsabilidades:

# Crear tokens JWT con un payload y tiempo de expiración.
# Validar tokens JWT.
# Extraer información del token.

from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def create_access_token(data: dict) -> str:
    """
    Genera un token JWT con una expiración.
    :param data: Diccionario con los datos que quieres incluir en el token.
    :return: Token JWT como cadena.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
