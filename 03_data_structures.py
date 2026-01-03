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


