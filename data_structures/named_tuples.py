"""Namedtuples are a specific data structure available in Python's collections module, which are used to create
simple, immutable objects for storing data. They are similar to regular tuples but have named fields or attributes,
making it easier to work with structured data. Namedtuples provide a more readable and self-documenting way to define
and access elements within the tuple.

"""

from collections import namedtuple


class Person:
    """A simple named tuple representing a person's information."""

    def __init__(self, name: str, age: int):
        """
        Initialize a Person instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age


# Define a Person namedtuple
Person = namedtuple('Person', ['name', 'age'])

# Create an instance of the Person namedtuple
person1 = Person(name='Alice', age=30)

# Access fields by name
print(person1.name)  # Output: 'Alice'
print(person1.age)  # Output: 30


# ========================================== Built-in methods ===========================================

# Define a namedtuple type 'Person' with fields 'name' and 'age'
Person = namedtuple('Person', ['name', 'age'])

# Creating instances
person1 = Person('Alice', 30)
person2 = Person('Bob', 25)

# Accessing fields by name
print(person1.name)  # Output: 'Alice'
print(person2.age)   # Output: 25

# Unpacking namedtuples
name, age = person1
print(name, age)  # Output: 'Alice' 30

# _replace method to create a new namedtuple with modified fields
person3 = person1._replace(name='Eve')
print(person3)  # Output: Person(name='Eve', age=30)

# _asdict method to convert a namedtuple to a dictionary
person_dict = person1._asdict()
print(person_dict)  # Output: {'name': 'Alice', 'age': 30}

# _fields attribute to get a list of field names
field_names = Person._fields
print(field_names)  # Output: ['name', 'age']

# _make method to create a new namedtuple from an iterable
data = ('Charlie', 28)
person4 = Person._make(data)
print(person4)  # Output: Person(name='Charlie', age=28)
