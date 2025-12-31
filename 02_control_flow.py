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

# Python Challenges
# 1. Check if a user's name is not empty and the age is greater than or equal to 18.
username = ""
age = 20
print(username != "" and age >= 18) # False

# 2. Check if the password is at least 8 characters long and does not contain spaces.
password = "my password"
print(len(password) >= 8 and " " not in password) # False

# 3. Check if a user's email is not empty, contains '@', and ends with '.com'.
email = "user@example.com"
print(email != "" and "@" in email and email.endswith(".com")) # True

# 4. Check if a username is a string, is not None, and is longer than 5 characters.
username = "user123"
print(isinstance(username, str) and username is not None and len(username) > 5) # True

# 5. Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.
is_admin = False
is_moderator = True
is_banned = False
is_email_verified = True
print((is_admin or is_moderator) and (not is_banned or is_email_verified)) # True

# Membership Operators (IN/NOT IN): Checks if a value inside another value, like a string, list, tuple, or dictionary or other sequence)
print("o" in "Python")  # True
print("f" not in "Python")  # True

print(3 in [1, 2, 3, 4, 5])  # True
print(3 not in [1, 2, 3, 4, 5])  # False

# Security check: ensure the domain is not blacklisted
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print (domain not in banned_domains)  # True

# Identity Operators (IS/IS NOT): Checks if two variables refer to the same object in memory
# Variables >>>Pointers>>> ID > Values
# a == b (comparing the values of the two variables)
# a is b (comparing the Ids of the objects, whether the two variables are pointing to the same object in the memory)
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)   #True
print(x is y)   #False

x = 10
y = 10

print(x == y)   #True
print(x is y)   #True

x = ['a', 'b', 'c']
y = x

print(x == y)   #True
print(x is y)   #True

# Make sure the email exists, and it's not empty
email1 = ""
email2 = "b@gmail.com"
email3 = None

print(email1 != "")   #False
print(email2 != "")   #True
print(email3 != "")   #True
print(email3 != None and email3 != "")   #False
print(email3 is not None and email3 != "") # Use IS instead of == when checking for None   #False


## 2. Conditional Statements

# Standalone
# IF Statement
# Defines the first condition (If this is true, do this, otherwise, do nothing)
# IF Condition1: do A
# IF Rules
# 1) Only one If
# 2) Starts with If
# 3) Required
# 4) Can standalone
## Itendation is part of the syntax in Python
score1 = 100
if score1 >= 90:
    print("A")
score2 = 50
if score2 >= 90:
    print("A")

# Two-Way Decision (Only one path runs!)
# IF ELSE
# ELSE Statement
# Runs only if all previous conditions are false (If nothing was true, do this instead)
# IF Condition1:
#    do A
# ELSE:
#    do B
# ELSE Rules
# 1) Comes at the end
# 2) No conditions
# 3) Optional
# 4) Cannot standalone
# 5) Only one else
score2 = 50
if score2 >= 90:
    print("A")
else:
    print("F")

# Multiple Conditions
# IF-ELIF-ELSE
# ELIF Statement
# Asks a follow-up question, only runs if previous conditions were false (If the first wasn't true, try this one)
# IF Condition1:
#    do A
# ELIF Condition2:
#    do C
# ELSE:
#    do B
# ELIF Rules
# 1) Comes after IF
# 2) Multiple ELIF
# 3) Needs condition
# 4) Optional
# 5) Cannot standalone
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# Branching
# IF-ELIF-ELIF-ELSE
score = 76
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
# Ans: C

# Nesting (Nested Ifs)
# IF-ELSE
score = 95
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# Ans: A+

# Connecting Conditions (Logical Operators)
score = 95
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# Ans: A

score = 50
submitted_project = True
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")
# Ans: D

# Independent (Independent Ifs)
# IF-ELSE
# Each IF is checked separately (All conditions are tested, even if one is already true)
score = 50
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")
# Ans: Low Score, Project is not submitted

