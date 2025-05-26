# 1. running program
# print("I Like Pizza")
# print("It's really good")

# 2. Variable = A container for a value (String, Integer, Float, Boolean)
#            A Variable behaves as if it was the values it contains
# # String :
# first_name = "Dadan"
# food = "Pizza"
# email = "dadan@fake.com"
# # Integer :
# age = 20
# num_of_student = 30
# npm = 2269700049
# # Float :
# price = 5.87
# gpa = 4.00
# distance = 5.5
# # Boolean
# is_student = True
# for_sale = True
# is_online = False

# 3. Type casting = the process of converting a variable from one data type to another
#                str(), int(), float(), bool()
# name = "Dadan Darmawan"
# age = 25
# gpa = 4.0
# is_student = True
# print(type(age))
# print(float(age))
# print(bool(name))

# 4. input() = A function that prompt the user to enter data
#           Return the entered data as a string
# name = input("What is your name? ")
# age = int(input("how old are you? "))
# age += 1
# print(f"hello {name}")
# print("Happy Birthday")
# print(f"you are {age} years old")

# # Exercise 1 Rectangle Area Calc
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = length * width
# print(f"The area of the retangle is {area} cm^2")

# # Exercise 2 shopping cart program
# item = input("What item would you like to bought?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is : ${total}")

# 5. Mad Libs Game
# adjective1 = input("what is the the first adjective?: ")
# adjective2 = input("what is the the second adjective?: ")
# animal1 = input("what is name of the animal?: ")
# animal2 = input("what is name of the animal?: ")
# verb_past_tense = ("what is the verb, past tense?: ")
# adjective3 = input("what is the the second adjective?: ")
# food = input("what is their ate?: ")
# beverage = input("what is their drank?: ")
# adjective4 = input("what is the the second adjective?: ")
# print(f"A Day at the Zoo Today, I went to the zoo with my {adjective1} friend.")
# print(f"We saw a {adjective2} {animal1} jumping around in its enclosure.")
# print(f"Then, we watched as a {animal2} {verb_past_tense} near the pond.")
# print(f"It was so {adjective3}! After that, we ate some {food} and drank {beverage}. It was the most {adjective4} day ever!")

# 6. Arithmetic & math
# a. section 1
# friends = 4
# friends = friends + 1
# friends += 1
# friends = friends - 1
# friends -= 1
# friends = friends * 2
# friends *= 2
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends = friends % 3
# print(friends)
# b. section 2
# x = 3.14
# y = - 4
# z = 5
# a = 2
# result = round(x) #output 3
# result = abs(y) #output 4
# result = pow(z, a) #output 25
# result = pow(3, 2) #output 6
# result = max(x, y, z, a) #output 5
# result = min(x, y, z, a) #output -4
# print(result)
# c. section 3
# import math
# x = 9.1
# y = 9.9
# z = 9
# print(math.pi) #output 3.141592653589793
# print(round(math.pi, 2)) #output 3.14
# result = math.sqrt(z) #output 3
# result = math.ceil(x) #output 10
# result = math.floor(y) #output 9
# print(result)
# d. section 4 - radius a circle
# import math
# radius = float(input('Enter the Radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f"The Circumference is: {circumference}cm")
# print(f"The Circumference is: {round(circumference, 2)}cm")
# e. section 5 - area a cirlce
# import math
# radius = float(input("Enter the radius of a cirlce: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the cirlce is : {round(area, 2)}cm")
# f. section 6 - find side c on trapezium
# import math
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"side c = {c}")

# 7. if = Do some code only IF some condition is True
#      Else do something else
# section 1. input age to sign up
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are now signed up")
# elif age <= 0:
#     print("You Haven't been born yet")
# elif age >= 100: #it false because in begin we type >18
#     print("You are too old to sign up")
# else:
#     print("You must tobe 18+ to sign up")
# section 2. question about food
# response = input("Would you like food? (Y/N) ")
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")
# section 3. Enter your name
# name = input("Enter your name!: ")
# if name == "":
#     print("You Did not type in your name!")
# else:
#     print(f"Hello {name}")
# section 4. boolean online / offline
# online = True
# offline = False
# if offline:
#     print("The user is Online")
# else: 
#     print("The user is offline")

