#  What is a Module in Python
# A module is just a file that contains Python code — it can have functions, variables, and classes.
# You can use that code in other Python files by importing the module
# for example you haveafile name
# math_tools.py
def add(a, b):
    return a + b
#  Why use modules?
# To keep your code organized To reuse code easily To split big programs into small, manageable files
#  What is a Function in Python? A function is a block of code that does a specific task. You define it once and use it many times
def greet(name):
    return f"Hello, {name}!"

print(greet("Ali"))  # Output: Hello, Ali!
# 1. Built-in Functions
# These are already made by Python — you can use them directly.
#  Examples:
print("Hello")       # prints something
len("hello")         # gives length
type(123)            # tells the type
# Some common ones:

print()

len()

input()

type()

int(), str(), float() 

# 2. User-defined Functions
# These are functions that YOU create to do a specific task.
#  Example:
def say_hello():
    print("Hello, World!")

say_hello()  # Calls the function
# You define your own function using def and call it when needed.
#  Based on Input/Output, User-defined Functions are of 4 Types:
# Type	Input (Parameters)	Output (Return)	Example
# 1. No Input, No Output	def hello(): print("Hi")
# 2. Input, No Output		def greet(name): print(name)
# 3. No Input, Output		def give_number(): return 5
# 4. Input and Output		def add(a, b): return a + b

#  What is Exception Handling?
# Sometimes your code can crash due to errors (like dividing by zero or wrong input).
# Exception handling helps you catch and handle those errors without crashing your program.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result is:", result)
finally:
    print("Done!")

    #  What is File Handling?
# File handling means reading from or writing to files (like .txt files) using Python.

#  Common File Modes:
# Mode	Meaning
# 'r'	Read (default)
# 'w'	Write (overwrite)
# 'a'	Append (add at end)
# 'x'	Create new file
# 'b'	Binary mode (e.g., images)
# 't'	Text mode (default)
#  Open a File:
file = open("myfile.txt", "r")  # open for reading
# Read from a File:
file = open("myfile.txt", "r")
content = file.read()
print(content)
file.close()
# Or read line by line:
for line in file:
    print(line)
#  Write to a File:
file = open("myfile.txt", "w")
file.write("Hello, this is Python!")
file.close()
#  'w' will overwrite the file. Use 'a' to add content without deleting existing content.

#  Best Practice: Use with
with open("myfile.txt", "r") as file:
    data = file.read()
    print(data)
# No need to call file.close() — Python will do it automatically.
# Time & Epoch in Python
# Epoch: Time starts from Jan 1, 1970. Computers count time from here in seconds.

# time.time(): Gives current time in seconds since epoch (called ticks).

# time.localtime(): Converts ticks to local time.

# time.asctime(): Gives time in a readable string format.

# Calendar Module
# Use the calendar module to see any month’s calendar.


import calendar
print(calendar.month(2025, 1))
#  Date & Time with datetime module
# datetime.now(): Shows current date & time.

# date(2023, 4, 19): Creates a specific date.

# strftime(): Formats date (e.g., show year, month, day name).
print(x.strftime("%A"))  # Day name
print(x.strftime("%Y"))  # type: ignore # Year
# Math Module in Python
# Built-in math functions:

# abs(), pow(), round(), max(), min()

# From math module:

# math.sqrt(), math.sin(), math.factorial(), math.log()

# Constants: math.pi, math.e, math.inf, math.nan

#  Special Values
#  NaN (Not a Number)
# Used when a result makes no sense (e.g., 0/0).

# math.isnan(x) checks if a value is NaN.

# NaN is not equal to anything, even itself.

# Infinity (math.inf)
# Represents infinity (very large number).
# Greater than all numbers-math.inf is negative infinity. Doing things like inf - inf gives NaN.











