# API de Gestión de Tareas con FastAPI

Este proyecto es una API RESTful para manejar tareas. Usa FastAPI, SQLModel y SQLite, y está dockerizado con Uvicorn.

---

## Endpoints

| Método | Ruta             | Descripción              |
|--------|------------------|--------------------------|
| GET    | `/tasks`         | Listar todas las tareas  |
| POST   | `/tasks`         | Crear nueva tarea        |
| PATCH  | `/tasks/{id}`    | Actualizar estado        |
| DELETE | `/tasks/{id}`    | Eliminar tarea           |

---

## Ejecutar en local

1. Crear entorno virtual y activar:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar API:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Probar: puede añadir, listar o borrar tareas desde <http://127.0.0.1:8000/docs/>

---

## Personalizar la aplicación

Modificar la aplicación para añadir una nueva ruta que muestre la versión de la aplicación junto con su nombre y apellidos. 

Los más directo es añadir el siguiente código en `main.py`:

```python
app.include_router(tasks.router)

# Código que se añade
@app.get("/version")
def version():
    return {"message": "Apellidos, Nombre - v0"}
``` 

--- 

## Ejecutar aplicación con Docker


```bash
docker build -t taskmanager .
docker run -p 80:8000 taskmanager
```

---


### Anexos

## Estructura del Proyecto

```
fastapi_taskmanager/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routers/
│       └── tasks.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

---

## Tecnologías usadas

- FastAPI
- SQLModel (ORM basado en Pydantic + SQLAlchemy)
- SQLite
- Uvicorn
- Docker