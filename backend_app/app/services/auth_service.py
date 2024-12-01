# Archivo que encapsula la lógica de negocio de autenticación.

# Manejar la lógica de registro:
# Validar si el usuario ya existe.
# Crear un nuevo usuario.
# Hashear la contraseña antes de guardarla en la base de datos.
# Manejar la lógica de login:
# Verificar las credenciales del usuario.
# Generar y devolver el token JWT.

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest
from app.utils.hashing import get_password_hash, verify_password
from app.utils.jwt_handler import create_access_token

def register_user(request: RegisterRequest, db: Session):
    """
    Lógica para registrar un usuario.
    """
    # Verificar si el usuario ya existe
    user_exists = db.query(User).filter(User.username == request.username).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe"
        )

    # Crear un nuevo usuario
    hashed_password = get_password_hash(request.password)
    new_user = User(
        username=request.username,
        email=request.email,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user.id


def authenticate_user(request: LoginRequest, db: Session):
    """
    Lógica para autenticar un usuario.
    """
    # Buscar el usuario en la base de datos
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no encontrado"
        )

    # Verificar la contraseña
    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta"
        )

    # Generar un token JWT
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
