"""A dictionary in Python is a built-in data structure that allows you to store a collection of key-value pairs. It
is also known as an associative array, hash map, or hash table in other programming languages. Dictionaries are
widely used because they provide efficient access to values based on their keys.

Here's how dictionaries work and some key points:

Key-Value Pairs: A dictionary stores data in the form of key-value pairs. Each key is unique, and it maps to a
corresponding value. Keys are typically strings, numbers, or immutable objects, while values can be of any data type,
including other dictionaries.

Unordered: Dictionaries are unordered collections in Python, meaning the order of key-value pairs is not guaranteed.
However, starting from Python 3.7 and later, dictionaries maintain insertion order, so they appear ordered in practice.

Accessing Values: You can access a value in a dictionary by using its key. This is a very efficient operation,
as dictionaries use a hashing mechanism to find values based on their keys.

Modifiability: Dictionaries are mutable, which means you can add, update, or remove key-value pairs.

Keys Must Be Unique: In a dictionary, keys must be unique. If you try to add a new key with an existing key,
it will update the existing key's value."""

from typing import Dict, Optional


class EmployeeDirectory:
    """
    A class for managing an employee directory using a dictionary.
    """

    def __init__(self):
        """
        Initialize an empty employee directory.
        """
        self.directory: Dict[int, Dict[str, str]] = {}

    def add_employee(self, employee_id: int, name: str, department: str) -> None:
        """
        Add an employee to the directory.

        Args:
            employee_id (int): The unique identifier for the employee.
            name (str): The employee's name.
            department (str): The department where the employee works.
        """
        self.directory[employee_id] = {"name": name, "department": department}

    def get_employee_info(self, employee_id: int) -> Optional[Dict[str, str]]:
        """
        Retrieve information about an employee based on their ID.

        Args:
            employee_id (int): The unique identifier for the employee.

        Returns:
            dict or None: A dictionary containing the employee's name and department, or None if the employee is not found.
        """
        return self.directory.get(employee_id, None)

    def remove_employee(self, employee_id: int) -> None:
        """
        Remove an employee from the directory based on their ID.

        Args:
            employee_id (int): The unique identifier for the employee.
        """
        if employee_id in self.directory:
            del self.directory[employee_id]


# Create an EmployeeDirectory object
directory = EmployeeDirectory()

# Add employees to the directory
directory.add_employee(101, "John Doe", "HR")
directory.add_employee(102, "Jane Smith", "Marketing")
directory.add_employee(103, "Alice Johnson", "Engineering")

# Retrieve and print employee information
employee_info = directory.get_employee_info(102)
if employee_info:
    print("Employee 102 Info:", employee_info)
else:
    print("Employee not found.")

# Remove an employee from the directory
directory.remove_employee(101)

# Print the updated directory
print("Updated Employee Directory:", directory.directory)
