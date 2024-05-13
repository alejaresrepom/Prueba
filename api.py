from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.utils import get_openapi
import json

# Crea una instancia de FastAPI
app = FastAPI()

# Define el esquema de autenticación básica
security = HTTPBasic()

# Lee los datos del archivo JSON
with open('archivo.json', 'r') as file:
    datos = json.load(file)

# Define la función para verificar las credenciales
def verificar_credenciales(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"  # Cambia esto por tu nombre de usuario
    correct_password = "admin"  # Cambia esto por tu contraseña

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Define el endpoint para obtener todos los libros
@app.get("/libros/")
async def obtener_libros(username: str = Depends(verificar_credenciales)):
    return datos['tabla']

# Personaliza la documentación de OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API de Libros",
        version="1.0.0",
        description="Esta es una API para acceder a datos de libros",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
