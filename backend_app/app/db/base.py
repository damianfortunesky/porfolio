# Crea un archivo app/db/base.py para definir la clase base de SQLAlchemy, que usarán tus modelos.

from sqlalchemy.ext.declarative import declarative_base

# Clase base para los modelos
Base = declarative_base()
