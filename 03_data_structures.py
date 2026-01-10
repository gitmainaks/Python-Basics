# Structured Data Types


## 1. List
## 2. Tuple
## 3. Set
## 4. Dictionary
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

# Order Lists:

# .sort() - Method
# Task: Sort the list in ascending order
letters = ['c', 'a', 'b']
letters.sort()   # default Ascending order
letters.sort(reverse = True)   # Descnding order
print(letters)   # Ans: ['c', 'b', 'a']
# Sorting
matrix = [
    ['d', 'e', 'f'],   # Row 0
    ['g', 'h', 'i'],   # Row 1
    ['a', 'b', 'c']    # Row 2
]
matrix.sort()
print(matrix)   # Ans: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# Note: For multiple lists, Python sorts by the first item of each inner list.
matrix = [
    ['d', 'e', 'f'],   # Row 0
    ['a', 'z', 'i'],   # Row 1
    ['a', 'a', 'c']    # Row 2
]
matrix.sort()
print(matrix)   # Ans: [['a', 'a', 'c'], ['a', 'z', 'i'], ['d', 'e', 'f']]
# Task: Sort the second list
matrix = [
    ['d', 'e', 'f'],   # Row 0
    ['a', 'z', 'i'],   # Row 1
    ['a', 'a', 'c']    # Row 2
]
matrix[1].sort()
print(matrix)   # Ans: [['d', 'e', 'f'], ['a', 'i', 'z'], ['a', 'a', 'c']]
# sorted() - Function
letters = ['c', 'a', 'b']
new_list = sorted(letters)
print('Original List:', letters)   # original list is unchanged
print('Sorted List:', new_list)   # Ans: Sorted List: ['a', 'b', 'c']
new_list = sorted(letters, reverse = True)
print('Sorted List:', new_list)

# Reversing List: Flip the List around
# .reverse() - Method
letters = ['c', 'a', 'b']
letters.reverse()
print(letters)   # Ans: ['b', 'a', 'c']
# reversed() - Function
letters = ['c', 'a', 'b']
new_list = list(reversed(letters))   # Note: reversed() creates an iterator object, not a list.
print('Original List:', letters)
print('Reversed List:', new_list)   # Ans: Reversed List: ['b', 'a', 'c']

# Copy Lists:

# Raw Data & Modified Data (Compare)
# Reference, Copy, Shallow Copy, Deep Copy
# Assignment = 
# Original
# CopyList = Original >> Object(list)(original) >> objects(str, 'a')
# New variable is referencing to the same list (original).
# Task: Create a copy of the list in a new variable
letters = ['a', 'b', 'c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:', letters)    # Original: ['a', 'b', 'z']
print('Copy:', letters_copy)   # Copy: ['a', 'b', 'z']
# Note: Both variables reference the same list in memory.

# Shallow Copy (Method)
# CopyList = Original.Copy() >> Object(list)(original) & Object(list)(copy) >> separete objects(str, 'a') for copy
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
letters.pop()
letters_copy.append('z')
print('Original:', letters)    # Original: ['a', 'b']
print('Copy:', letters_copy)   # Copy: ['a', 'b', 'c', 'z']
# Note: .copy() creates a separate list in memory