# 8. Python Calculator Program
# operator = input("please choose your operator between '+', '-', '*', '/': ")
# num1 = float(input("Enter your 1st number: "))
# num2 = float(input("Enter your 2nd number: "))
# if operator == "+":
#     result = num1 + num2
#     print(f"result is: {round(result, 1)}")
# elif operator == "-":
#     result = num1 - num2
#     print(f"result is: {round(result, 1)}")
# elif operator == "/":
#     result = num1 / num2
#     print(f"result is: {round(result, 1)}")
# else:
#     print(f"The operator {operator} is not available")

# 9. Python weight program
# weight = float(input("Enter your Weight!: "))
# unit = input("What are input your units, Kilograms or Pounds (K/L)?")
# if unit == "K":
#     result = weight / 0.45
#     print(f"Your weight in Pounds is {round(result, 2)}")
# elif unit == "L":
#     result = weight * 0.45
#     print(f"Your weight in Kilograms is {round(result,2)}")
# else:
#     print(f"Your input in weight is {weight} that is not a number or you type {unit} wheen choose unit")

# 10. Temperetare conversion in pyhton
# unit = input("Is this temperature in Celcius or Fahrenheit (C/F)")
# temp = float(input("Enter the temperature: "))
# if unit == "C":
#     result = round((temp * 9) / 5 + 32, 1)
#     print(f"The conversion temp is {result} fahrenheit")
# elif unit == "F":
#     result = round((temp - 32) * 5 / 9, 1)
#     print(f"The conversion temp is {result} Celcius")
# else:
#     print(f"{unit} is an invalid unit of measureme")

# 11. Logical operators = Evaluate multiple conditions (or, and, not)
#                         or  = at least one condition must be True
#                         and = both conditions must be True
#                         not = inverts the conditions (not false, not true)
# section 1. and
# is_adult = True
# has_ticket = False
# if is_adult and has_ticket:
#     print("You can enter.")
# else:
#     print("Entry denied.")
# section 2. or
# is_vip = True
# has_regular_ticket = False
# if is_vip or has_regular_ticket:
#     print("You can enter.")
# else:
#     print("Entry denied.")
# section 3. not
# is_raining = True
# if not is_raining:
#     print("Let's go outside!")
# else:
#     print("Better stay indoors.")

# 12. conditional expressions = A one-line shortcut for the if-else statment (ternary operator)
#                           print or assign one of two values based on a condition
#                           x if condition else y
# num = 11
# a = 5
# b = 6
# age = 17
# temperature = 30
# user_role = "users"
# print("positive" if num >=0 else "negative")
# print("Even" if num % 2 == 0 else "Odd")
# print("a" if a > b else "b")
# print("a" if a < b else "b")
# print("addult" if age >= 18 else "child")
# print("Hot" if temperature >=28 else "Cold")
# access_level = "full access" if user_role == "admin" else "limited access"
# print(access_level)

# 13. string methods
# name = input('Input your name!: ') #dadan, DADAN, 1234 566
# result = print(len(name)) #output 3
# result = name.find('n') #find number from characters 0 - ~
# result = name.rfind("n") #find the reverse number from character 0 - ~
# result = name.capitalize() #output Dadan
# result = name.upper() #output DADAN
# result = name.lower() #output dadan
# result = name.isdigit() #output False
# result = name.isalpha() #output True
# result = name.count(' ') #output 1
# result = name.replace(' ', '-') #ouput 1234-5678-9012
# print(help(str))
# print(result)
# # excercise string
# username = input("Enter your username!: ")
# if len(username) <= 12:
#     print("your name must 12 characters")
# elif not username.find(' ') == -1:
#     print("sorry username can not contains space")
# elif not username.isalpha():
#     print("Sorry username cant contains numbers")
# else:
#     print(f"hello {username}")

