# Python Basics


# Python Built-in Functions

# 1. Print Function
print("Hi Python!")
print('Hello Python!')
print("------------------------")
print("...LEARN PYTHON...")
print("------------------------")


# Special Characters
print("Hi \"Python\"!")
print("Hi 'Python'!")
print('Hi \'Python\'!')

print("Path: C:\\Users\\Name")

print("Message1")
print()
print("Message2")
print("Message1\n")
print("Message2")
print("Message1\n\n\n")
print("Message2")
print("Message1\n\n\nMessage2")

print("Message1\tMessage2")

print("My learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")
print("""My learning Path:
      \t-Python Basics
      \t-Data Engineering
      \t-AI""")

# 2. Input Function
# 3. Len Function



# Python Variables

print("My name is X.")
print("X is learning Python.")
print("X wants to become a Python developer.")

#name = "Y"
#language = "C++"
#print("My name is", name + ".")
#print(name, "is learning", language + ".")
#print(name, "wants to become a", language, "developer.")


# 2. Input Function
 
#name = input("Enter Your Name:")
#country = "Germany"
#print(name, "comes from", country)



# Python Data Types

### Data Types :-
# 1. No Value (none)
# 2. Single Value (Primitive Types - Numeric > int, float, complex, DateTime, str, bool)
# 3. Multiple Values (Data Structures - list, tuple, set, dict, array. Collections, Containers)
# 4. User-defined Data Types (Classes/Objects)
# 5. Special Data Types (Modules, Files, etc.)

a = 19 #int
b = 13.96 #float
c = "Python" #str
d = 'Java' #str
e = "1234" #str
f = "" #str - blank
g = " " #str - Empty space
h = True #bool 
i = False #bool
j = None #NoneType



#### Functions:-

### Sources-

## Standard Library

### Types-
# Standalone Functions [Print(), Type()]
# Methods of classes/objects [Upper(), Replace()]
# Operators [+ / > < == in or]

## 3rd-Party Libraries [Pandas, NumPy, TensorFlow]
## User Defined

#### Standard Library

### Built-in Module
## Functions - Print(), Type(), Len()
## Class str - Upper(), Replace()
## Class int - Bit_length(), To_bytes()

### Math Module
## Functions - Abs(), Round(), Floor()



### Functions and Methods

## Functions - Independent block of code
# Syntax - function_name(value)
# Example - print("Hello"), type(123)

## Methods - Functions belonging to a class/object
# Syntax - value.method_name()
# Example - "hello".upper(), 50.bit_length()


text = "python"
number = 64

print(text)
print(number)

# Nested functions
print(type(text))
print(type(number))
print(len(text))
print(text.upper())
print(number.bit_length())



#### String Functions

### Categories

## Types - type(), str() [Built-in Functions]
## Math - len(), count()
## Tranformations - replace(), 'H'+'i', f{}, split(), 'ha'*2, Extraction: 'cat'[0], 'cat'[1:3] [Operators]
## Cleaning - Clean Whitespaces: lstrip(), rstrip(), strip(), Clean Cases: lower(), upper() [Methods of <str-class>]
## Search - startswith(), endswith(), find(), index(), 'a'in'cat'
## Validation - isalpha(), isnumeric(), isspace()

## Types - type(), str()
name = "Alice"
print(type(name))

age = 25
print(type(age))
print("Your Age is: " + str(age))
age = age + 3
#age = str(age)


## Math - len(), count()
password = "  123@hfklkfdsj"
print(len(password))

if len(password) < 8:
      print("Your password is too short!")

text = """
Python is easy to learn.
Python is powerful.
Many developers use python.
"""
print(text.count("Python"))
#print(text.count("%"))


## Transformations -

# replace()
#price = "1123,45"
#print(price.replace(",", "."))

phone = "123-456-7890"
print(phone.replace("-", "/"))
#print(phone.replace("-", ""))

price = "$1,298.99"
print(price.replace("$", "").replace(",", ""))

# Concatenation
first_name = "John"
last_name = "Doe"
last_name = first_name + " " + last_name
print(last_name)

folder = "C:/Users/John"
file = "report.csv"
full_file_path = folder + "/" + file
print(full_file_path)

# f-strings (Easy way to format and build strings, "f" stands for "formatted", put variables and expressions directly inside string values)
name = "Emma"
age = 30
is_student = False
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".") 

print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")

print(f"{{This will show curly braces}}")

# split()
stamp = "2026-10-06 14:30"
print(stamp.split(" "))
stamp2 = "2026-10-06"
print(stamp2.split("-"))

csv_file = "1123,John,Germany,1984-05-12,M"
print(csv_file.split(","))

# String Repetition (*, multiplier)
print("ha" * 3)
print("=" * 25)

# Extraction (Indexing and Slicing)
text1 = "Python"

