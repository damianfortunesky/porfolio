# Archivo con los modelos de entrada y salida relacionados con autenticación. (Pydantic)

# Definir esquema para Registro (RegisterRequest, RegisterResponse).
# Definir esquema para Login (LoginRequest, LoginResponse).
# Definir esquema para Token (TokenSchema).

from pydantic import BaseModel, EmailStr, Field

# Solicitud para el registro
class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


# Solicitud para el login
class LoginRequest(BaseModel):
    username: str
    password: str


# Respuesta para el token JWT
class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
