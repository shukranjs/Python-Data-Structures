"""
Python Data Structures: Tuple Example

Tuples are ordered, immutable collections of items. They are similar to lists, but unlike lists, tuples cannot be modified once created.

In this script, we'll create and use tuples, demonstrating their immutability and common operations.

Author: [Your Name]
Date: [Date]
"""

from typing import Tuple
from typing import Set

# Create a tuple of fruits with type hints
fruits: Tuple[str, str, str] = ('apple', 'banana', 'cherry')

# Access elements in a tuple
first_fruit: str = fruits[0]
print("First fruit:", first_fruit)  # Output: First fruit: apple

# Attempt to modify a tuple (This will raise an error)
# fruits[0] = 'orange'  # TypeError: 'tuple' object does not support item assignment

# Concatenate tuples
more_fruits: Tuple[str, str] = ('orange', 'grape')
combined_fruits: Tuple[str, str, str, str] = fruits + more_fruits
print("Combined fruits:", combined_fruits)  # Output: Combined fruits: ('apple', 'banana', 'cherry', 'orange', 'grape')

# Slicing tuples
sliced_fruits: Tuple[str, str] = combined_fruits[1:3]
print("Sliced fruits:", sliced_fruits)  # Output: Sliced fruits: ('banana', 'cherry')

# ==========================================================================================================

"""
Python Sets: Class Example

Sets are unordered collections of unique elements. In this script, we'll create a class that uses sets to manage a list of unique students' IDs.

Author: [Your Name]
Date: [Date]
"""


class StudentDatabase:
    def __init__(self):
        """
        Initialize an empty student database.
        """
        self.student_ids: Set[int] = set()

    def add_student(self, student_id: int) -> None:
        """
        Add a student's ID to the database.

        Args:
            student_id (int): The unique ID of the student to be added.
        """
        self.student_ids.add(student_id)

    def remove_student(self, student_id: int) -> None:
        """
        Remove a student's ID from the database.

        Args:
            student_id (int): The unique ID of the student to be removed.
        """
        self.student_ids.discard(student_id)

    def get_student_ids(self) -> Set[int]:
        """
        Get the set of unique student IDs in the database.

        Returns:
            Set[int]: A set of unique student IDs.
        """
        return self.student_ids


# Create a StudentDatabase instance
student_db = StudentDatabase()

# Add student IDs to the database
student_db.add_student(101)
student_db.add_student(102)
student_db.add_student(103)
student_db.add_student(104)
student_db.add_student(101)  # Adding a duplicate ID (won't be stored)

# Remove a student from the database
student_db.remove_student(103)

# Retrieve the set of unique student IDs
unique_ids = student_db.get_student_ids()

print("Unique Student IDs:", unique_ids)  # Output: Unique Student IDs: {101, 102, 104}
