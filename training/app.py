# Hello World
# print ('Hello world')
# print ("*" * 10)

# Variable, Integer, Float, Boolean 
# price = 10
# rating = 4.9
# is_published = True
# print (price)

# Exercise variable, integer, float and boolean
# name = "John Smith"
# age = 20
# is_new = True
# print (name)
# print (age)
# print (is_new)

# Getting Input
# name = input("what is your name? ")
# print ("Hello " + name)

# Exercise Getting Input
# full_name = input("what is yourname? ")
# color = input("what is your favorite color? ")
# print (full_name + " likes " + color)

# Type Conversion
# change date type exp str to int use int() or str(), float(), bool()
# birth_year = input("birth year: ")
# print(type(birth_year))
# age = 2025 - int(birth_year)
# print(type(age))
# print(age)

# exercise type conversion
# weight = input("how much your weight in kilograms? ")
# ons = 100 * int(weight)
# print(ons)
# weight_lbs = input("berat-badan (lbs) : " )
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)

# ---------------------------------------->
# Strings
# course = 'python for "beginner"'
# print(course)
# course_1 = "Python for beginner"
# print(course_1)
# course_2 = "python's for beginner"
# print(course_2)
# course_3 = '''
#
# hello john
#
# this is my first email
#
# thank you for
# your support
#
# '''
# print(course_3)
# course_4 = "Darizatun nisa muslimah"
# print(course_4[:])
# print(course_4[0])
# print(course_4[-1])
# print(course_4[10:15])
# print(course_4[1:-1])
# another = course_4[:]
# print(another)
#<---------------------------------------

# formated strings
# first = "dudun"
# last = "darmawan"
# message = first + " [" + last + "] is a coder "
# msg = f'{first} [{last}] is a coder'
# print(msg)

# exercise formated strings
# num1 = 5
# num2 = 10
# result = "The sum of " + str(num1) + " and "+ str(num2) + " is " + str(num1) + " + " + str(num2)
# new_result = f"the sum of {num1} and {num1} is {num1 + num2}"
# print(new_result)

# strings method
# course = "dadan Darmawan and Darizatun nisa muslimah"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course)
# print(course.find("Darizatun"))
# print(course.replace("dadan", "Dadan"))
# print("Dadan" in course)

# aritmatic operations and operator precedence
# print(10 ** 5)
# X = 20
# X = X / 5
# X -= 2 
# print (X)
# y = (10 + 2) * 6 ** 2
# print(y)
# z = (2 + 3) * 10 - 3
# print(z)

#math funtions
# x = 2.1
# print(round(x)) # output 2
# print(abs(-123)) # output 123
# import math
# print(math.ceil(2.1)) # output 3
# print(math.floor(2.9)) # output 2

#if statement
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("wear warm clothes")
# else:
#     print("It's a lovely day")
# print("enjoy your day")

#exercise if statement
# price = 1000000
# has_good_credit = False

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"They need to put down payment: ${down_payment}")

#Logical operator
# has_good_income = False
# has_good_credit = True
# has_criminal_record = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("No eligible for loan")

#comparison operators
# temperature = 30
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print ("It's not a hot day")

#comparison operator exercise
# name = input("what is your name ? ")
# # name = "Dadan"
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good")

#weight converter program
# weight = int(input("how much your weight? "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"your weight is {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"your weight {converted} pounds")


# name = input("what is your name? ")
# if len(name) < 5:
#     print("you must input name at least 5 characters")
# elif len(name) > 20:
#     print("you mus input maximum name 20 charaters")
# else:
#     print("name looks goods")

# tempelature = int(input("how high is your body temperatur? "))
# result = input("Choose (F) for farenheit or (C) for cercius! ")
# if result.upper() == "F":
#     converted = tempelature * 0.32
#     print(f"your temperature is {converted} celcius")
# else:
#     converted = tempelature / 0.32
#     print(f"your temperature is {converted} farenheit")

# while loops
# i = 1
# while i <= 5:
#     print(i)
#     # print("d" * i)
#     i = i + 1
# print("done")

# making a guess game with while loop
# secret_number = 6
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit :
#     guess = int(input("guess number : "))
#     guess_count += 1
#     if guess == secret_number:
#         print ("you won!")
#         break
# else :
#     print("you failed!")

