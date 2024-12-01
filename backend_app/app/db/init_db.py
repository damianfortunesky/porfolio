from app.db.base import Base
from app.db.session import engine
from app.models import user  # Importa todos los modelos

# Crear las tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)
