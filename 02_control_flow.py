# Control Flow


## 1. Boolean Expressions
## 2. Conditional Statements
## 3. Loops


### Control Flow Statements

## Conditional Statements
# IF
# ELSE
# ELIF
## Loops
# Types
# FOR
# WHILE
# Control
# BREAK
# PASS
# CONTINUE

## Boolean Expressions
# Values
# TRUE
# FALSE
# NONE
# Functions
# BOOL()
# ANY()
# ALL()
# ISINSTANCE()
# Comparison Operators
# EQUALS (==)
# NOT EQUALS (!=)
# GREATER THAN (>)
# LESS THAN (<)
# GREATER THAN OR EQUAL TO (>=)
# LESS THAN OR EQUAL TO (<=)
# Logical Operators
# AND
# OR
# NOT
# Membership Operators
# IN
# NOT IN
# Identity Operators
# IS
# IS NOT


## 1. Boolean Expressions

# Boolean Values & Functions
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hello"))
print(bool())
print(bool([]))
print(bool(0))
print(bool(""))
print(bool(None))

email = ""
phone = "123-456-7890"
username = "user123"
# Allows registration
# if any field is filled
print(any([email, phone, username]))  # True
# Allows registration
# only if all fields are filled
print(all([email, phone, username]))  # False

print(isinstance(123, int))        # True
print(isinstance(True, str))      # False

print("Python".endswith("n")) # True
print("Python".startswith("n")) # False

# Comparison Operators
print(10 == 10)    # True
print(10 != 10)    # False
print(5 > 3)       # True
print(7 >= 7)      # True
print(2 < 5)       # True
print(3 <= 1)      # False
print("apple" == "banana")  # False
print(len("apple") != len("banana"))  # True

print("a" < "b") # True
print("a" == "b") # False
print("a" == "A") # False

print(1 < 5 < 6) # True
print(8 < 5 < 6) # False

# Is age between 18 and 30?
age = 20
print(18 <= age <= 30) # True

# Logical Operators(and|or): Used to combine multiple boolean expressions
print((5 > 3) and (10 > 7))  # True
print((5 > 3) and (10 < 7))  # False

print((5 > 3) or (10 > 7))   # True
print((5 > 3) or (10 < 7))   # True
print((5 < 3) or (10 < 7))   # False

# Checks if the system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90) # True

# Checking user credentials before login
email = True
password = False
print(email and password) # False

print(not 3 > 2) # False
print(not True)  # False
print(not False) # True
print(not not False) # False

name = ""
print(not name) # True
print(not 0)   # True

# Execution Order [Parentheses () First, Control Mixed Conditions]
# AND has higher precedence than OR

# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned
is_logged_in = True
is_guest = False
is_banned = False
print(is_logged_in or is_guest and not is_banned)  # True

is_logged_in = True
is_guest = False
is_banned = True
print(is_logged_in or is_guest and not is_banned) # True

is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned) # False


