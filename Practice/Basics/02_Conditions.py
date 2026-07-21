## Conditions in Python

## IF conditions 

age = 20

if age >= 18:
    print("You can vote")
    print("You are eligible to participate in the democratic process")



age = 15 
if age >= 18: 
    print("you can vote") # No output will be printed as the condition is False


a = int(input("Enter a number:"))
if a >=0:
    print("a is a positive number")


marks = int(input("Enter your marks : "))
if marks >=35:
    print("you have passed the Test ") 



salary = int(input("Enter your salary :"))  
if salary >= 50000:
    print("you are eligible for the loan")

## IF-ELSE conditions

age = int(input("Enter your age for vote:"))
if age >=18:
    print("You can vote")
else:
    print("You are underage , cannot vote")




age = int(input("Enter your age for driving license:"))
if age >=21:
    print("You can apply for a driving license")
else:
    print("You are underage , cannot apply for a driving license") 


# Check if a number is even or odd.
num = int(input("check the  number:"))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Check if marks are pass or fail (35+ = Pass).

marks = int(input("Enter your marks:"))
if marks >= 35:
    print("Your are paased")
else:
    print("You are failed")


# Check if the password is correct or not.
password = (input("Enter the password:"))
if password == "python123":
    print("Correct Password",)
else:
    print("Incorrect Password")



# If-elif-else conditions
marks = int(input("Enter Your Marks:"))

if marks >= 90:
    print("You have scored A grade")
elif marks >=80:
    print("You have scored B grade")
elif marks >=70:
    print("You have scored C grade")
elif marks >=60:
    print("You have scored D grade")
else:
    print("You have scored F grade")


Traffic light condition

light = (input("Enter the Light's Color:"))
if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
elif light =="Green":
    print("Go")



age = int(input("Enter Your age :"))
if age <=5:
    print("Free Entry")
elif age <=17:
    print("Child Ticket")
elif age <=18:
    print("Adult Ticket")
elif age <=60:
    print("Senior Citizen Ticket")
else:
    print("Invalid Age")


age = int(input("Enter Your age :"))
citizen = input("Enter your citizenship :")
if age <=18 and citizen == "Indian":
    print("You are Adult And Eligible for vote")


age = int(input("Enter Your age :"))
if age >=18 and age <=60:
    print("You are eligible for Driving License")
else:
    print("You are not eligible")

marks = int(input("Enter Your marks :"))
grace = input("Enter Your Grace Marks :")
if marks >=35 or grace == "yes":
    print("You are Passed")
else:
    print("You are Failed")


user_name = "Python"
password = "python123"
input_user_name = input("Enter your username:")
input_password = input("Enter your password:")
if input_user_name == user_name and input_password == password:
    print("Login Successful")
else:
    print("Login Failed")



num = int(input("Enter a number:"))
if num >= 0 and num <=100:
    print("The number is between 0 and 100")
else:
    print("The number is not between 0 and 100")


age = int(input("Enter your age:"))
citizenship = "Indian"
citizenship = input("Enter your citizenship:")
if age >= 18 and citizenship == citizenship:
    print("You are adult and Indian citizen,")


# Nested if-else conditions


Job Criteria

age = int(input("Enter your age:"))
degree = input("Do you have a degree? (yes/no):")
if age >= 18:
    if degree == "yes":
        print("You are eligible for the job")
    else:
        print("Degree required")
else:
    print("Age must be 18+")       


# Admission Criteria 

age = int(input("Enter your Age :"))
marks = int(input("Enter your Marks :"))
if age >=18:
    if marks >=75:
        print("you are eligible for admission")
    else:
        print("Minimum marks required for admission is 75 or above")
else:
    print("You are underage, Age must be 18+ ")


# ATM Pin + Balance check
correct_pin = 1234
balance = 50000
user_pin = int(input("Enter Your Pin: "))
if user_pin == correct_pin:
    print("your available balance is :", balance)
else:
    print("Error, Wrong Pin")
