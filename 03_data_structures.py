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


