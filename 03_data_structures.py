# Structured Data Types


## 1. List
## 2. Tuple
## 3. Dictionary
## 4. Set
## 5. Array

### Data Structure, is a way of organizing and storing data so it can be used efficiently.
## Built-in data structures:
# list[]
# tuple()
# set{}
# dict{}
## *Primitive Data Type (only one value):- Int, String, Boolean. But in real world we have multiple values.
## If we have multiple values for the same topic, then we use a container, a data structure in order to handle those values.

### Functions and Methods -
#### Function: costs = [10,20,15]
#               len(costs)
# input >> len >> output (3)
# Functions will not manipulate the original value, the input. It will just return a new value.
#### Method: costs = [10,20,15]
#               costs.remove(10)
# input >>< remove >> output (None, Nothing)
# Methods change directly the original value.


## 1. List
# Ordered collection of items, Changebale, Allows Duplicates.

# How to Create?
# How to Access & Read?
# How to Unpack?
# How to Explore & Analyze?
# How to Change?
# How to Order?
# How to Copy?
# How to Combine?
# How to Iterate?
# How to Transform?
# How to Filter?
# List Comprehensions.

# Create Lists:

# Create Empty List
empty = []
print(empty)
print(type(empty))
# Ans: [], <class 'list'>
# Create a List by adding items manually
letters = ['a', 'b', 'c']
print(letters)
print(type(letters))
# Ans: ['a', 'b', 'c'], <class 'list'>
# letters >> Object(list, Array) >pointer> Object(str, 'a')
# Create a List of numbers
numbers = [1, 2, 3]
print(numbers)
print(type(numbers))
# Ans: [1, 2, 3], <class 'list'>
# numbers >> Object(list, Array) >pointer> Object(int, 1)
# We can mix data types in the same list
mixed = [1, 'a', True, None]
print(mixed)
print(type(mixed))
# Ans: [1, 'a', True, None], <class 'list'>
# mixed >> Object(list, Array) >pointer> Objects{(int, 1), (str, 'a'), (bool, True), (None Type, )}
# Creation of List in Python by using built-in function list()
empty = list()
print(empty)
# list() - converts an iterable (sequence) into a list.
letters = list('Python')
print(letters)
# Ans: ['P', 'y', 't', 'h', 'o', 'n']
numbers = list(range(5))
print(numbers)
# Ans: [0, 1, 2, 3, 4]
# Create Nested List (Matrix)
matrix = [['a', 'b', 'c'], 
          ['d', 'e', 'f']]
print(matrix)
print(type(matrix))
# Ans: [['a', 'b', 'c'], ['d', 'e', 'f']], <class 'list'>
# matrix >> object(list, array) >pointer> objects(list, array) >pointer> objects(str, 'a')
mixed_matrix = [['a', 'b'],
                [1, 2, 3],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))
# Ans: [['a', 'b'], [1, 2, 3], [True]], <class 'list'>

# Access Lists:

# Indexing & Slicing
# Access & Read

# Indexing
# Task: Get the first item from the list
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
# Ans: a
# Task: Get the last item from the list
lst = ['a', 'b', 'c', 'd']
print(lst[3])
print(lst[-1])
# Ans: d, d
# Task: Get the 'c' from the list
print(lst[-2])
# Ans: c
# Nested List (Matrix)
## matrix >> Whole List, matrix[1] >> Complete Row, matrix[1][1] >> One Single Value
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Get the whole Matrix
print(matrix)
# Ans: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# Task: Get the last row of the matrix
print(matrix[2])
print(matrix[-1])
# Ans: ['g', 'h', 'i']
# Task: Get the last item of the last row
print(matrix[-1][-1])
# Ans: i
# Task: Get the first item of the first row
print(matrix[0][0])
# Ans: a
# Task: Get the second item of the second row of the matrix
print(matrix[1][1])
# Ans: e (Answer can vary depending on the structure of the matrix)

