# src/schemas/task.py
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class CreateTaskSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: TaskStatus


class TaskSchema(CreateTaskSchema):
    id: int