# secret_code = 8
# min_code = 0
# max_code = 3
# while min_code < max_code:
#     code = int(input("guess number : "))
#     min_code += 1
#     if code == secret_code:
#         print("you win!")
#         break
# else:
#         print("you failed")

# command = ""
# started = False
# #while command != "quit":
# while True :
#     command = input("> ").lower()
#     if command == "start" :
#         if started :
#             print("The car is already started")
#         else :
#             started = True
#             print("The car start")
#     elif command == "stop" :
#         if not started:
#             print("the car is already stopped!")
#         else :
#             started = False
#             print("The car stop")
#     elif command == "help" :
#         print("""
# start to start the car
# stop to stop the car
# quit to quit
#         """)
#     elif command == "quit" :
#         break
#     else:
#         print("Sorry, I don't undestand that")

# condition = ""
# mulai = False
# while True:
#     condition = input("> ").lower()
#     if condition == "berdiri" :
#         if mulai :
#             print("sudah masuk ruang makan")
#         else:
#             mulai = True
#             print("silahkan masuk ruang makan")
#     elif condition == "duduk" :
#         if not mulai :
#             print("orang sudah masuk ruang keluarga")
#         else:
#             mulai = False
#             print("silahkan masuk ruang keluarga")
#     # elif condition == "tidur" :
#     #     print("silahkan masuk kamar tidur")
#     elif condition == "tolong" :
#         print("""
# ketik berdiri untuk masuk ruang makan
# ketik duduk untuk masuk ruang keluarga
# ketik jongkok untuk keluar
# """)
#     elif condition == "jongkok" :
#         break
#     else:
#         print("perintah tidak diketahui")


#for Loop
# for item in "Python" :
#     print(item)

# for item in ["dadan", "wisnu", "jundi", "kalila"]:
#     print(item)

# for item in [1,2,3,4,5]:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(5, 10,2):
#     print (item)

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"total {total}")

# payment = [5, 10, 15]

# amount = 5
# for pay in payment:
#     amount = amount - pay
# print(f"amount is {abs(amount)}")

# nested loop
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# print("\n")
# for y_count in numbers:
#     print("x" * y_count)

# for loop exercise
# for i in range(3):
#     print(i)
# for char in "python":
#     print(char)
# for i in range(2, 5):
#     print(i, end='')
# print("\n")
# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# print("\n")
# for i in range(1, 6, 2):
#     print(i, end='')
# print("\n")
# for i in range (5):
#     if i % 2 == 0:
#         print(i)
# print('\n')
# for i in range(3):
#     for j in range(2):
#         print(i,j)
# print('\n')
# for i in range(4):
#     if i == 2:
#         break
#     print(i)
# print('\n')
# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# print('\n')
# for i in range(2, 5):
#     print(i, end='')
# print('\n')
# for i in range(3):
#     for j in range(i):
#         print(j, end='')
# print('\n')
# for i in range(3):
#     print(i)
# else:
#     print("done")
# print('\n')
# for i in range(3):
#     if i == 1:
#         break
#     print(i)
# else:
#     print('done')
# print('\n')
# for i in range(3):
#     for j in range(i):
#         print(j)
# print('\n')
# for i in range(3):
#     for j in range(i):
#         print(j)

#while loop exercise
# x = 0
# while x < 5:
#     print(x, end='')
#     x += 3
# print('\n')
# x = 10
# while x > 0:
#     if x % 2 == 0:
#         print(x)
#     x -= 1
# print('\n')
# x = 5 
# while x > 0:
#     print(x)
#     x -= 2
# print('\n')
# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x, end='')
#     x +=1
# print('\n')
# x = 1
# while x < 10:
#     x *= 2
#     print(x)
# print('\n')
# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x, end=' ')

# x = 5
# while x < 10:
#     for i in range(5):
#         x += 1
#         print(x)

#list
# numbers = [5, 3, 9, 6, 18, 11, 20]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# 2D List
# matriks = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matriks[0][1] = 10
# print(matriks[0][1])
# for row in matriks :
#     for item in row :
#         print(item, end='')