# Python Challenge
# 1. Validate the Quality and Correctness of Email Values
# - Must not be empty
# - Must contain '.' and '@'
# - Must contain exactly one '@' symbol
# - Must end with '.com', '.org', or '.net'
# - Must not be longer than 254 characters
# - Must start and end with a letter or digit
email = "  "
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
else:
    print("Email is valid.")
# Ans: Email cannot be empty

email = "xyz@promailcom"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print("Email must contain . and @.")
else:
    print("Email is valid.")
# Ans: Email must contain . and @.

email = "xyz@pro@mail.com"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print("Email must contain . and @.")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one '@'.")
else:
    print("Email is valid.")
# Ans: Email must contain exactly one '@'.

email = "xyz@promail.io"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print("Email must contain . and @.")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):   # Use of SET
    print("Email must end with '.com', '.org', or '.net'.")
else:
    print("Email is valid.")
# Ans: Email must end with '.com', '.org', or '.net'.

email = "xyz@promail.net"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print("Email must contain . and @.")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):   # Use of SET
    print("Email must end with '.com', '.org', or '.net'.")
# Email must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters.")
else:
    print("Email is valid.")
# Ans: Email is valid.

# Case 1: Only one IF and ELIFs
email = "+xyz@promail.net"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print("Email must contain . and @.")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):   # Use of SET
    print("Email must end with '.com', '.org', or '.net'.")
# Email must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters.")
# Email must start and end with a letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()):   # Use of Index[], ISALNUM() - Checks if the string contains only letters and digits(a function)
    print("Email must start and end with a letter or digit.")
else:
    print("Email is valid.")
# Ans: Email must start and end with a letter or digit.

# Case 2: Independent IFs
email = "+xyz@promail.net#"
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
# Email must contain a '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain . and @.")
# Email must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):   # Use of SET
    print("Email must end with '.com', '.org', or '.net'.")
# Email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters.")
# Email must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):   # Use of Index[], ISALNUM() - Checks if the string contains only letters and digits(a function)
    print("Email must start and end with a letter or digit.")
else:
    print("Email is valid.")
# Ans: Email must end with '.com', '.org', or '.net'. and Email must start and end with a letter or digit.

# Case 3:
email = "xyz@promail.net"
valid = True
email = email.strip()   # Clean the String
# Email must not be empty
if email == "":
    print("Email connot be empty.")
    valid = False
# Email must contain a '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain . and @.")
    valid = False
# Email must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one '@'.")
    valid = False
# Email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):   # Use of SET
    print("Email must end with '.com', '.org', or '.net'.")
    valid = False
# Email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters.")
    valid = False
# Email must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):   # Use of Index[], ISALNUM() - Checks if the string contains only letters and digits(a function)
    print("Email must start and end with a letter or digit.")
    valid = False
if valid:
    print("Email is valid.")
# Ans: Email is valid.

# Inline IF Statement (Ternary)
# (do A IF condition1 else do B) Quick & Short
# Rules
# 1) Must have ELSE
# 2) No ELIF
# 3) Can be stored in a variable
# 4) If the logic is very simple!
# Classical IF-ELSE
score = 100
if score >= 90:
    print("A")
else:
    print("F")
# Inline IFs
print("A" if score >= 90 else "F")

grade = "A" if score >= 90 else "F"
print(grade)

# Classical IF-ELSE (For complex logic)
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
# Inline IFs (For simple logic)
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

# Special Statements:
# MATCH CASE
# Evaluate a value against multiple values, runs the code of the first match.
# Task
# IF-ELIF-ELSE (For flexible logic and multiple conditions)
country = "USA"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown Country")
# Ans: Unknown Country

# MATCH CASE (Easy to Read & Write)
match country:
    case "United States" | "USA":   # Matching multiple values in a single case
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unkown Country")
# Ans: US
# Can be used only for matching values


## 3. Loops

# Controling the flow of code
# Repeat a block of code over and over until a condition is met

# (1) For Loops
# Basics: Go through a group of items one by one to do something for each item.
# Python Iterator: an object that go through items one by one in a sequence (Remembers what's done. Knows what's next).
# Sequences (Tuple, List, String, Range, Dictionary, File)
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

