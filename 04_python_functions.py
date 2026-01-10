### Python Functions


## Functions: A small, reusable block of code that does one specific job.

# Why We Need Functions? 
# 1) Easy to change
# 2) Fast changes
# 3) Safer (low Risk)
# 4) Smaller & Clean
# 5) Easy to Read & Understand
# 6) Modular
# 7) Collaboration
# 8) Code Modularity; For Big & Complex Problem, Divide It into Smaller Pieces "FUNCTIONS"

## Sources Of Functions - 

# Predefined

# (1) Built-in Functions; print(), len(), str(), input(), type(), bool()
# Come with Python
# 1) Use Them

# (2) Standard Library; math, datetime, random
# Written by Python Team
# 1) Import
# 2) Use

# (3) External Library; Pandas, Matplotlib, Numpy
# Written by Community
# 1) Install
# 2) Import
# 3) Use

## (4) User-Defined Functions;

# Written by Mich
# 1) Define
# 2) Use

# Golden Rule: Before writting new Code, always Check if it already exists!
#1 Built-in Functions >> #2 Libraries >> #3 Team (User-Defined Fn) >> #4 then Write (User-Defined Fn)

## User-Defined Functions

# How Function Work?
# 1) Function Definition
# def function_name():
#       <----->
#       <----->          (Description, "Declaration")
#       <----->
# 2) Function Call
# function_name()        (Execution)

print("Start")
def greet():
    print("Hello")   # Saving the Fn inside the Memory (Creating an Object)
greet()              # Execution
print("End")

# Simple Example

def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")   # Change in the process
    print("Enjoy it")
print("Wake up")
make_coffee()
print("Working for a while")
make_coffee()
make_coffee()

#print("Start Machine")   # Repeat the Process
#print("Make Coffee")
#print("Enjoy it")

# Note: Functions organize and structure our code.

# Built-in Function (Just Calling)
print(len("Python"))   # 6

# Function From Libraries (Import then Call)
import math
number = 7.3
print(math.ceil(number))   # 8

# User Defined Function (Define then Call)
def greet():
    print("Hello")
greet()   # Hello