# Slicing
# Task: Get the first two items from the list
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0:2])
print(lst[:2])
# Ans: ['a', 'b']
# Task: Get the last three items from the list
print(lst[1:4])
print(lst[1:])
# Ans: ['b', 'c', 'd']
# Task: Get the whole list
print(lst[:])
# Ans: ['a', 'b', 'c', 'd']
# Nested List (Matrix)
## matrix >> Whole List, matrix[1:3] >> Complete Rows, matrix[2][:-1] >> Certain part of a Specific Row
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Get the first two rows (lists) from a list
print(matrix[0:2])
print(matrix[:2])
# Ans: [['a', 'b', 'c'], ['d', 'e', 'f']]
# Task: Get the last two rows (lists) from a list
print(matrix[1:3])
print(matrix[1:])
# Ans: [['d', 'e', 'f'], ['g', 'h', 'i']]
# Task: Slicing inside one specific row
print(matrix[2][:2])
# Ans: ['g', 'h']

# Unpacking Lists:

# Packing a list means creating a list.
# Without Unpacking, using only Indexes makes code long and hard to extend.
person = ['Maria', 29, 'Data Engineer', 'Spain']
name = person[0]
age = person[1]
role = person[2]
country = person[3]
# Unpacking, list of variables, separated by commas
name, age, role, country = person
# Rule: Variable order must match the list values order.
print(role)
# Ans: Data Engineer
# Note: Unpacking is clean, easy and makes code simple to extend.

# Rest Collector, Asterisk (*)
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
name, *details, country = person
print(name)   # Ans: Maria
print(details)   # Ans: [29, 'Data Engineer', 'city']
print(country)   # Ans: Spain

person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
name, *details = person
print(name)   # Ans: Maria
print(details)   # Ans: [29, 'Data Engineer', 'city', 'Spain']

*details, country = person
print(details)   # Ans: ['Maria', 29, 'Data Engineer', 'city']
print(country)   # Ans: Spain
*details, city, country = person
print(details)   # Ans: ['Maria', 29, 'Data Engineer']
print(city)   # Ans: city
print(country)   # Ans: Spain
# Rule: Only one asterisk(*) is allowed in unpacking.

# Unpacking Rules
# 1) Nr. of variables must match the Nr. of values exactly - not less, not more.
# Note: * Asterisk collects leftovers, and it's fine if there are none.
numbers = [1]
first, *rest = numbers
print(first)   # Ans: 1
print(rest)   # Ans: []
# Note: We can unpack any sequence (lists, tuples, strings etc).
numbers = 'Hi'
first, *rest = numbers
print(first)   # Ans: H
print(rest)   # Ans: ['i']

# Skipping Items, Underscore "_"
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, age, role, country = person

name, _, role, _ = person

print(name)   # Ans: Maria
print(role)   # Ans: Data Engineer

# Asterisk (*) & Underscore "_"
name, *_, country = person

print(name)   # Ans: Maria
print(country)   # Ans: Spain

name, *_ = person
print(name)   # Ans: Maria
*_, country = person
print(country)   # Ans: Spain

# Explore & Analyze Lists:

# Functions -
# Analyze - max(), min(), sum(), len()
numbers = [1, 5, 5, 4, 3]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Total:", sum(numbers))
print("Length of list:", len(numbers))
# Completeness & Existence Check - all(did everything pass), any(did something pass)
print("All:", all(numbers))   # Ans: All: True
print("All:", all([1, 0, 2]))   # Ans: All: False
print("All:", all(['a', '', 'b']))   # Ans: All: False
print("All:", all(['a', 'c', 'b']))   # Ans: All: True
print("Any:", any(numbers))   # Ans: Any: True
print("Any:", any([1, 0, 2]))   # Ans: Any: True
print("Any:", any(['a', '', 'b']))   # Ans: Any: True
print("Any:", any([0, 0, 0]))   # Ans: Any: False
# Methods -
# Search & Count - .count(how often), .index(where it appears, returns the position of the first occurrence of a value)
print("Count:", numbers.count(5))   # Ans: Count: 2
print("Index:", numbers.index(5))   # Ans: Index: 1
# Operators -
# Membership & Identity - in (checks if a value exists in a sequence), is ()
numbers = [1, 5, 5, 4, 3]
print(4 in numbers)   # Ans: True
print(8 in numbers)   # Ans: False
print(8 not in numbers)   # Ans: True
list1 = [5, 8, 3]
list2 = [5, 8, 3]
print(list1 is list2)   # Ans: False (because the memory addresses are not equal due to different lists)
# Comparison - ==, >
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
print(list1 == list2)   # Ans: False
print(list3 == list2)   # Ans: True
list1 = [5, 8, 3]
list2 = [5, 2, 3]
print(list1 < list2)   # Ans: False
# Note: The first elements are compared, if they're equal, Python moves to the next element.

