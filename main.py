import math

print("new")
new_one = "what"
anotherone = "is"
num_1 = 2.3
print("new" + " " + new_one + " " + anotherone + " " + str(num_1) )
print(anotherone.upper())
print(6+14-4*16/8)
print(10 % 3)


print(math.floor(num_1))
print(math.ceil(num_1))

# simple calculator
'''
num_1 = input("enter first number :")
num_2 = input("enter second number: ")
result = float(num_1) + float(num_2)
print("the answer is: " + str(result))

# creating a mad-lib game
color = input("enter a color: ")
noun = input("enter a noun: ")
clebrity = input("enter celebrity name: ")


print("Roses are " + color)
print( noun + " is blue")
print("i love " + clebrity)
'''
# know lets see arrays or lists
random_items = ["kevin", "is", 14, 19.45, True, "yap"]
random_items.insert(0, False)
print(random_items[0])

#tuples tuples are list that can not be modified
important_names = ("mike", "dane")
print(important_names[0])
'''
#functions
name = input("enter name: ")
age = input("enter age: ")
def info(name1 , age1):
    print("your name is: " + name1 + " and your age is: " + str(age1))
info(name, age)
'''
# using the return
'''
def cube(num1, num2, num3):
    return float(num1) * float(num2) * float(num3)
num1 = input("enter a number: ")
num2 = input("enter a number: ")
num3 = input("enter a number: ")

value = cube(num1, num2, num3)
print(str(value))
'''
#lets see if statment
numm_1 = 2
numm_2 = 5
if numm_1 > numm_2:
    print("correct")
elif numm_2 > numm_1:
    print("wrong")
else:
    print("they are equal!")
'''
def calculator(num1, op, num2):
    if op == "+":
        print(float(num1) + float(num2))
    elif op == "-":
        print(float(num1) - float(num2))
    elif op == "*":
        print(float(num1) * float(num2))
    elif op == "/":
        print(float(num1) / float(num2))
    elif op == "%":
        print(float(num1) % float(num2))
    else:
        print("invalid operator!")

print("welcome to the simple calculator!")
num1 = input("enter first number: ")
op = input("enter an operator: ")
num3 = input("enter second number: ")

calculator(num1, op, num3)
'''
'''
#decitionaries have like key value pair
favorites = {
    1: "january",
    "birth": "addis ababa",
    "month": "march",
    22: "yap not yet",
}
print(favorites["month"])
while True:
    print(favorites)
    break
'''
'''
#for loops
anarray = [1, "kevin", "mike", 12]
for array in anarray:
    print(array)

#exponent functions
print(2**5) # this means 2 the power of 5

def exponent(base_num, pow_num):
    print(float(base_num)**float(pow_num))

def expow(base, pow):
    result = 1
    for index in range(pow):
        result = float(result) * float(base)
    return result

base = input("enter a base number: ")
pow = input("enter a power number: ")
exponent(base, pow)
print(expow(base, int(pow)))

#array inside an array
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[1][0])
for index in number_grid:
    for inside in index:
        print(inside)

# giraffe languge adding g to all the vowels and outputing it
def translate(phrase):
    translation = ""
    for index in phrase:
        if index in "AEIOUaeiou":
            if index.isupper() :
                translation += "G"
            else:
                translation += "g"
        else:
            translation += index
    print(translation)
phrase = input("enter any word: ")
translate(phrase)


try:
    number = int(input("enter a number: "))
    print(number)
    value = 10 / 0
except ZeroDivisionError as error:
    print(error)
except ValueError as value:
    print(str(value) + "try again!")

# how to open a file and what mode to use
# mode of use "r+" means read ane write the file
# "r" means read file
# "w" means write the file
# "a" means append or add information but you cant modify or change the information in the file
# then we are storing the file in a variable, after opening make sure to close the file.

employeefile = open("index.py", "w")


employeefile.write("nice = 'allofus'")


employeefile.close()

import index
import docx

print(nice)
#there are two types of modules built-in modules and exteranl modules
# google list of python modules, there you can see a lot of python modules u can import and work
# with will be very helpful to our project, select the version 3, look for them in different areas
# because there is someone who already wrote the python code that we are trying to do full or partioal
# so it can be very helpful

# class and objects helps us create our own data-type just like int, string
# to describe this class is the whole thing in this case the student and
# object is each student with there respective characters specified
# when we are calling the student and passing it value we are actually calling the init
# function and the values we passed are going to be stored the respective variables
# the self.name = name means the value the user passed in is equal to the name variable
# self is refering to the actual object like student1
# so what it means is the student object name(student1.name) is equal to the name we passed in
# in simple terms it means student1.name = mike
class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

student1 = student("mike", "biology", 3.3, False)
print(student1.major)
print(student1.gpa)


class questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompt = [
    "what are the color of apples?\n a. Red \n b.purple \n c.orange\n",
    "what are the color of bnannas?\n a. Red \n b.yellow \n c.orange\n",
    "what are the color of strawberries?\n a. Red \n b.purple \n c.orange\n",
]

# common thing is to store objects inside an array
questions = [
   questions(questions_prompt[0], "a"),
   questions(questions_prompt[1], "b"),
    questions(questions_prompt[2], "a"),
]

def asking(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you score is: " + str(score) + "/3")

asking(questions)


class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def ishonor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False



student1 = student("mike", "biology", 3.2)
print(student1.ishonor())
'''
'''
class chef:
    def makes_chicken(self):
        print("the chef makes a chicken!")
    def makes_salad(self):
        print("the chef makes a salad!")
    def makes_special_dish(self):
        print("the chef makes a special dish!")

 # the thing about inheritance is, like here the chinses chef can also cook what ever
 # the normal chef can cook, so here inside of the chinese_chef i want to be able to use
 # all the functionality(functions) that are contained inside of the chef class
 # if i have simliar function but different attribute i can override it.
class chinese_chef(chef):
    def makes_chicken(self):
        print("the chef makes orange chinkens!")
    def nuddles(self):
        print("the chinese chef can cook nuddles!")


newguy = chinese_chef()
print(newguy.makes_chicken())


import pandas as pd
new_dic = {
    "employee" : {"dave": {"id": "001", "salary": 2000}, "Ava": {"id": "002", "salary": 1000 }}
}
print(new_dic["employee"]["dave"]["id"])
new_dic["employee"]["dave"]["salary"] = 3000
print(new_dic.keys())
print(new_dic.values())
print(new_dic.get("employee"))
for x in new_dic["employee"]:
    print(x)

print(new_dic["employee"])

import pandas as pd
df = pd.DataFrame.from_dict(new_dic["employee"])
print(df)


import pandas as pd
new_dic = {
    "employee" : {"dave": {"id": "001", "salary": 2000}, "Ava": {"id": "002", "salary": 1000 }}
}

df = pd.DataFrame.from_dict(new_dic["employee"], orient='index')
print(df)
'''
myset = set()
myset.add(4)
myset.add(5)
myset.add(7)
myset.remove(5)
print(myset)
myset.clear()
print(myset)


print(id(number))
string[0] = m
print(id(number))
print(number)string = "hey"

a = 5
b = 5
print(id(a))
print(id(b))