# Deep Copy (Function)
# Task: Add a new item in the 1st row of the copied list
matrix = [
    ['a', 'b'],   # Row 0
    ['c', 'd'],   # Row 1
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)         # Original: [['a', 'b', 'z']]
print('Copy:    ',  matrix_copy)   # Copy:     [['a', 'b', 'z'], ['c', 'd']]
# Note: The .copy() method creates a SHALLOW copy
# CopyList = Original.Copy() >> Object(list)(original) & Object(list)(copy) >> Objects(lists)(original) & Objects(lists)(copy) >> separately uasble objects(str, 'a') for copy
#                               -------- Top Level (Independent) ---------                                                        ---------- Deeper Level (Shared) -----------
# Standard Library > Copy Module > Functions - copy(), deepcopy()
# import Copy
# Original
# CopyList = Copy.deepcopy(Original) >> Object(list)(original) & Object(list)(copy) >> Objects(lists)(original) & Objects(lists)(copy) >> Completely Independent copies from the lists - objects(str, 'a') (No pointers, no references)
#                                       -------- Top Level (Independent) ---------                                                        ------------------------------ Deeper Level (Independent) -----------------------------------
import copy
matrix = [
    ['a', 'b'],   # Row 0
    ['c', 'd'],   # Row 1
]
matrix_copy = copy.deepcopy(matrix)
#matrix_copy = copy.copy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)         # Original: [['a', 'b']]
print('Copy:    ',  matrix_copy)   # Copy: [['a', 'b', 'z'], ['c', 'd']]
# Note: copy.deepcopy() creates a true, independent copy for all levels.
# Note: copy.copy() creates a SHALLOW copy just like the method .copy().
# Note: copy.copy() is more general than list.copy(), not limited to lists. (Methods like .copy() belongs to specific class, but the functions are for allpurpose)

# Testing
# IS Operator
# Checks If Two Variables Refer to the Same Object
original = [
    ['a', 'b'],   # Row 0
    ['c', 'd'],   # Row 1
]
# Assignment
copy1 = original
print("Same Object?", original is copy1, "\n")          # Ans: Same Object? True
# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)                # Ans: Same Object? False
print("Shared Lists?", original[0] is copy2[0], "\n")   # Ans: Shared Lists? True
# Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)                # Ans: Same Object? False
print("Shared Lists?", original[0] is copy3[0], "\n")   # Ans: Shared Lists? False
# Tip: Use the IS operator to check if the copies are truly independent.
# How to Copy?
# Avoid Assignment = (Risky & Confusing)
# Use .copy() for simple, flat lists
# Use copy.deepcopy() for Nested lists
# Always make extra Copy for Experiments/Tests

# Combine Lists:

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)          # Ans: ['a', 'b', 'c', 1, 2, 3] flat list
# Multiplier Operator, makes multiple copies of the same list.
print(letters * 2)   # Ans: ['a', 'b', 'c', 'a', 'b', 'c']
# New Nested List (two lists inside one big list)
comb = [letters, numbers]
print(comb)          # Ans: [['a', 'b', 'c'], [1, 2, 3]]

# .extend() Change the list itself by adding the second list inside it
# list1.Extend(list2) (Method), like appending list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)   # Ans: ['a', 'b', 'c']
print(numbers)   # Ans: [1, 2, 3, 'a', 'b', 'c']
# Note: Extends doesn't create a new list; it expands the original one.

# Zip() (Function), pairing the items from two list by positions
# Output of the zip would be a list of Tuples (a Nested thing)
# Python will stop at the shortest list.
# Output of the zip function is an iterator, an object. Convert it to list by using fn list().
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers, "Hi"))
print(comb)   # Ans: [('a', 1, 'H'), ('b', 2, 'i')]
# Task: Pair Customers with their IDs (rebuild the relationship)
ids = [101, 102, 103]
names = ['Kali', 'Sara', 'Don']
print(list(zip(ids, names)))   # Ans: [(101, 'Kali'), (102, 'Sara'), (103, 'Don')]

# Advanced Techniques:

# How to Iterate?

# Iterator vs Iterable
# Enumerate, Map, Filter, Reversed, Chain (Functions)

# Why do we need Iterators?
# 1) For Looping
# 2) Save Memory (Big Data)
# 3) Speed Flexibility (Data Pipeline, Transformation, Kafka)

# Iterator - An object that helps to do the iteration, the process, the engine, the machine.
# Iterable - An object that has a sequence of items, in order to loop over, the data structure itself. (str is iterable, but int or boolean aren't)

letters = ['a', 'b', 'c']   # iterable, because of str values
for l in letters:
    print(l)
# Note: We use iteration to transform data.
for l in letters:
    print(l.upper())

# Task: Store the transformed results in a new list.
letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)   # Ans: ['A']
#                            ['A', 'B']
#                            ['A', 'B', 'C']

# Iterators - enumerate(), reversed(), zip()

