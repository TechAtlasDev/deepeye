# Importar las librerías (herramientas)
import fastapi # Programar la página web -> Para el backend
import requests # Nos permitirá "hablar" con el intermediario de shodan

# Creando la aplicación
backend = fastapi.FastAPI()

# Crear una nueva ruta
@backend.get("/prueba") # http://backend/prueba
def prueba():
    return {"mensaje": "Hola mundo"} # El sistema nos dará el diccionario "mensaje": "Hola mundo"

# Crear ruta de busqueda
@backend.get("/buscar/") # http://backend/buscar
def buscar(consulta):
    # Crear una variable que contenga la URL
    return {"mensaje": f"Buscando {consulta}"} # El sistema nos dará el diccionario "mensaje": "Buscando {query}"