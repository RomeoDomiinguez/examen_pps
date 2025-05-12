from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import Task
from app.database import engine

router = APIRouter()


@router.get("/tasks", response_model=list[Task])
def read_tasks():
    """
    Obtiene todas las tareas existentes.

    Returns:
        list[Task]: Lista de todas las tareas en la base de datos.
    """
    with Session(engine) as session:
        return session.exec(select(Task)).all()


@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    """
    Crea una nueva tarea.

    Args:
        task (Task): Objeto Task con los datos de la nueva tarea.

    Returns:
        Task: La tarea recién creada con su ID asignado.
    """
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


@router.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, completed: bool):
    """
    Actualiza el estado de completado de una tarea.

    Args:
        task_id (int): ID de la tarea a actualizar.
        completed (bool): Nuevo estado de completado.

    Raises:
        HTTPException: 404 si la tarea no existe.

    Returns:
        Task: La tarea actualizada.
    """
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        task.completed = completed
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Elimina una tarea existente.

    Args:
        task_id (int): ID de la tarea a eliminar.

    Raises:
        HTTPException: 404 si la tarea no existe.

    Returns:
        dict: Confirmación de eliminación.
    """
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        session.delete(task)
        session.commit()
        return {"ok": True}