# enumerate(Iterable, start=1), default start from 0
# It returns (Position Nr. + Value)
letters = ['a', 'b', 'c']   # < Iterable
print(enumerate(letters))   # Ans: <enumerate object at 0x00000RFA118K098HQ43>   < Iterator
#                                    Iterator Type         Memory Address
print(list(enumerate(letters, start = 1)))   # Ans: [(1, 'a'), (2, 'b'), (3, 'c')]

letters = ['a', 'b', 'c'] 
for index, value in enumerate(letters):
    print(index, value)   # Ans: 0 a
#                                1 b
#                                2 c
# Enumerate Use Case: Find the exact position of the bad data in list.

# reversed()
# Returns an iterator that flips the data order.
letters = ['a', 'b', 'c']
print(list(reversed(letters)))   # Ans: ['c', 'b', 'a']
for l in reversed(letters):
    print(l)   # Ans: c
#                     b
#                     a

# zip()
# Combines two or more sequences into pairs (tuples)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]

print(list(zip(letters, numbers)))   # Ans: [('a', 1), ('b', 2), ('c', 3)]

for l, n in zip(letters, numbers):
    print(l, n)   # Ans: a 1
#                        b 2
#                        c 3

# map(Class.Function and/or Class, Iterable)
# Task: Make every letter uppercase
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))   # Ans: ['A', 'B', 'C']

# Task: Convert list items to integers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))   # Ans: [1, 2, 3]

# Task: Clean up the list by removing all unwanted spaces
names = [' Maria ', 'Don ', ' Bimar']
print(list(map(str.strip, names)))   # Ans: ['Maria', 'Don', 'Bimar']

names = [' Maria ', 'Don ', ' Bimar']
for n in map(str.strip, names):
    print(n)   # Ans: Maria
#                     Don
#                     Bimar
# Note: Map is fast, clean way to do data transformations.

# filter(Function, Iterable)
# Task: Clean up the list by removing unvalid data
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))    # Ans: ['a', 'b', 'c']
# None, removes all falsy values like 0, '', or False
print(list(filter(bool, letters)))    # Ans: ['a', 'b', 'c']
# bool, works the same! it filters out all falsy values

# Task: Keep only letters (alphabetic) items
items = ['sql', '123', 'python', '43']
print(list(filter(str.isalpha, items)))   # Ans: ['sql', 'python']
# str.isalpha (class.method)

items = ['sql', '123', 'python', '43']
for i in filter(str.isalpha, items):
    print(i)   # Ans: sql
#                     python
# Note: filter() is perfect for cleaning up data in our structures.

# Python Lambda Functions: Quick & Custom Logic

# Normal Function
# def tax(price):
#   return price*1.2

# No name, Anonymous Function
# tax = lambda price: price*1.2

# Lambda is used with other data structure functions like map(), filter(), sorted() to do extra complicated logic on top of the data structure like the list.
# Output = lambda X(input variable): Expression(functions, methods, loop, check)

multiple = lambda x: x * 2
print(multiple(3))   # Ans: 6
# Variable(multiple), stores a lambda function which doubles a number.

add = lambda x, y: x + y
print(add(2, 3))   # Ans: 5
# Note: When a lambda has two parameters, you must pass two values when calling it.

check = lambda i: i in "Python"
print(check('n'))   # Ans: True
# Note: A lambda can contain any expression, including conditions.

# Lambda + Map
# map(lambda_:_, Iterable)
# Task: Prices are stored as messy strings and need cleaning to floats.
prices = ['$13.70', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))
#-------------(2.LambdaFn)------(1.DataTransformation)-------
#--------(3.Map the Fn to iterate, to manipulate data)-------
# Ans: [13.7, 9.99, 100.0]
# Initial test
#p = '$13.70'
#print(float(p.replace('$', '')))   # Ans: 13.7

# Lambda + Filter
# filter(lambda_:_, Iterable)
# Task: Remove all prices lower than 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))
#-------------------(2)-------(1)--------------
#------------------------(3)-------------------
# (1) Filter Logic
# (2) in Lambda
# (3) Filter to apply the function to filter all data in list
# Ans: [120, 300]

