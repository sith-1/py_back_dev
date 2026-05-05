# src/use_cases/tasks/get_task.py
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from src.schemas.task import TaskSchema
from src.storage import tasks_storage


class Input(BaseModel):
    id: int


class Output(BaseModel):
    task: Optional[TaskSchema]


def handle(data: Input) -> Output:
    # HTTP-ошибка — ответственность роутера, тут только бизнес-результат
    return Output(task=tasks_storage.get_task_by_id(data.id))

