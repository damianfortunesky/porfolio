# Archivo donde defines las rutas públicas de la API para registro y login.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenSchema
from app.services.auth_service import register_user, authenticate_user

auth_router = APIRouter()

@auth_router.post("/register", status_code=201)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    Ruta para registrar nuevos usuarios.
    """
    try:
        user_id = register_user(request, db)
        return {"message": "Usuario registrado exitosamente", "user_id": user_id}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")


@auth_router.post("/login", response_model=TokenSchema)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Ruta para iniciar sesión y devolver un token JWT.
    """
    try:
        token = authenticate_user(request, db)
        return token
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

