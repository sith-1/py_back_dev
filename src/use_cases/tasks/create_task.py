# src/use_cases/tasks/create_task.py
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from src.schemas.task import TaskSchema, TaskStatus
from src.storage import tasks_storage


class Input(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: TaskStatus


class Output(BaseModel):
    task: TaskSchema


def handle(data: Input) -> Output:
    task = tasks_storage.add_task(
        title=data.title,
        description=data.description,
        status=data.status,
    )
    return Output(task=task)