# 14. String indexing : Accessing elements of a sequence using [] (indexing operator)
#                       [start : end : step]
# credit_numbers = "1234-5678-1234-5678"
# print(credit_numbers)
# print(credit_numbers[0])
# print(credit_numbers[:4])
# print(credit_numbers[5:9])
# print(credit_numbers[5:])
# print(credit_numbers[-1])
# print(credit_numbers[::3])
# print(credit_numbers[::-1])
# last_digit = credit_numbers[-4:]
# print(f"is your last digit credit number is XXXX-XXXX-XXXX-{last_digit}")

# 15. format specifers = {:flags} format a value based on what 
#                                 flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :(03) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# example format specifers
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# price4 = 3000.14159
# price5 = -9870.65
# price6 = 1200.34
# print(f"Price 1 is ${price1:.2f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.2f}")
# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")
# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")
# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")
# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")
# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")
# print(f"Price 1 is ${price1:=}")
# print(f"Price 2 is ${price2:=}")
# print(f"Price 3 is ${price3:=}")
# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")
# print(f"Price 1 is ${price4:,}")
# print(f"Price 2 is ${price5:,}")
# print(f"Price 3 is ${price6:,}")
# print(f"Price 1 is ${price4:10,.2f}")
# print(f"Price 2 is ${price5:10,.2f}")
# print(f"Price 3 is ${price6:10,.2f}")

# 16. While loops = execute some code WHILE some condition remains true
# #analogy
# name = input('Enter yourname: ')
# if name == "":
#     print("You did not enter yourname")
# else:
#     print(f"Hello {name}")
# #practice
# name = input('Enter yourname: ')
# while name == "":
#     print("You did not enter yourname")
#     name = input('Enter yourname: ')
# print(f"Hello {name}")
# #more practice
# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"you are {age} years old")
# excercise while loop
# food = input("Enter a food you like (q to quit)")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit)")
# print("bye")
# #more exercise while loop
# num = int(input("Enter a number between 0 - 10: "))
# while num < 0 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 0 - 10: "))
# print(f"your number is {num}")

# 17. compound interest calculator
# principle = 0
# time = 0
# rate = 0
# while principle <= 0:
#     principle = float(input("Enter the principle!: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")
# while rate <= 0:
#     rate = float(input("Enter the interest rate!: "))
#     if rate <= 0:
#         print("Rate can't be less than or equal to zero")
# while time <= 0:
#     time = int(input("Enter the time in years!: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s : ${total:.2f}")
# #other ways
# principle = 0
# time = 0
# rate = 0
# while True:
#     principle = float(input("Enter the principle!: "))
#     if principle < 0:
#         print("Principle can't be less than zero")
#     else:
#         break
# while True:
#     rate = float(input("Enter the interest rate!: "))
#     if rate < 0:
#         print("Rate can't be less than zero")
#     else:
#         break
# while True:
#     time = int(input("Enter the time in years!: "))
#     if time < 0:
#         print("Time can't be less than zero")
#     else:
#         break
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s : ${total:.2f}")

# for loops = execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc.
# for counter in range(1,11):
#     print(counter)
# print("Done")
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New Year")
# print("Done")
# for x in range(1,11,5):
#     print(x)
# print("Done")
# credit_card = "1234-5678-9012-3456"
# for value in credit_card:
#     print(value)
# print("Done")
# for x in range(1, 21):
#     if x == 5:
#         continue
#     else:
#         print(x)
# print("Done")
# for x in range(1, 21):
#     if x == 5:
#         break
#     else:
#         print(x)
# print("Done")

# 19. countdown timer program
# import time
# my_time = int(input("Enter your time in seconds!: "))
# for x in reversed(range(0, my_time)):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's UP!")
# print("Done")
# import time
# my_time = int(input("Enter your time in seconds!: "))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's UP!")
# print("Done")