for i in (1,2,3,4,5):
    print(f"Round: {i}")   # String function 'f' and Loop variable {i}

# Use the same word: Variable > singular, Sequence > plural
items = (1,2,3,4,5)   # Tuple ()
for item in items:
    print(f"Round: {item}")

items = [1,2,3,4,"Py"]   # List []
for item in items:
    print(f"Round: {item}")

items = " Python"   # String " "
for item in items:
    print(f"Round: {item}")
# Ans: Rounds &   P y t h o n

# Range Function: to generate a sequence of numbers
# RANGE(Start[optional,default=0,in], Stop[out], Step[optional,default=1]) 
for item in range(1, 10, 2):
    print(f"Round: {item}")
# Ans: 1 3 5 7 9 (Only odd numbers, from 1 to 10 with 2 steps)
# Any object in Python that is iteratable, could be use in For Loop.

# For Loops Applications -
# Loading Data/Tables(csv files) from Source to Target
#for filename in [file]:
#    df = pd.read_csv(src)
#    df.to_csv(tgt, index=False)
# Data Preparation
# Data Cleaning (Iteration through columns)
#for col in df.columns:
#    df[col] = df[col].str.strip()

# We use For Loops to go through values and aggregate data like summing, counting or averaging.
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total = total + score
    print("Current Total:", total)
print("Final Total:", total)

scores = [80, 50, 60, 75]   # Sequence (scores), only for iteration
total = 0
for score in scores:   # Loop Variable (score)
    total += score   # Use the Loop Variable, not the Sequence
    print("Current Total:", total)
print("Final Total:", total)
# Ans: Final Total: 265

# We use For Loops to transform data like cleaning data before processing.
# Inconsistent casing & unnecessary spaces
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')   # Clean first, Transform second
    print(f"Processing {file}")

# Python challenges
# 1) Print the 7-times table from 1 to 10 using a for loop.
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 2) Print a left-aligned pyramid of stars with 6 rows using a for loop.
for i in range(1, 7):
    print('*' * i)
# Right-aligned pyramid
for i in range(1, 7):
    spaces = ' ' * (6-i)
    stars = '*' * i
    print(f"{spaces}{stars}")

# Advanced For Loops
# Loop Control
# BREAK, CONTINUE, PASS

# BREAK Statement (When to stop?)
# It stops the loop immediately (jumps out and ends the loop right away)
names = ['john', 'maria', '', 'max']
for name in names:   # first condition (FOR)
    if name == '':   # second condition (IF under FOR)
        print('Empty value detected!')
        break
    print(f'Name = {name}')

# CONTINUE Statement (When to skip?)
# It skips one loop cycle without stopping the loop (skip this one and go next)
names = ['john', 'maria', '', 'max']
for name in names:   # first condition (FOR)
    if name == '':   # second condition (IF under FOR)
        print('Empty value detected!')
        continue
    print(f'Name = {name}')
# Use CONTINUE to skip bad or empty data without stopping the whole loop.

# PASS Statement (When to pass?)
# It is a placeholder where nothing happens (for now.. just keep going.. do nothing...)
# Iteration without having a condition (just a placeholder to be changed later)
names = ['john', 'maria', '', 'max']
for name in names:
    if name == '':
        pass # todo: Handle Empty Value
    print(f'Name = {name}')

names = ['john', 'maria', '', 'max']
for name in names:
    if name == '':
        name = name.replace('', 'unknown') # Handling Empty Value
    print(f'Name = {name}')

# Break vs Continue, Applications - 
# Loop through a list of days and print only the working days, skipping the weekends.
days = ['Mon', 'Sun', 'Wed', 'Tue']
for day in days:
    if day in ['Sat', 'Sun']:   # Avoid hardcoding values inside FOR or IF. Instead, define them as variables.
        continue
    print(f'Workday: {day}')

days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']   # Correct approach
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')

# Scan emails to block unsafe data from entering the system.
emails = [
    'data@gmail.com',
    'max@outlook.in',
    'DROP TABLE USERS;',   # SQL Injection Threat
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email: {email}')


