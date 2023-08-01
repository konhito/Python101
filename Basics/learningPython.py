# variable = a reusable container for storing a value
#                   a variable behaves as if it were the value it contains

# INTEGER
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance}Km")
print(f"The price is ${price}")

# STRING
name = "Bro"
food = "pizza"
email = "Bro123@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# BOOLEAN
online = True
for_sale = False
running = False

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

name = "Bro"
age = 21
gpa = 1.9
student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

name = bool(name)
print(name)
# EXERCISE 1 MAD LIBS
# ------------------------------------------------
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# ------------------------------------------------
# EXERCISE 2 AREA CALC
# ------------------------------------------------
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# area = length * width
# print(f"The area is: {area}cm^2")

# ------------------------------------------------
# EXERCISE 3 SHOPPING CART
# ------------------------------------------------
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")


# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# —---------------------
#   EXAMPLE 1
# —---------------------
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ sign up")

# —---------------------
#   EXAMPLE 2
# —---------------------
response = input("Do you want food (Y/N)?: ")

if response == "Y":
    print("Have some food")
else:
    print("No food for you!")

# —---------------------
#   EXAMPLE 3
# —---------------------
name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")

# —---------------------
#   EXAMPLE 4
# —---------------------
online = False

if online:
    print("You are online")
else:
    print("You are offline")

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