# Task: Keep only students with scores higher than 70
students = [['Maria', 85],
            ['Bumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[1] > 70, students)))
# Ans: [['Maria', 85], ['Bumar', 90]]
# Initial test
#print(students[2][1] > 70)   # Ans: False
# Matrix iteration happens one row at a time.

# Task: Keep only students with names starting with 'M'
print(list(filter(lambda row: row[0].startswith('M'), students)))
# Ans: [['Maria', 85], ['Max', 60]]
# Initial test
#print(students[2][0].startswith('M'))   # Ans: True

# Lambda + Sorted
# sorted(Iterable, Key=lambda_:_,)

# List Comprehensions:

# Input > [Transformation & Filter] > Output
# 3 Blocks
# [1.Data Transformation(p*2)] [2.Loop(p for prices)] [3.Filter(if p>50)] 
#---------(3)-------------------------(1)---------------------(2)--------
# Filtering the Data is Optional.

# Task: Normalize the domains into standard format
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.PYTHON.COM']

cleaned = [
    # Data Transformation
    d.lower().replace('www.', '')
    # For Loop
    for d in domains
    # Data Filtering
    if '.' in d
]

print(cleaned)   # Ans: ['google.com', 'openai.com', 'python.com']

cleaned = [ d.lower().replace('www.', '') for d in domains if '.' in d]

cleaned = [
    d.lower().replace('www.', '')
    for d in domains
]
print(cleaned)   # Ans: ['google.com', 'openai.com', 'localhost', 'python.com']
# Note: In Comprehensions, Filtering Data is Optional

cleaned = [
    d
    for d in domains
    if '.' in d
]
print(cleaned)   # Ans: ['www.google.com', 'openai.com', 'WWW.PYTHON.COM']
cleaned = [d for d in domains if '.' in d]
# Note: Only Filtering: Using only the varible name means no transformation.

# Python List Operations:

# 1. [0] (Indexing)
# 2. [1:3] (Slicing)
# 3. a, b, c = 1, 2, 3 (Unpacking)
# 4. max()
# 5. min()
# 6. len()
# 7. all() ('')
# 8. any() 
# 9. .count()
# 10. .index() (position)
# 11. in
# 12. .append()
# 13. .insert(1,)
# 14. .clear()
# 15. .remove()
# 16. .pop()
# 17. .sort()
# 18. .reverse()
# 19. a = b (Assigning)
# 20. b = a.copy (Shallow Copy)
# 21. copy.deepcopy() (Deep Copy)
# 22. + (Combining, Flat List)
# 23. , (Combining, Nested List)
# 24. .extend()
# 25. zip()
# 26. enumerate()
# 27. map(fn,)
# 28. filter(fn,)
# 29. fn(filter) > fn(transformation) (Comprehension)


## DATA STRUCTURES - 
# list[1,2] < Everything allowed
# tuple(1,2) < Frozen
# set{1,2} < Unique
# dict{'a':1, 'b':2} < Mapping

# 4 Characteristics of Data Structures - 
# 1) Ordered
# 2) Duplicates
# 3) Indexed
# 4) Mutable

# List
list = [10, 30, 20, 10]

print(list)   # Ordered, Allow Duplicates 
print(list[1])   # Indexed
list[3] = 40
print(list)   # Mutable


## 2. Tuple
# Ordered collection that can't be changed after creating it.

# Tuple
tuple = (10, 30, 20, 10)

print(tuple)   # Ordered, Allow Duplicates 
print(tuple[1])   # Indexed
#tuple[3] = 40    # Immutable

print(sorted(tuple))   # Ans: [10, 10, 20, 30]
# Output of this function will always be a List. We can pass for it as Tuple.

# Use Case: For storing the database informations, database server, port, username etc.
# Protecting the values.


## 3. Set
# Unordered collection of Unique Values.

# Set
set = {10, 30, 20, 10}

print(set)   # Ans: {10, 20, 30}; Unordered, Don't Allow Duplicates (Unique)
#print(set[1])   # Not Indexed
set.remove(20)
print(set)   # {10, 30}; Mutable

# Set = {a,b,c} [Hash Function Fn(x) > Hash Table] (Random)
# used for speed and performance
# A trade-off between losing the order and having fast performance.

# Set Methods
a = {10, 20, 30, 40}
# Note: Index-based methods do not work with Sets.
a.add(50)
print(a)   # {40, 10, 50, 20, 30}
# Add(), inserts the item somewhere in the set, but only if it is new.
#a.update("Hi")
#print(a)   # {'H', 40, 10, 50, 20, 'i', 30}
#a.update([1,2])
#print(a)   # 
#a.update({1,2})
#print(a)   # 
# Update(), Merges another group of values (Iterable) into the set.
# Note: We can use mathe operators as quick shortcuts: | & - ^
a |= {1,2}
print(a)   # {1, 2, 40, 10, 50, 20, 30}
# |= works like update for sets
#a.remove(10)
#print(a)   # {1, 2, 40, 50, 20, 30}
# Remove(), Throws an error if the value is missing.
a.discard(100)
print(a)   # {1, 2, 40, 10, 50, 20, 30}
# Discard(), Removes the item if it exists and does nothing if it does not.
#a.pop()
#print(a)   # {2, 40, 10, 50, 20, 30}
# Pop(), Removes and returns a random item from a set.

# Set Math Methods
# Built-in methods
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
# Mathematical Operations:

# .Union(), combines All unique items from both sets.
print(a.union(b))   # {40, 10, 50, 20, 60, 30}
print(a | b)
print(a)   # {40, 10, 20, 30}
# Note: Math operators return a new set and leave the originals untouched.

# .Intersection(), returns only the shared items.
print(a.intersection(b))   # {40, 30}
print(a & b)

# .Difference(), returns items only in A, Not in B
print(a.difference(b))   # {10, 20}
print(a - b)
print(b - a)   # {50, 60}
print(b.difference(a))
# Return Items in B, but Not in A

# .Symmetric_Difference(), finds only None-Shared items.
print(a.symmetric_difference(b))   # {10, 50, 20, 60}
print(a ^ b)   # '^' (shift+6)

# Set Relationship Methods
# Built-in
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# .Issubset(), returns True if All items in this set exist in the other.
print(a.issubset(b))   # False

a = { 30, 40}
b = {30, 40, 50, 60}

print(a.issubset(b))   # True

# .Issuperset(), returns True when it includes All items of the other set.
print(b.issuperset(a))   # True
# Use Case: All Customers must be maintained in Master Table.

# .Isdisjoint(), returns True if both sets share no items (No Overlapping).
print(a.isdisjoint(b))   # False

a = { 10, 20}
b = {30, 40, 50, 60}

print(a.isdisjoint(b))   # True
# Use Case: For Big dataset Spliting, to confirm no same record.


## 4. Dictionary
# It stores different type of informations in key value pairs.

# {Keys(Description of Data) : Values(Actual Data)}
# Customers = {Name : Alex, Age : 33, Country : USA}   (Pairs)

# Dict
dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40
}

print(dict)   # {'a': 40, 'b': 20, 'c': 20}; Ordered
# Keys are Unique
# Values Allow Duplicates
#print(dict[1])   # Not Indexed
print(dict['b'])   # 20
# Note: In Dict, we access values by using their keys, not indexes (Dict is Keyed).
dict['c'] = 80
print(dict)   # {'a': 40, 'b': 20, 'c': 80}; Mutable

# Dict Methods
# Special Methods

user = {"id":1, "age":30, "city": "berlin"}

# Access
print(user["city"])   # berlin
#print(user["name"])   # KeyError
# If the key is not found, Python throws a KeyError
print(user.get("name", "Unknown"))   # Unknown, default None
# .Get(), returns the value safely, gives None if missing.
# Missing key returns None or the default value.
print(user.get("age"))   # 30

# Checks
print("age" in user)   # True
# In Operator, tests if the key is inside the dictionary.
print("name" in user)   # False

# View Objects
print(user.keys())   # dict_keys(['id', 'age', 'city'])
# .Keys(), returns all the KEYS in our dictionary.
print(user.values())   # dict_values([1, 30, 'berlin'])
# .Values(), returns all the VALUES in our dictionary.
print(user.items())   # dict_items([('id', 1), ('age', 30), ('city', 'berlin')])
# .Items(), returns all (key, value) pairs of our dictionary.
# Items() is perfect when we need key and value together for looping, transforming data, building new dicts, comparing and more.
print(user)   # {'id': 1, 'age': 30, 'city': 'berlin'}

# Looping
for u in user:
    print(u)   # id
               # age
               # city
for u in user:
    print(u, user[u])   # id 1
                        # age 30
                        # city berlin

# Clean way of Looping
for key, value in user.items():
    print(key, value)   # id 1
                        # age 30
                        # city berlin

# Add, Remove, Update

# Assign Key, updates the value if the key exists, or inserts a new key value pair if it doesn't.
user["name"] = "John"
print(user)   #(Add) {'id': 1, 'age': 30, 'city': 'berlin', 'name': 'John'}
user["age"] = 35
print(user)   #(Update) {'id': 1, 'age': 35, 'city': 'berlin', 'name': 'John'}
# .Update(), adds new keys and updates existing ones using another dictionary.
user.update({"age": 40, "city": "Paris"})
print(user)   # {'id': 1, 'age': 40, 'city': 'Paris', 'name': 'John'}

# Removing
# .Pop(), removes a key from the dictionary and returns its value.
#age = user.pop("age")
#print(user)   # {'id': 1, 'city': 'Paris', 'name': 'John'}
#print("Removed Item:", age)   # Removed Item: 40
#age = user.pop("salary")   # KeyError
age = user.pop("salary", "Not Found")
print(user)   # {'id': 1, 'city': 'Paris', 'name': 'John'}
print("Removed Item:", age)   # Removed Item: Not Found
# Pop(), removes the key and returns its value or returns our default if the key is missing.

#user.pop()   # TypeError: pop expected at least 1 argument, got 0
# .Popitem(), returns and deletes the most recent key value pair from the dictionary.
user.popitem()
print(user)   # {'id': 1, 'age': 40, 'city': 'Paris'}

# Creating Dict
user = {"id": None,
        "name": None,
        "age": None,
        "city": None}
# .Fromkeys(), builds a new dictionary where all keys get the same default value.
user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)   # {'id': None, 'name': None, 'age': None, 'city': None}
user["age"] = 40
print(user)   # {'id': None, 'name': None, 'age': 40, 'city': None}

