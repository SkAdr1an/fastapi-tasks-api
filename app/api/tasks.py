from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import SQLModel, Field, Session, select
from app.core.deps import get_session

class TaskBase(SQLModel):
    title: str
    done: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    done: Optional[bool] = None

router = APIRouter()

@router.get("/", response_model=List[TaskRead])
def list_tasks(session: Session = Depends(get_session)):
    return session.exec(select(Task)).all()

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, session: Session = Depends(get_session)):
    task = Task.from_orm(data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, data: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for k, v in data.dict(exclude_unset=True).items():
        setattr(task, k, v)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return None
