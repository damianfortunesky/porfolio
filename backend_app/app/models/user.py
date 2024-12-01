from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)  # Booleano que inicia como True
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # Fecha de creación automática con zona horaria UTC
    deactivated_at = Column(DateTime, nullable=True)  # Fecha de baja que inicia como NULL

