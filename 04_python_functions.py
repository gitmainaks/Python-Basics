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



## Python Parameters vs Arguments
# Parameters: Variables listed inside the parentheses in the function definition.
# Arguments: Values passed to the function when it is called.

## Function Shapes:
# 1) No Input/Output
# 2) Only Input
# 3) Input & Output (Input is called Parameters and the Arguments and Output is called Returned Value)
# 4) Multi-Input & Multi-Output

# Parameters:
# Names used in function definition that describe what data the function expects.

# Arguments:
# Actual values passed in a function call that are assigned to parameters.

# Example:
## User-Defined Functions have Two parts:
# 1) Function Definition with Parameters (Description, Declaration)
# 2) Function Call with Arguments (Execution)

def clean_name():
    name = " MariA  "
    print(name.strip().lower())

clean_name()   # maria
# Rule: Normalize Strings
# Remove extra spaces and make text lowercase
# Hardcoded Value Issue:
# It is not reusable because it always cleans the same value
# Pass Data In:
# Pass the value as a parameter to handle any input
def clean_name(name):
    print(name.strip().lower())

clean_name(" MariA  ")   # maria
clean_name("BOOMER ")   # boomer
clean_name("")
# Works With Any Value
# Values change, but the logic stays the same.


## Python Parameters vs Global vs Local Variables

# Global Variable:
# Created outside the function and can be accessed Anywhere

# Local Variable:
# Created inside the function and can be accessed Only Inside the Function

#f = 2                      # f is Global Variable
#def multiple_factor (x):   # x is Parameter
#    y = x * f              # y is Local Variable
#    print(y)
#multiple_factor(5)

# Global Variable (f) has the Longest Life (Whole Programme).
# Local Variable (y) is temporary, destroyed after function execution.
# Parameter (x) is also temporary, live as long as the function is running.

# Example:
# Control Logic Globally
# A global variable controls behavior without changing the function
case_rule = "lower"          # 'case_rule' is Global Variable

def clean_name(name):        # 'name' is Parameter
    cleaned = name.strip()   # 'cleaned' is Local Variable
    if case_rule == "lower":     # Accessing Global Variable
        cleaned = cleaned.lower()
    print("Raw:", name)          # Raw:  MariA  
    print("Cleaned:", cleaned)   # Cleaned: maria

clean_name(" MariA  ")
# Raw vs Processed Data
# Parameter keeps the raw value to be reused
# Local variable holds the processed version
# Scope: Parameters and local variables can be accessed only inside the function.
# Global Access: A global variable is available across the entire script.
print("The Rule is :", case_rule)   # The Rule is : lower


## Python Positional vs Keyword Arguments | Default Parameters

# Task1. Send First and Last Names to be cleaned
# Task2. Merge them into Full Name

# Building Full Clean Name
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)   # michael smith From DE

# Positional Arguments
clean_name(" MiChAel  ", "SMITH ", "DE")

# Keyword Arguments
clean_name(country = "DE", last_name = "SMITH ", first_name = " MiChAel  ")

# Rule: Nr. of Arguments must match the Nr. of Parameters.

# Positional Arguments:
# Values pass to the function based on their Order.
# Rule: The order of Arguments must match the order of Parameters.

# Keyword Arguments:
# Values pass to the function based on their Names.
# Readability: Keyword Arguments are easier to read and understand than Positional.
# Safety: Keyword arguments are safer since they reduce mistakes with clear names.
# Overhead: Keyword arguments take more time to write and maintain.

# How to choose between Positional and Keyword?
# Depends on the number of parameters.
# If 2-3 parameters, Positional is fine.
# If more than 3, Keyword is better for clarity.

## Mixed Arguments
clean_name(" MiChAel  ", last_name = "SMITH ", country = "DE")
# Rule: We must Start with Positional Args then Keyword.


## Default Parameter:
# Parameter that has already a value, so if we dont pass anything in, Python uses that value automatically.

# Building Full Clean Name
def clean_name(first_name, last_name, country="n/a"):   # Default Parameter value for 'country' is 'n/a'
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)   # michael smith From DE

# Positional Arguments
clean_name(" MiChAel  ", "SMITH ", "DE")

# Keyword Arguments
clean_name(country = "DE", last_name = "SMITH ", first_name = " MiChAel  ")

# Mixed Arguments
clean_name(" MiChAel  ", "SMITH ", country = "DE")

# Default Parameter Usage
clean_name(" MAx  ", "STERN ")   # max stern From n/a
# Rule: Parameter without a Default follows Parameter with a Default.


## *Args and **Kwargs
# Some times we dont know how many arguments we will pass to the function, so we use *args and **kwargs to handle that.

# *Args(Positional Arguments) & **Kwargs(Keyword Arguments): allow functions to accept a unknown number of arguments.

# Calculate the total of values
def total(a=0, b=0, c=0, d=0):
    print(a + b + c + d)
total(1, 2)   # 3
total(1, 2, 3)   # 6
total(1, 2, 3, 4)   # 10

def total(*args):
    print(type(args))   # <class 'tuple'>
    print(sum(args))
total(1, 2)   # 3
total(1, 2, 3)   # 6
total(1, 2, 3, 4)   # 10
total(1, 2, 3, 4, 5, 6)   # 21
# Args: A tuple of all the positional arguments passed to the function.
# When we pass similar types of values.

# Create the user profile
def create_user(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    print(kwargs)
create_user(firstname="Mo",
            last_name="Salah",
            age=33,
            country="Egypt")   # {'firstname': 'Mo', 'last_name': 'Salah', 'age': 33, 'country': 'Egypt'}
create_user(name="Ronaldo",
            country="Portugal")   # {'name': 'Ronaldo', 'country': 'Portugal'}
# Kwargs: A dictionary of all the keyword arguments passed to the function.
# When we pass different types of values.
# Works only with Keyword Arguments.




