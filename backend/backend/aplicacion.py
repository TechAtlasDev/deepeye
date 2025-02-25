# Importar las librerías (herramientas)
import fastapi # Programar la página web -> Para el backend
import requests # Nos permitirá "hablar" con el intermediario de shodan

import uvicorn

# Creando la aplicación
backend = fastapi.FastAPI()

# Configurar los cors-headers
@backend.middleware("http")
async def cors_headers(request, call_next):
    respuesta = await call_next(request)
    respuesta.headers["Access-Control-Allow-Origin"] = "*"
    return respuesta

# Crear una nueva ruta
@backend.get("/prueba") # http://backend/prueba
def prueba():
    return {"mensaje": "Hola mundo"} # El sistema nos dará el diccionario "mensaje": "Hola mundo"

# Crear ruta de busqueda
@backend.get("/buscar") # http://backend/buscar
def buscar(consulta, resultados, cantidad):
    URL_INTERMEDIARIO = "https://prl412-web-backend.vercel.app/api/search"
    DATOS = {
        "query": consulta,
        "facets": resultados,
        "limit": cantidad
    }
    respuesta = requests.post(url=URL_INTERMEDIARIO, data=DATOS)

    # Crear una variable que contenga la URL
    return respuesta.json() # Nos devolverá la respuesta del intermediario

def main():
    uvicorn.run(backend, host="0.0.0.0", port=8000)