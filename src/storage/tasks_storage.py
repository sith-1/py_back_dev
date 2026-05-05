# src/storage/tasks_storage.py
from __future__ import annotations

from threading import Lock
from typing import List, Optional

from src.schemas.task import TaskSchema, TaskStatus

_lock = Lock()
_tasks: List[TaskSchema] = []
_next_id = 1


def add_task(*, title: str, description: Optional[str], status: TaskStatus) -> TaskSchema:
    global _next_id

    with _lock:
        task = TaskSchema(id=_next_id, title=title, description=description, status=status)
        _tasks.append(task)
        _next_id += 1
        return task


def get_task_by_id(task_id: int) -> Optional[TaskSchema]:
    with _lock:
        for task in _tasks:
            if task.id == task_id:
                return task
    return None


def list_tasks() -> List[TaskSchema]:
    with _lock:
        return list(_tasks)

