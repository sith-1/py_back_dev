# src/routers/api.py
from typing import List

from fastapi import APIRouter, HTTPException, status

from src.schemas.task import CreateTaskSchema, TaskSchema
from src.use_cases.tasks import create_task, get_task, list_tasks

router = APIRouter()


@router.post("/tasks", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(payload: CreateTaskSchema) -> TaskSchema:
    result = create_task.handle(
        create_task.Input(
            title=payload.title,
            description=payload.description,
            status=payload.status,
        )
    )
    return result.task


@router.get("/tasks", response_model=List[TaskSchema])
def list_tasks_endpoint() -> List[TaskSchema]:
    result = list_tasks.handle(list_tasks.Input())
    return result.tasks


@router.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task_endpoint(task_id: int) -> TaskSchema:
    result = get_task.handle(get_task.Input(id=task_id))
    if result.task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result.task

