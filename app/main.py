from fastapi import FastAPI
from app.routers import tasks
from app.database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    """Evento que se ejecuta al iniciar la aplicación."""
    create_db_and_tables()


app.include_router(tasks.router)


@app.get("/version")
async def get_version():
    """Endpoint que devuelve la versión de la API."""
    return {"message": "Dominguez, Romeo - v06"}


@app.get("/tarea1")
async def ejecutar_tarea_backup():
    """Endpoint para la tarea de backup de base de datos."""
    return {"tarea": "Realizar backup de base de datos"}


@app.post("/tarea2")
async def procesar_archivos_csv():
    """Endpoint para procesar archivos CSV."""
    return {"tarea": "Procesar archivos CSV"}
