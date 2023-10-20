# Sets in Python are an unordered collection of unique elements. They are commonly used
# when you need to store a collection of items where uniqueness is essential.

from typing import Set

# Create an empty set
my_set: Set[int] = set()

# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Display the set
print("Set:", my_set)  # Output: Set: {1, 2, 3}

# Remove elements from the set
my_set.remove(2)
my_set.discard(4)  # Discarding an element not in the set is safe

# Check if an element is in the set
element_exists = 3 in my_set

# Determine the size of the set
set_size = len(my_set)

# Create a new set from a list
new_set: Set[int] = set([3, 4, 5, 6])

# Perform set operations: union, intersection, and difference
union_set = my_set | new_set
intersection_set = my_set & new_set
difference_set = my_set - new_set

# Display the results of set operations
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

# Clear all elements from the set
my_set.clear()

# Verify if the set is empty
is_empty = not my_set

# Final set
print("Final Set:", my_set)

# Print the results of set operations
print("Is 3 in the set?", element_exists)  # Output: Is 3 in the set? True
print("Set size:", set_size)  # Output: Set size: 2
print("Is the set empty?", is_empty)  # Output: Is the set empty? True


# ==========================================================================================================

class SetOperations:
    """
    A class that demonstrates set operations in Python.
    Sets are an unordered collection of unique elements.
    They are commonly used when you need to store a collection of items where uniqueness is essential.
    """

    def __init__(self):
        """
        Initialize an empty set.
        """
        self.my_set: Set[int] = set()

    def add_element(self, element: int) -> None:
        """
        Add an element to the set.

        Args:
            element (int): The element to be added to the set.
        """
        self.my_set.add(element)

    def remove_element(self, element: int) -> None:
        """
        Remove an element from the set.

        Args:
            element (int): The element to be removed from the set.
        """
        self.my_set.discard(element)

    def element_exists(self, element: int) -> bool:
        """
        Check if an element exists in the set.

        Args:
            element (int): The element to be checked.

        Returns:
            bool: True if the element exists in the set, False otherwise.
        """
        return element in self.my_set

    def set_size(self) -> int:
        """
        Get the size of the set.

        Returns:
            int: The number of elements in the set.
        """
        return len(self.my_set)

    def display_set(self) -> None:
        """
        Display the contents of the set.
        """
        print("Set:", self.my_set)


# Create an instance of the SetOperations class
set_operations = SetOperations()

# Add elements to the set
set_operations.add_element(1)
set_operations.add_element(2)
set_operations.add_element(3)

# Display the set
set_operations.display_set()  # Output: Set: {1, 2, 3}

# Remove an element from the set
set_operations.remove_element(2)

# Check if an element exists in the set
element_exists = set_operations.element_exists(3)

# Get the size of the set
set_size = set_operations.set_size()

# Display the set after removal
set_operations.display_set()  # Output: Set: {1, 3}

# Display the results
print("Is 3 in the set?", element_exists)  # Output: Is 3 in the set? True
print("Set size:", set_size)  # Output: Set size: 2
