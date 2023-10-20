"""A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO)
manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and
delete operations are often called push and pop."""

from typing import List, Any


class Stack:
    """
    A class representing a stack data structure.

    Attributes:
        stack (List): A list to store elements in the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.stack: List[Any] = []

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.

        Args:
            item (Any): The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self) -> Any:
        """
        Pop the top item from the stack and return it.

        Returns:
            Any: The popped item.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def peek(self) -> Any:
        """
        Peek at the top item of the stack without removing it.

        Returns:
            Any: The top item of the stack.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek at an empty stack.")

    def size(self) -> int:
        """
        Get the current size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)


# Create a stack
my_stack = Stack()

# Push elements onto the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# View the stack
print("Stack:", my_stack.stack)

# Peek at the top element
top_element = my_stack.peek()
print("Top element:", top_element)

# Pop an element from the stack
popped_element = my_stack.pop()
print("Popped element:", popped_element)

# Check if the stack is empty
print("Is the stack empty?", my_stack.is_empty())

# Get the current size of the stack
stack_size = my_stack.size()
print("Stack size:", stack_size)

# ============================================== Another example ==============================================

from typing import List, Any


def create_stack() -> List[Any]:
    """
    Create an empty stack.

    Returns:
        List: An empty list representing the stack.
    """
    return []


def is_empty(stack: List[Any]) -> bool:
    """
    Check if the stack is empty.

    Args:
        stack (List): The stack to check.

    Returns:
        bool: True if the stack is empty, False otherwise.
    """
    return len(stack) == 0


def push(stack: List[Any], item: Any) -> None:
    """
    Push an item onto the stack.

    Args:
        stack (List): The stack to push the item onto.
        item (Any): The item to be pushed onto the stack.
    """
    stack.append(item)


def pop(stack: List[Any]) -> Any:
    """
    Pop the top item from the stack and return it.

    Args:
        stack (List): The stack to pop from.

    Returns:
        Any: The popped item.
    """
    if not is_empty(stack):
        return stack.pop()
    else:
        raise IndexError("Stack is empty. Cannot pop from an empty stack.")


def peek(stack: List[Any]) -> Any:
    """
    Peek at the top item of the stack without removing it.

    Args:
        stack (List): The stack to peek at.

    Returns:
        Any: The top item of the stack.
    """
    if not is_empty(stack):
        return stack[-1]
    else:
        raise IndexError("Stack is empty. Cannot peek at an empty stack.")


def size(stack: List[Any]) -> int:
    """
    Get the current size of the stack.

    Args:
        stack (List): The stack to get the size of.

    Returns:
        int: The number of elements in the stack.
    """
    return len(stack)


# Create a stack
my_stack = create_stack()

# Push elements onto the stack
push(my_stack, 5)
push(my_stack, 10)
push(my_stack, 15)

# View the stack
print("Stack:", my_stack)

# Peek at the top element
top_element = peek(my_stack)
print("Top element:", top_element)

# Pop an element from the stack
popped_element = pop(my_stack)
print("Popped element:", popped_element)

# Check if the stack is empty
print("Is the stack empty?", is_empty(my_stack))

# Get the current size of the stack
stack_size = size(my_stack)
print("Stack size:", stack_size)


# ============================================ Another example ===========================================

from collections import deque

# Create an empty stack using a deque
stack = deque()

# Push elements onto the stack
stack.append(5)
stack.append(10)
stack.append(15)

# View the stack
print("Stack:", list(stack))

# Peek at the top element
top_element = stack[-1]
print("Top element:", top_element)

# Pop an element from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)

# Check if the stack is empty
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)

# Get the current size of the stack
stack_size = len(stack)
print("Stack size:", stack_size)
