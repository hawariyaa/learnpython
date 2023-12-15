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
def cube(num1, num2, num3):
    return float(num1) * float(num2) * float(num3)
num1 = input("enter a number: ")
num2 = input("enter a number: ")
num3 = input("enter a number: ")

value = cube(num1, num2, num3)
print(str(value))