# 20. Nested Loops = A loop within another loop (outer, inner) 
#                    outer loop:
#                       inner loop:
# for x in range(3):
#     for y in range(1,11):
#         print(y, end="")
#     print()
# print("Done")
# coloumn = int(input("Enter your # for coloumn: "))
# rows = int(input("Enter your # for rows: "))
# symbol = input("Enter your symbols: ")
# for x in range(rows):
#     for y in range(coloumn):
#         print(symbol, end="")
#     print()
# print("Done")
# number = 5
# for x in range(number):
#     for y in range(x):
#         print(x, y)
#     print("Done")

# 21. list, sets, and tuples
# collection     = single "variable" used to store multiple values 
#       list     = [] ordered and changeable, Duplicates OK 
#       Set      = {} unordered and immutable, but add/remove OK. No duplicates 
#       Tuples   = () ordered and unchangeable. Duplicates OK. Faster
# # list
# fruits = ["Banana", "Orange", "Coconut", "Apple"]
# print(fruits)
# print(fruits[0])
# print(fruits[0:2])
# print(fruits[::2])
# print(fruits[::-1])
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# list method
# fruits[0] = "pineapple"
# fruits.append("watermelon")
# fruits.remove("Apple") 
# fruits.insert(4, "chery")
# fruits.sort()
# fruits.reverse()
# fruits = fruits.count("Banana")
# print(fruits)
# for fruit in fruits:
#     print(fruit)
# # set
# fruits = {"Banana", "Orange", "Coconut", "Apple", "Banana"}
# print(dir(fruits))
# print(help(fruits)sss)
# print(len(fruits))
# print("pineapple" in fruits)
# fruits[0] = "pineapple"
# fruits.add("pineapple")
# fruits.remove("Orange")
# fruits.pop()
# fruits.clear()
# print(fruits)
# # tuple
# fruits = ("Banana", "Orange", "Coconut", "Apple", "Banana")
# print(dir(fruits))
# print(help(fruits)sss)
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("Apple"))
# print(fruits.count("Banana"))
# print(fruits)
# for fruit in fruits:
#     print(fruit)

# 22. shopping cart program
#       list     = [] ordered and changeable, Duplicates OK 
#       Set      = {} unordered and immutable, but add/remove OK. No duplicates 
#       Tuples   = () ordered and unchangeable. Duplicates OK. Faster
# foods = []
# prices = []
# total = 0
# while True:
#     food = input("Enter your foods to buy! or type (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}!: $"))
#         foods.append(food)
#         prices.append(price)
# print("---- YOUR CART ----\n")
# for food in foods:
#     print(food, end=" ")
# for price in prices:
#     total += price
# print()
# print(f"total your food is ${total:.2f}")
# print("\n----Thank you for purchase----")

# 23. 2D collectios / nestred loop
# fruit = ["banana", "apple", "orange"]
# drink = ["juice", "coffee", "milk"]
# food = ["pizza", "hamburger", "bread"]
# meal = [fruit, drink, food]
# print(meal[0])
# print(meal[0][1])
# meal = [["banana", "apple", "orange"],
#         ["juice", "coffee", "milk"],
#         ["pizza", "hamburger", "bread"]]
# # print(meal[0][1])
# for collection in meal:
#     for list in collection:
#         print(list, end=" ")
#     print()
# numbers = ((1, 2, 3),
#            (4, 5, 6), 
#            (7, 8, 9), 
#            ("*", 0, "#"))
# for number in numbers:
#     for numped in number:
#         print(numped, end=" ")
#     print()
# 23. Question quiz game

# questions = ("How many elements are in the periodic table?: ",
#             "Whic animal lays the large eggs?: ",
#             "What is the most abundant gas in earth's atmosphere?: ",
#             "How many bones are in the human body?: ",
#             "Which planet in the solar system is the hottest?: ")

# options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D.  Hydrogen"), 
#            ("A. 206", "B. 207", "C. 208", "D. 209"), 
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("------------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter your answer! (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct! ")
#     else:
#         print("Incorrect!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1    
    
# print("------------------------------")
# print("            RESULT            ")
# print("------------------------------")

# print("Answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("Guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")


# 25. Dictionary = a collection of {key : value} pairs 
#                  ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C.",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print("That capital doesn't exist")