# # list Method#
# # append for add an element to the end of the list
# fruit = ["banana", "orange", "apple"]
# fruit.append("watermelon") 
# print(fruit)
# # insert for insert an element at a specific position
# numbers = [1,2,3,4]
# numbers.insert(4, 5)
# print(numbers)
# # extend for extend the list by adding elements from another iterable 
# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]
# list_1.extend(list_2)
# print(list_1)
# # remove for remove the first occurance of a specified element
# colors = ["blue", "green", "yellow", "purple"]
# colors.remove("purple")
# print(colors)
# # pop for remove an element at a specified index and return it
# numbers = [20,30,30,40]
# number = numbers.pop(3)
# print(number)
# print(numbers)
# # index for get the index of the first occurrence of tanhe element 
# names = ["Dadan", "Wisnu", "Haris"]
# name = names.index("Dadan")
# print(names.index("Wisnu"))
# print(name)
# print("------------------")
# # count for count occurrence a value
# cars = ["Santafe", "Pajero Sport", "Fortuner", "Santafe", "Palisade", "Crv", "Fortuner", "Santafe"]
# print(cars.count("Santafe"))
# # sort for sort the list in ascending order (Modify in place)
# numbers = [5,2,8,4,6,1,3,9]
# numbers.sort()
# print(numbers)
# # reverse for reverse of the element
# letters = ["a", "b", "c"]
# letters.reverse()
# print(letters)
# # copy for create a shallow copy of the list
# original = [1,2,3]
# copy_list = original.copy()
# original.insert(3, 4)
# print(original)
# print(copy_list)
# # clear for remove all element from the list
# items = ["Handphone", "Laptop", "Tablet"]
# items.clear()
# print(items)
# #exercise list method
# numbers = [1,2,3,4,5,1,2,3,4,5,1,1,2,3,4,5,4]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)
    
# tuples
# numbers = (1,2,3)
# numbers[0] = 10
# print(numbers)

# Unpacking Tuples
# cordinates = (1, 2, 3)
# x, y, z = cordinates
# print(x, y, z, end='')
# print()
# person = ("dadan", 18, "engineer")
# name, age, job = person
# print(f"\nmy name is {name}, \nmy age is {age}, \ni work as {job}")

# Dictionary
# student = {
#     "name" : "Dadan Darmawan",
#     "age" : 21,
#     "mayor" : "computer science"
# }
# print(student["mayor"])

# numbers = input("what is your phone? ")
# phone = {
#     "1" : "satu",
#     "2" : "dua",
#     "3" : "tiga",
#     "4" : "empat"
# }
# output = ""
# for ch in numbers:
#    output += phone.get(ch,"!") + " "
# print(output)

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)" : "😄",
#     "(:" : "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.keys())
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict)

# my_tuple = (1, 2, 3, 4)
# print(my_tuple[1:3])

# Function
# def my_biografy():
#     print("my name is Dadan")
#     print("i hope all my dream come be true")

# print("bismillah")
# my_biografy()
# print("alhamdullilah")

# # Parameters
# def greet(name):
#     """This function prints a greeting message."""
#     print(f"\nHello, {name}!")
# greet("Dadan")
# greet("Daruzatun")

# #exercise parameters
# def add(a, b): #parameters
#     return a + b 

# result = add(1,1) #argument
# print(result)

# #argument
# def show_numbers(*args):
#     print(args)  # Output: (1, 2, 3)

# show_numbers(1, 2, 3)

# def show_info(**kwargs):
#     print(kwargs)  # Output: {'name': 'Dadan', 'age': 25}

# show_info(name="Dadan", age=25)

# #return statement
# def numbers(number): # the first way
#     return(number*number)

# result = numbers(2)
# print(f'\n{result}')

# def numbers(number): # the second way
#     return(number*number)

# print(numbers(2))

# def numbers(number): # another way
#     print(number*number)

# numbers(2)

# #  creating a reusable function
# def converter_messanger(message):
#     words = message.split(' ')
#     emojis = {
#         ":)" : "😄",
#         "(:" : "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output

# message = input(">")
# converter_messanger(message)
# print(converter_messanger(message))

