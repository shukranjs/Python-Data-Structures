"""In Python, a "list" and a "linked list" are both data structures used to store collections of elements,
but they differ in how they are implemented and their characteristics. Here's a brief overview of the differences
between the two:

List (Python List):

Lists in Python are implemented as dynamic arrays. They are a built-in data structure in Python and are very commonly
used. Lists allow for efficient random access to elements because they are stored in contiguous memory locations.
Appending or removing elements from the end of a list is typically a fast operation, but inserting or deleting
elements in the middle of a list can be slower because it may require shifting elements. Lists can store elements of
different data types, and they are mutable, meaning you can change the elements after the list is created. Example:
my_list = [1, 2, 3, 4, 5] Linked List:

A linked list is a data structure where each element (node) contains a value and a reference (or link) to the next
element in the list. It's not a built-in data structure in Python but can be implemented using classes. Linked lists
are less memory-efficient than lists because of the additional memory required for storing references. Insertions and
deletions, especially at the beginning or middle of the list, are generally faster in a linked list because it
doesn't require shifting elements. However, random access can be slower as you need to traverse the list from the
beginning to reach a specific element. Linked lists can be more flexible in terms of data structure, and they can be
used to implement more complex data structures like stacks and queues."""

from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data: Any) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage:
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()  # Output: 1 -> 2 -> 3

linked_list.prepend(0)

linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

linked_list.delete(2)

linked_list.display()  # Output: 0 -> 1 -> 3


# =================================================== Circular Linked List ====================================

"""A circular linked list is a data structure used in computer science for organizing and storing a collection of 
elements, similar to a regular linked list. The key difference is that in a circular linked list, the last element of 
the list does not point to a null or None reference; instead, it points back to the first element, creating a closed 
loop or cycle."""
class CircularNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: Any) -> None:
        new_node = CircularNode(data)  # Updated the class name here
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data: Any) -> None:
        new_node = CircularNode(data)  # Updated the class name here
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def delete(self, data: Any) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def display(self) -> None:
        if self.head is None:
            return

        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(map(str, elements)))


circular_linked_list = CircularLinkedList()

circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)

circular_linked_list.display()  # Output: 1 -> 2 -> 3

circular_linked_list.prepend(0)

circular_linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

circular_linked_list.delete(2)

circular_linked_list.display()  # Output: 0 -> 1 -> 3