# Add, Remove & Update Lists (Change Lists):

# Add Items
# Task: Add 'x' to the end of the list
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
print(letters)   # Ans: ['a', 'b', 'c', 'x']
# Insert at specific position
# Task: Add 'x' at the start of the list
letters = ['a', 'b', 'c']
letters.insert(0, 'x')
letters.insert(3, 'y')
print(letters)   # Ans: ['x', 'a', 'b', 'c']
# Adding
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Add new row to the end of matrix
matrix.append(['x', 'y', 'z'])
matrix.insert(0, ['a', 'a', 'a'])
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']]
# Task: Add 'x' at the end of second row
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
matrix[1].append('x')
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f', 'x'], ['g', 'h', 'i']]
# Task: Add 'z' at the start of the first row
matrix[0].insert(0, 'z')
print(matrix)   # Ans: [['z', 'a', 'b', 'c'], ['d', 'e', 'f', 'x'], ['g', 'h', 'i']]

# Remove Items
# Remove everything from a list
letters = ['a', 'b', 'c']
letters.clear()
print(letters)   # Ans: []
# Task: Remove 'a' from the list
letters = ['a', 'b', 'a']
letters.remove('a')   # Removes only the first match
print(letters)   # Ans: ['b', 'a']
# Task: Remove the last item
letters = ['a', 'b', 'c']
removed = letters.pop()   # default last item
print(letters)   # Ans: ['a', 'b']
print('Removed Item:', removed)   # Ans: Removed Item: c
# Task: Remove the first item
letters = ['a', 'b', 'c']
removed = letters.pop(0)   # position number of the first item
print(letters)   # Ans: ['b', 'c']
print('Removed Item:', removed)   # Ans: Removed Item: a
# Task: Remove the second item
letters = ['a', 'b', 'c']
removed = letters.pop(1)   # position number of the first item
print(letters)   # Ans: ['a', 'c']
print('Removed Item:', removed)   # Ans: Removed Item: b
# Removing
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Remove the first row
matrix.remove(['a', 'b', 'c'])
print(matrix)   # Ans: [['d', 'e', 'f'], ['g', 'h', 'i']]
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Remove the last row
matrix.pop()
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f']]
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Remove 'e' from the matrix
matrix[1].remove('e')
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'f'], ['g', 'h', 'i']]
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Remove the first item from the last row
matrix[-1].pop(0)
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f'], ['h', 'i']]
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Remove the last item of the first list
matrix[0].pop()
print(matrix)   # Ans: [['a', 'b'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# Update Items
# Task: Update the first item to the value 'x'
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)   # Ans: ['x', 'b', 'c']
# Updating
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Update the content of the last list
matrix[-1] = ['x', 'y', 'z']
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f'], ['x', 'y', 'z']]
matrix = [
    ['a', 'b', 'c'],   # Row 0
    ['d', 'e', 'f'],   # Row 1
    ['g', 'h', 'i']    # Row 2
]
# Task: Update the first item of the first list
matrix[0][0] = '-'
print(matrix)   # Ans: [['-', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# Task: Update the second item of the second row
matrix[1][1] = '-'
print(matrix)   # Ans: [['-', 'b', 'c'], ['d', '-', 'f'], ['g', 'h', 'i']]
# Task: Update the last item of the last row
matrix[-1][-1] = '-'
print(matrix)   # Ans: [['-', 'b', 'c'], ['d', '-', 'f'], ['g', 'h', '-']]