# Dict Challenge
# Challenge: Keep only String values & Convert them to UPPERCASE, in a New Dict
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

user_str = {
    k: v.upper() #Expression(3.Transformation if applicable)
    for k, v in user.items() #Loop(1)
    if isinstance(v, str) #Filter(2)
}

print(user_str)   # {'name': 'JOHN', 'city': 'BERLIN'}

user_str = {
    k.upper(): v.lower() #Expression(3.Transformation if applicable)
    for k, v in user.items() #Loop(1)
    if isinstance(v, str) #Filter(2)
}
print(user_str)   # {'NAME': 'john', 'CITY': 'berlin'}

# Dict Applications

# Representing a Single Row from a Database or API
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}
# Use Case.1: Database or API Records
# Returned records are stored as dictionaries where column names are keys and the row values are the dictionary values.

# Mapping Translations to Friendly Values
status_map = {
    "01": "Open",
    "02": "In Progress",
    "03": "Done"
}
# Use Case.2: Mapping to Friendly Values
# Great for converting technical codes into friendly labels.

country_map = {
    "DE": "Germany",
    "FR": "France",
    "US": "United States"
}
# Use Case.3: Mapping Abbreviations
# Turning short abbreviations into full readable names.

# Storing Environment Variables & Configuration
system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytics_warehouse"
}
# Use Case.4: Config and Environment Data
# Store system settings like host, port, and usernames in one clean place.





