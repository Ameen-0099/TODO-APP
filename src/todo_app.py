"""
This module contains the core application logic for the Todo application.
"""
from typing import List
from .models import Task

class TodoApp:
    """Manages the application's core functionality and state."""
    def __init__(self):
        """Initializes the TodoApp with an in-memory task store."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """
        Adds a new task to the store.

        Args:
            title: The title of the task.
            description: The description of the task.

        Returns:
            The newly created Task object.
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the store.

        Returns:
            A list of all Task objects.
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Task | None:
        """
        Retrieves a single task by its ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task object if found, otherwise None.
        """
        return self._tasks.get(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            True if the task was deleted successfully, False otherwise.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def update_task(self, task_id: int, title: str, description: str) -> Task | None:
        """
        Updates a task's title and description.

        Args:
            task_id: The ID of the task to update.
            title: The new title for the task.
            description: The new description for the task.

        Returns:
            The updated Task object if found, otherwise None.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.title = title
            task.description = description
            return task
        return None

    def update_task_status(self, task_id: int, status: str) -> Task | None:
        """
        Updates a task's status.

        Args:
            task_id: The ID of the task to update.
            status: The new status for the task.

        Returns:
            The updated Task object if found, otherwise None.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            return task
        return None