print(text1[0])  # Extract first character
print(text1[-6]) # Extract first character using negative index

print(text1[5])  # Extract last character
print(text1[-1]) # Extract last character using negative index

print(text1[3])  # Extract h
print(text1[-3]) # Extract h using negative index

# slicing
date = "2024-06-15"
print(date[0:4])  # Extract the year
print(date[:4])   # Extract the year (omitting start index)

print(date[5:7])  # Extract the month

print(date[8:])   # Extract the day (omitting end index)
print(date[-2:])  # Extract the day using negative index


## Cleaning -

# Clean Whitespaces
text2 = " Engineering".lstrip()
print(text2)

text2 = "Engineering ".rstrip()
print(text2)

text2 = "     Engineering ".strip()
print(text2)

text2 = "Data Engineering".strip()
print(text2)

text2 = "###Abc###".strip("#")
print(text2)

# test
text2 = " Engineering "
print(len(text2))
print(len(text2.strip()))

nr_of_spaces = len(text2) - len(text2.strip())
is_clean = len(text2) == len(text2.strip())
print("Nr of Spaces:", nr_of_spaces)
print("Is my data clean?", is_clean)

# Clean cases (Case Conversations)
text = "PyThOn ProGRamMing"
print(text.lower())
print(text.upper())

# test
search = "Email".lower().strip()
data = " emAil".lower().strip()
print(search == data)

# challange
data = "968-Maria, (D@t@ Engineer );; 27y  "   #>>> name: maria | role: data engineer | age: 27
print(data.strip().split(",")[0].split("-")[1].strip().lower())  # name
print(data.strip().split("(")[1].strip().split(")")[0].replace("@", "a").lower())  # role
print(data[-6:-3].strip())  # age


## Search -

phone1 = "+49-176-12345"
print(phone1.startswith("+49"))

email = "maxmin@outlook.com"
print(email.endswith(".gmail.com"))

file = "data_report_2024.csv"
print(file.endswith(".csv"))

print("@" in email)

url = "https://api.compaby.com/v3/data"
print("/api" in url)

phone1 = "+49-176-12345"
phone2 = "48-654-16548"
phone3 = "+1-202-55501"
print(phone1[4:])
print(phone2[3:])

print(phone1.find("-"))

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])


## Validation -

# isalpha(): checks if all characters in the string are alphabetic
country = "Germany#"
print(country.isalpha())

# isnumeric(): checks if all characters in the string are numeric
phone = "096-9865987"
print(phone.isnumeric())
phone1 = "096986.5987"
print(phone1.isnumeric())

# isspace(): checks if all characters in the string are whitespace



#### Numeric Functions

# int: 5, -12, 34444
# float: 3.15, -0.4, 100.0
# complex: 3+4j, 5-2j

### Categories

## Types - type(), int(), float(), complex() [Built-in Functions]
## Math Operators - +, -, *, /, //, %, ** [Operators]
## Rounding - abs(), round(), ceil(), floor(), trunc()
## Advanced Math - sqrt(), sin(), cos(), log() [Python Modules]
## Random - random(), randint()
## Validation - is_integer(), isinstance()

## Types - 
x = 10
y = 5.75
z = 3 + 4j
print(type(x))
print(type(y))
print(type(z))

x = "24"
print(type(x))
x = int(x)
print(type(x))
print(x * 2)

x = 3.14
print(int(x))

x = 3
print(float(x))

x = "3.14"
print(float(x))

x = 3 # real
y = 4 # imaginary
print(complex(x, y))


## Math Operators -
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 3)   # float division
print(10 // 3)  # floor division
print(9 % 2)   # modulus
print(10 ** 3)  # exponentiation
print(2 ** 5)   # 2 to the power of 5

# shortcuts
x = 10
x = x + 3
x += 3 # shortcut for x = x + 3
print(x)
x -= 2 # shortcut for x = x - 2
print(x)
x *= 4 # shortcut for x = x * 4
print(x)


## Rounding -
# measure distance
print(2-10)
print(abs(2-10))

# rounding numbers
price = 35.54879865
print(round(price))
print(round(price, 2))
print(round(price, 1))

import math
print(math.floor(price))
print(math.ceil(price))

print(math.trunc(price))
print(int(price))


## Advanced Math -


## Random -
import random
print(random.random())  # random float between 0.0 and 1.0
print(random.randint(1, 100))  # random integer between 1 and 100 (both inclusive)


## Validation -
x = 5.00
print(x.is_integer())
y = 5.5
print(y.is_integer())

x= 94
print(isinstance(x, int))
x= 94.0
print(isinstance(x, int))
print(isinstance(x, float))

# challange: generate a random even number between 2 and 50 and check if it is an even number
rand_num = random.randint(1, 25)
print(rand_num % 2)