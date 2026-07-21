
print("Hello Manish")
print("Welcome to Python Mastery")


# Variables 


name = "Manish"
age = 25
course = "Python Mastery"
print(name)
print(age)
print(course)

# Data Types 

name = "Manish"
age = 25
height = 5.9
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>


# User Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Type casting 
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

age = int(input("Enter your age: "))
print(type(age))  # <class 'int'>

int()
float()
str()
bool()



## Operators    

a = 10
b = 5 

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Assignment Operators

x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4

# Comparison Operators
print(a == b)  # Equal
print(a != b)  # Not Equal
print(a > b)   # Greater Than
print(a < b)   # Less Than
print(a >= b)  # Greater Than or Equal To
print(a <= b)  # Less Than or Equal To
# Return True or False 

# Logical Operators

True and false # Returns False
True or false # Returns True
not true # Returns False