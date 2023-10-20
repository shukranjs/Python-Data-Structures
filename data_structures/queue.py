"""A queue is a common data structure in computer science and programming that operates
on a "first-in, first-out" (FIFO) basis. It's a linear data structure that follows a specific order for adding and
removing elements. In a queue, the first element added to the queue is the first one to be removed, similar to people
waiting in a line (queue) for a service, like in a supermarket checkout.

Key characteristics of a queue:

FIFO Order: The fundamental principle of a queue is to maintain the order in which elements were added. The element
that has been in the queue the longest (the front) is the first to be removed.

Two Primary Operations:

Enqueue (Add): Adding an element to the back (or rear) of the queue. This operation is also known as "push" or
"insert." Dequeue (Remove): Removing the element from the front (or head) of the queue. This operation is also known
as "pop." Peek Operation: A method to look at the front element without removing it. It allows you to inspect the
element that will be dequeued next.

Size Operation: A method to determine the number of elements currently in the queue."""

from typing import Any


class Queue:
    """A simple queue data structure implemented in Python."""

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the end of the queue.

        Args:
            item (Any): The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the item from the front of the queue.

        Returns:
            Any: The item removed from the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self) -> Any:
        """
        Get the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue.
        """
        if not self.is_empty():
            return self.items[0]


# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: Queue size: 3
print("Front of the queue:", queue.peek())  # Output: Front of the queue: 1

item = queue.dequeue()
print("Dequeued item:", item)  # Output: Dequeued item: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2

# ==========================================================================================================

# Initialize an empty list to represent the queue
queue = []

# Enqueue (add) elements to the back of the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Display the queue
print("Queue:", queue)  # Output: Queue: [1, 2, 3]

# Dequeue (remove) elements from the front of the queue
if queue:
    front_element = queue.pop(0)
    print("Dequeued element:", front_element)  # Output: Dequeued element: 1
else:
    print("Queue is empty")

# Peek at the front element without removing it
if queue:
    front_element = queue[0]
    print("Front element:", front_element)  # Output: Front element: 2
else:
    print("Queue is empty")

# Determine the size of the queue
queue_size = len(queue)
print("Queue size:", queue_size)  # Output: Queue size: 2
