"""
Lists and Python Arrays?
Lists are one of the most common data structures in Python, and a core part of the language.

Lists and arrays behave similarly.

Just like arrays, lists are an ordered sequence of elements.

They are also mutable and not fixed in size, which means they can grow and shrink throughout the life of the program.
Items can be added and removed, making them very flexible to work with.

However, lists and arrays are not the same thing.

Lists store items that are of various data types. This means that a list can contain integers, floating point
numbers, strings, or any other Python data type, at the same time. That is not the case with arrays.

As mentioned in the section above, arrays store only items that are of the same single data type. There are arrays
that contain only integers, or only floating point numbers, or only any other Python data type you want to use.

When to Use Python Arrays Lists are built into the Python programming language, whereas arrays aren't. Arrays are not
a built-in data structure, and therefore need to be imported via the array module in order to be used.

Arrays of the array module are a thin wrapper over C arrays, and are useful when you want to work with homogeneous data.

They are also more compact and take up less memory and space which makes them more size efficient compared to lists.

If you want to perform mathematical calculations, then you should use NumPy arrays by importing the NumPy package.
Besides that, you should just use Python arrays when you really need to, as lists work in a similar way and are more
flexible to work with."""

# ====================================================================================================
# ========================================== How to Use Arrays in Python =============================
import array as arr

# how to create an array
arr.array()
"""
The general syntax for creating an array looks like this:
    # variable_name = array(typecode,[elements])
"""
numbers = arr.array('i', [10, 20, 30])
"""
    Let's break it down:

    First we included the array module, in this case with import array as arr . Then, we created a numbers array. We 
    used arr.array() because of import array as arr . Inside the array() constructor, we first included i, 
    for signed integer. Signed integer means that the array can include positive and negative values. Unsigned 
    integer, with H for example, would mean that no negative values are allowed. Lastly, we included the values to be 
    stored in the array in square brackets."""

print(numbers)
# output
# array('i', [10, 20, 30])

# an array of floating point values
numbers = array('d', [10.0, 20.0, 30.0])

print(numbers)
# output
# array('d', [10.0, 20.0, 30.0])

# ==================================== How to indexing works Through an Array in Python ============================

# array_name[index_value_of_item]

print(numbers[0])  # gets the 1st element
print(numbers[1])  # gets the 2nd element
print(numbers[2])  # gets the 3rd element

# output
# 10
# 20
# 30

# ========================================== How to Loop Through an Array in Python ==================================

for number in numbers:
    print(number)

# output
# 10
# 20
# 30

# ========================================== How to Search Through an Array in Python ==================================

# search for the index of the value 10
print(numbers.index(10))
# output
# 0

# ========================================== How to Slice Through an Array in Python ==================================

# get the values 10 and 20 only
print(numbers[:2])  # first to second position

# output

# array('i', [10, 20])

# ========================================== How to Slice Through an Array in Python ==================================

# original array
numbers = arr.array('i', [10, 20, 30])

# add the integer 40 to the end of numbers
numbers.append(40)

print(numbers)

# output
# array('i', [10, 20, 30, 40])
# Note:  new item you add needs to be the same data type as the rest of the items in the array!
# further methods you can find: remove, insert, extend and so on.
