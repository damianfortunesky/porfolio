# Para interactuar con la base de datos, necesitas usar sesiones. Configura una dependencia en FastAPI para manejar las sesiones.

from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.session import SessionLocal

# Crear una dependencia para obtener una sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