# if capitals.get("China"):
#     print("That capital exist")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "NewYork"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

# for key, value in capitals.items():
#     print(f"{key} : {value}")

# 26. concession stand program
# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "fries": 5.00,
#         "chips": 2.50,
#         "pretzel": 3.50,
#         "soda": 3.00,
#         "lemonade": 4.25}
# cart = []
# total = 0

# print("------ MENU ------")
# for key, value in menu.items():
#     print(f"{key:10} : ${value:.2f}")
# print("------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("------ Order ------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: ${total:.2f}")
# print("-------------------")


# 27. random numbers
# import random

# print(help(random))
# print(random.randint(1, 6))
# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# print(random.randint(low, high))
# print(random.choice(options))
# random.shuffle(cards)

# print(cards)


# 28. number guessing game
# import random

# lowest_num = 0
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} dan {highest_num}")

# while is_running:
    
#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Select a number between {lowest_num} dan {highest_num}")
#         elif guess < answer:
#             print("To Low! Try again")
#         elif guess > answer:
#             print("To High! Try again")
#         else:
#             print(f"Correct!! The answer was {answer}")
#             print(f"Number of guesses is {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")


# 29. rock, paper, scissors game
# import random

# print("Python Choice a rock, paper, scissors game")
# options = ("rock", "paper", "scissors")
# playing = True

# while playing:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice between (rock, paper, scissors): ")

#     print(f"Player : {player}")
#     print(f"computer : {computer}")

#     if player == computer:
#         print("It's a tie")
#     elif player == "rock" and computer == "scissors":
#         print("You Win!!")
#     elif player == "paper" and computer == "rock":
#         print("You Win!!")
#     elif player == "scissors" and computer == "paper":
#         print("You Win!!")
#     else:
#         print("You Lose!!")

#     if not input("Do you want Play again (y/n)?: ").lower() == "y":
#     # if not play_again == "y":
#         playing = False

# print("Thanks for playing this game")

# 30. Dice roller program
# import random

# # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# # "● ┌ ─ ┐ │ └ ┘"
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"
# dice_art = {
#     1:("┌─────────┐", 
#        "│         │",
#        "│    ●    │",
#        "│         │",
#        "└─────────┘"),
#     2:("┌─────────┐",
#        "│  ●      │",
#        "│         │",
#        "│      ●  │",
#        "└─────────┘"),   
#     3:("┌─────────┐",
#        "│  ●      │",
#        "│    ●    │",
#        "│      ●  │",
#        "└─────────┘"),
#     4:("┌─────────┐",
#        "│  ●   ●  │",
#        "│         │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#     5:("┌─────────┐",
#        "│  ●   ●  │",
#        "│    ●    │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#     6:("┌─────────┐",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # print(dice)

# # ----------------vertical dice-----------------------
# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)

# # ----------------horizontal dice----------------------
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total : {total}"j)

# 31. function = A block of reusable code 
#                place() after the function name to invoke it

# example if not use a function
# print("Happy birthday to you")
# print("You are old")
# print("happy birthday to you")
# print()
# print("Happy birthday to you")
# print("You are old")
# print("happy birthday to you")
# print()
# print("Happy birthday to you")
# print("You are old")
# print("happy birthday to you")
# print()

# example use a function
# def happy_birtday():
#     print("Happy birthday to you")
#     print("You are old")
#     print("happy birthday to you")
#     print()

# happy_birtday()
# happy_birtday()
# happy_birtday()

# paramater function
# def happy_birtday(name, old):
#     print(f"Happy birthday {name}")
#     print(f"You are {old} years old")
#     print("happy birthday to you")
#     print()

# happy_birtday("Dadan", 21)
# happy_birtday("Wisnu", 18)

# another example parameter function
# def display_invoice(name, amount, due_date):
#     print(f"Hello {name}")
#     print(f"Your bill is ${amount:.2f} is due: {due_date}")

# display_invoice("Dadan", 5.95, "25/05")

# return = statement used to end a function 
#          and send a result back to the caller

# def add(x, y):
#     return(x + y)

