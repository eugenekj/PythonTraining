# code begins
print("Study starts here")
print("Hello World")
# code ends

# Python program to declare variables
myNumber = 3
print(myNumber)
myNumber2 = 4.5
print(myNumber2)
myNumber = 'hello world'
print(myNumber)

# Python program to illustrate a list

# creates a empty list
nums = []
# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")
print(nums)
# list creation with data
nums1 = [20, 20.5, "Hello World"]
print(nums1)

# Python program to illustrate
# getting input from user
name = input("Enter your name: ")
print("hello", name)

# Python3 program to get input from user
""" accepting integer from the user
    the return type of input() function is string ,
    so we need to convert the input to integer"""
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = num1 * num2
print("Product is: ", num3)

# Python program to illustrate
# selection statement
num1 = 37
if (num1 > 12):
    print("Num1 is good")
elif (num1 > 35):
    print("Num1 is not gooooo....")
else:
    print("Num1 is great")
# Output -> Num1 is good

# Python program to illustrate
# functions
def hello():
    print("hello")
    print("hello again")
# calling function
hello()


# Python program to illustrate
# function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result
def Main():
    print("Started")
    # calling the getInteger function and
    # storing its returned value in the output variable
    output = getInteger()
    print(output)
# now we are required to tell Python
# for 'Main' function existence
if __name__=="__main__":
    Main()

# Python program to illustrate
# a simple for loop
for step in range(5):
    print(step)

# Python program to illustrate
# math module
import math


def Main():
    num = -85
    # fabs is used to get the absolute
    # value of a decimal
    num = math.fabs(num)
    print(num)
if __name__ == "__main__":
    Main()
