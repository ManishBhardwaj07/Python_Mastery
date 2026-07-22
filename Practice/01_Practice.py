# Q 1 - write a program to check wether a person is eligible to vote.

age = int(input("Enter your age: "))
if age >= 18:
    print ("Eligible to vote")


## Q 2 - Write a program to check the largest of two numbers.
a = int(input("Enter the first number"))
b = int(input("Enter the second"))
if a>=b:
    print(a," is the largest number ")
else:
    print(b," is the largest number")
    
## Q 3 -     Take a sentence from the user and print:
# input = "python is awesome"
# Uppercase
# Lowercase
# Title Case

sentence = input("Enter the sentence:")
print(sentence.upper())
print(sentence.lower())
print(sentence.title())

# Q4 - Take a name from the user and print:
# First character
# Last character
# Reverse name
# user input is "Manish"

name = input("Enter your name ")
print(name[0])
print(name[-1])
print(name[::-1])

# Q5 - Take a sentence from the user and print:
# Number of times "a" appears.
# First occurrence of "Python".
#"python is awesome"

sentence = input("Enter Sentence:")
print(sentence.count("a"))
print(sentence.find("Python"))

# Q6 - take a sentence from the user 
# replace every "Java" with "python"

sentence = input("Enter the Sentence:")
print(sentence.replace("Java", "Python"))

# Q7 - Take a comma-separated string from the user.
# Convert it into a list.
# user input =  "Apple,Mango,Banana"
fruits = input("Enter fruits name:")
print(fruits.split(","))

# Q8 - Take a comma-separated string from the user.
# Convert it into a list.

file = input("Enter the File Name: ")

if file.endswith(".pdf"):
    print("Valid PDF File")
else:
    print("Not a PDF File")

text = "MachineLearning"

print(text[1:10:2]) # =  ahnLa

print(text[-8:-2]) # = earnin

print(text.replace("Learning", "AI")) # = MachineAI

text = "MachineLearning"

print(",".join(text.split("e"))) #  Machin,L,arning