# def subtract(x, y):
#     return(x - y)

# def divide(x, y):
#     return(x / y)

# def multiply(x, y):
#     return(x * y)

# print(add(5, 2))
# print(subtract(5, 2))
# print(divide(5, 2))
# print(multiply(5, 2))

# def full_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return (f"Hello {first} {last}")
#     # return "hello " + first + " " + last

# name = full_name("dadan", "darmawan")
# print(name)


# default argument = A default value for certain parameters 
#                    default is used when that argument is omitted 
#                    make your functions more flexible, reduces # of arguments 
#                    1. postions, 2. DEFAULT, 3. keyword, 4. arbitrary

# import time

# without default argument
# def count(start, end):
#     for x in range(start, end):
#         print(x)
#         time.sleep(1)
#     print("Done")

# count(0, 10)

# with default argument
# def count(end, start=0):
#     for x in range(start, end):
#         print(x)
#         time.sleep(1)
#     print("Done")

# count(10, 5)

# another example default argemnts

# def net_price(list_price, discount=0, tax=0.01):
#     return list_price * (1 + discount) * (1 + tax)

# print(net_price(100))

# 33. keyword arguments = an argument preceded by an identifer
#                         helps with readability 
#                         order of arguments dosn't matter 
#                         1. positional 2. default 3. KEYWORD 4. arbitrary

# def full_name(greeting, tittle, first, last):
#     return f"{greeting}, {tittle}{first} {last}"

# print(full_name("Hello", tittle="mr.", last="Darmawan", first="Dadan"))



# 23. *args     = allows you to pass multiple non-key arguments
#               = allows you to pass multiple keyword-arguments 
#                 * unpacking operator 
#                 1. positional 2. default 3. keyword 4.ARBITRARY

# def add_operator(a, b):
#     return a + b

# print(add_operator(2, 2))

# def add_operator(*args):
#     print(type(args))

# add_operator(2, 2, 2)

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(2, 2))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Dadan", "stronger", "Darmawan")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street="Jl. Patinggi",
#               village="Bunihayu",
#               city="Subang",
#               state="Idn",
#               zip="41281")

# def print_address(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     if "village" in kwargs:
#         print(f"{kwargs.get("street")} {kwargs.get("village")}")
#     else:
#         print(f"{kwargs.get("street")}")

#     print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")

# print_address("Mr.", "Dadan", "Darmawan", "I",
#               street="Jl. Patinggi",
#               village="Bunihayu",
#               city="Subang",
#               state="Indonesia",
#               zip="41281")

# 35. Iterables = An object/collection that can return its elements one at a time, 
#                 allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]
# fruits = ("Banana", "Orange", "Grave")
# motorcycles = {"Honda", "Yamaha", "Suzuki"}
# my_dictionary = {"A" : 1,
#                  "B" : 2,
#                  "C" : 3}

# for number in reversed(numbers):
#     print(number, end=" ")
    
# print()
# for fruit in reversed(fruits):
#     print(fruit, end=" ")

# print()
# for motorcycle in motorcycles:
#     print(motorcycle, end=" ")

# print()
# for key, value in my_dictionary.items():
#     print(f"{key} : {value}")

# 36. Membership operators = used to test whether a value or variable is found in a sequence 
#                            (string, list, tuple, set or dictionary) 
#                            1. in 
#                            2. not in

# word = "APPLE"
# letter = input("guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# students = {"Dadan", "Wisnu", "Haris"}
# student = input("Enter the name of student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not student")

# if student not in students:
#     print(f"{student} was not student")
# else:
#     print(f"{student} is a student")
    
# grades = {"Dadan" : "A", 
#             "Wisnu" : "B", 
#             "Haris" : "C"}
# student = input("Enter name that you want find a grade of the student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"The student was not found")

# email = "dadan@gmail.com"

# if "@" in email and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# 37. List comprehensions = A concise way to create lists in python 
#                           compact an easier to read than traditional loops 
#                           [expression for value in iterable if condition]

# traditional loops
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

