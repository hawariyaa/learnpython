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
'''