# Exceptions
# sytax errors:-->
# print("hello
# type errors:-->
# try :
#     result = "text" + 5
#     print(result)
# except TypeError as e:
#     print(f"TypeeError : {e}")
# try:
#     result = "text" + 5
#     print(result)
# except TypeError:
#     print("cannot add string to integer")
# Value error:-->
# try:
#     num = int("abc")
#     print(num)
# except ValueError:
#     print("cannot change value string to interger")
# try:
#     age = int(input("how old are you? "))
#     print(age)
# except ValueError:
#     print("the value must number")
# index error:-->
# try:
#     ist = (1,2,3,4)
#     print(ist[4])
# except IndexError:
#     print("cannot find index 4 because available is 0 until 3")
# key Error:-->
# try:
#     date = { "a" : 1, "b" :2}
#     print(date["c"])
# except KeyError:
#     print("nothing date c in dictionary date and date c is doesn't exist")
# ZeroDivision error:-->
# try:
#     date = 10/0
#     print(date)
# except:
#     print("cannot attempt divide a number by zero")    
# attribute error:-->
# try:
#     x = 5
#     x.append(10)
#     print(x)
# except:
#     print("int has no attribut")
# traceback
# import traceback

# try:
#     result = "text" + 5
# except TypeError:
#     print("A TypeError occurred!")
#     traceback.print_exc()  # Shows full error traceback

# classes
# class Name:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point1 = Name()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.move()

# point2 = Name()
# print(point2.x)

# construktor
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point = Point(10,20)
# print(point.x)
# point.x = 1
# print(point.x)

# # exercise construktor 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f"\nHello nama saya {self.name} and my age is {self.age}")
    

# person = Person("Dadan", 20)
# print(f"\n{person.name}")
# person.talk()

# wisnu = Person("wisnu", 17)
# wisnu.talk()

# # advance class and construktor exercise

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display_info(self):
#         print(f"\nmy car is : {self.brand} {self.model} ")

# car = Car("Toyota", "Yaris Cross")
# car.display_info()

# Inheritance
# class Mammal:
#     def walk(self):
#         print("walk")

# class Dog(Mammal):
#     pass

# class Cat(Mammal):
#     def meow(self):
#         print("Sound cat is meoww")

# dog1 = Dog()
# dog1.walk()

# cat1 = Cat()
# cat1.meow()

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.name = age

# class Student(Person):
#     def __init__(self, name, age, major):
#         super().__init__(name, age)
#         self.major = major

#     def introduce(self):
#         print(f"\nHello my name is {self.name} and i from {self.major} major")

# student = Student("Dadan", 20, "Computer Science")
# student.introduce()

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "bark"     

# class Cat(Animal):
#     def speak(self):
#         return "meow"
        
# dog = Dog("buddy")
# cat = Cat("whiskers")

# print(f"\n{dog.name} says {dog.speak()}")
# print(f"{cat.name} says {cat.speak()}")

#modules
# import converters
# converters.kg_to_lbs(60)

# from converters import lbs_to_kg
# lbs_to_kg(133.33334)

# import converters
# print(converters.kg_to_grams(60))

# from utils import find_max

# numbers = [2,3,7,4,30]
# max = find_max(numbers)
# print(max)

# import datetime
# #get the current date and time
# time = datetime.datetime.now()
# print("current date and time :", time)
# #get only the date
# today = datetime.date.today()
# print("today's date:", today)
# #formating dates
# now = datetime.datetime.now()
# rightnow = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formated Date and time:", rightnow)

# from datetime import datetime, timedelta

# # Get today's date
# today = datetime.today()

# # Calculate a future date (5 days from today)
# future_date = today + timedelta(days=5)

# print("Today:", today)
# print("Future Date:", future_date)

# Packages
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()

# from ecommerce import module
# print(module.greet("Dadan"))

# Generating Random Values
# import random

# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(f"\nrandom value : {random.randint(10, 20)}")

# members = ['john', 'marry', 'dadan']
# leader = random.choice(members)
# print(f"\n{leader}")

# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
    
# dice = Dice()
# print(dice.roll())

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)  # Output might be [3, 5, 1, 4, 2]

# working with directories  
# from pathlib import Path

# path = Path("ecommerce")
# print(path.exists())

# path = Path("emails")
# print(path.mkdir())

# path = Path("emails")
# print(path.rmdir())

# path = Path()
# for file in path.glob('*.py'):
#     print(file)


# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference

# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#     # cell = sheet['a1']
#     # cell = sheet.cell(1,1)
#     # print(cell.value)
#     # print(sheet.max_column)

#     for row in range(2, sheet.max_row + 1):
#         #print(row)
#         cell = sheet.cell(row,3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row,4)
#         corrected_price_cell.value = corrected_price

#     values = Reference(sheet, 
#                     min_row=2, 
#                     max_row=sheet.max_row, 
#                     min_col=4, 
#                     max_col=4
#                     )
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')

#     wb.save(filename)


