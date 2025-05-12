from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import Task
from app.database import engine

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
def read_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()


@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


@router.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, completed: bool):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task.completed = completed
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return {"ok": True}
