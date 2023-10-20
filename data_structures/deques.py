"""Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list
in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides
an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.
FIFO (First-in, First-out) logic is used in deque.
"""

from collections import deque
from typing import Deque, Optional, List


class TaskQueue:
    """
    A class representing a task queue using a deque.
    """

    def __init__(self):
        """
        Initialize an empty task queue.
        """
        self.tasks: Deque[str] = deque()

    def add_task(self, task: str) -> None:
        """
        Add a task to the back of the queue.

        Args:
            task (str): The task to be added.
        """
        self.tasks.append(task)

    def remove_task(self) -> Optional[str]:
        """
        Remove and return a task from the front of the queue.

        Returns:
            str or None: The removed task if the queue is not empty, else None.
        """
        if self.tasks:
            return self.tasks.popleft()
        else:
            print("Queue is empty. No tasks to remove.")
            return None

    def add_task_to_front(self, task: str) -> None:
        """
        Add a task to the front of the queue.

        Args:
            task (str): The task to be added to the front.
        """
        self.tasks.appendleft(task)

    def view_tasks(self) -> List[str]:
        """
        View the tasks in the queue.

        Returns:
            List[str]: A list of tasks in the queue.
        """
        return list(self.tasks)


# Create a TaskQueue object
task_queue = TaskQueue()

# Add tasks to the queue
task_queue.add_task("Task 1")
task_queue.add_task("Task 2")
task_queue.add_task("Task 3")

# View the tasks in the queue
print("Tasks in the queue:", task_queue.view_tasks())

# Remove a task from the front of the queue
removed_task = task_queue.remove_task()
print("Removed task:", removed_task)
print("Tasks in the queue after removal:", task_queue.view_tasks())

# Add a task to the front of the queue
task_queue.add_task_to_front("Task 0")
print("Tasks in the queue after adding to the front:", task_queue.view_tasks())


# ========================================== collection module ================================================

# Create an empty deque
task_queue = deque()

# Add tasks to the back of the queue
task_queue.append("Task 1")
task_queue.append("Task 2")
task_queue.append("Task 3")

# View the tasks in the queue
print("Tasks in the queue:", list(task_queue))

# Remove a task from the front of the queue
removed_task = task_queue.popleft()
print("Removed task:", removed_task)
print("Tasks in the queue after removal:", list(task_queue))

# Add a task to the front of the queue
task_queue.appendleft("Task 0")
print("Tasks in the queue after adding to the front:", list(task_queue))


