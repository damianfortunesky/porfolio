from fastapi import FastAPI
from app.api.v1.auth import auth_router

app = FastAPI()

# Registrar rutas
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