# list comprehensive
# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# squares = [x * 4 for x in range(1, 11)]
# print(squares)

# fruits = ["banana", "apple", "orange", "grave"]
# fruits = [x.capitalize() for x in fruits]
# fruit = [x.upper() for x in ["banana", "apple", "orange", "grave"]]
# fruit_chars = [x[0] for x in fruits]
# print(fruits)
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, 6, -7, 8]
# positive_nums = [nums for nums in numbers if nums >= 0]
# negative_nums = [nums for nums in numbers if nums < 0]
# even_nums = [nums for nums in numbers if nums % 2 == 0]
# odd_nums = [nums for nums in numbers if nums % 2 == 1]
# print(odd_nums)

# grades = [85, 77, 50, 90, 59]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)


# 38. match-case statements (switch) = An alternative to using many 'elif' statements 
#                                      Execute some code if a value matches a 'case' 
#                                      Benefits: cleaner and syntax is more readable

# traditional elif
# def day_of_week(day):
#     if day == 1:
#         return "It's Sunday"
#     elif day == 2:
#         return "It's Monday"
#     elif day == 3:
#         return "It's Tuesday"
#     elif day == 4:
#         return "It's Wednesday"
#     elif day == 5:
#         return "It's Thursday"
#     elif day == 6:
#         return "It's Friday"
#     elif day == 7:
#         return "It's Saturday"
#     else:
#         return "not a valid day"
    
# print(day_of_week(7))

# match case
# def day_of_week(day):
#     match day:
#         case 1:
#             return "It's Sunday"
#         case 2:
#             return "It's Monday"
#         case 3:
#             return "It's Tuesday"
#         case 4:
#             return "It's Wednesday"
#         case 5:
#             return "It's Thursday"
#         case 6:
#             return "It's Friday"
#         case 7:
#             return "It's Saturday"
#         case _:
#             return "not a valid day"
    
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _:
#             return False
        
# print(is_weekend("Sunday"))

# with | (or) operator
# def is_weekend(day):
#     match day:
#         case "Sunday" | "Saturday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False
        
# print(is_weekend("Monday"))


# 39. Modules = a file containing code you want to include in your program 
#               use 'import' to include a module (built-in or your own) 
#               useful to break up a large porgram reusable separate files

# ----------------------- main.py -----------------------
# print(help("modules")) # for see all available modules
# print(help("math")) # for see the math from modules

# import math
# print(math.pi)
# import math as m
# print(m.pi)
# from math import pi
# print(pi)
# from math import e
# print(e)
# print()
# a, b, c, d = 1, 2, 3, 4
# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)

# import example

# result = example.pi
# print(result)

# print(example.cube(2))
# print(example.square(2))
# print(example.circumference(2))
# print(example.area(2))

# 40. Variable scope = where a variable is visible and accessible
#     scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local
# def func1():
#     a = 1
#     print(a) 

# def func2():
#     b = 2
#     print(b) 

# func1()
# func2()

# Enclosed
# def func1():
#     x = 1

#     def func2():
#         print(x) 
#     func2()

# func1()

# Global
# def func1():
#     # x =1
#     print(x)

# def func2():
#     # x =2
#     print(x)

# x = 3

# func1()
# func2()

# Built-in
# from math import e

# def func1():
#     print(e)

# e = 3

# func1()

# 41. if __name__ = __main__ : (this script can be imported OR run standalone)
#                               functions and classes in this module can be reused 
#                               without the main block of code executing

# ex. library = import library for functionality
#               when running library directly, display a help page

# print(dir())
# print(__name__)

# from example import *
# print(__name__)

# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# def main():
#     print("This is script 1")
#     print("And you cannot see in the script2")
#     favorite_food("pizza")
#     print("GoodBye!")

# if __name__ == "__main__":
#     main() 


#  42. Banking program

def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to deposited: "))
    print("*********************")

    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter an amount to be withdraw: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        choice = input("Enter your choice between 1 - 4: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")
    print("*********************")
    print("Thank You! Have a nice day")
    print("*********************")

if __name__ == '__main__':
    main()
