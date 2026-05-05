# src/use_cases/tasks/list_tasks.py
from typing import List

from pydantic import BaseModel

from src.schemas.task import TaskSchema
from src.storage import tasks_storage


class Input(BaseModel):
    pass


class Output(BaseModel):
    tasks: List[TaskSchema]


def handle(_: Input) -> Output:
    return Output(tasks=tasks_storage.list_tasks())

