#Instead of writing this massive Python code
#we can also code this in a different way
#Python code to demonstrate working of iskeyword()
# importing "keyword" for keyword operations
import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "while", "tanisha", "break", "sky", "elif", "assert", "pulkit", "lambda", "else", "sakshar"]
for i in range(len(keys)):
	# checking which are keywords
	if keyword.iskeyword(keys[i]):
		print(keys[i] + " is python keyword")
	else:
		print(keys[i] + " is not a python keyword")
print ("The list of keywords is : ")
print (keyword.kwlist)

# True False None
print(False == 0)
print(True == 1)
print(True + True + True)
print(True + False + False)
print(None == 0)
print(None == [])

print("--------------")
# showing logical operation
print(False and True)
print(True and False)
print(True and None)
print(False and None)
print(False or True)
print(True or False)
print(True or None)
print(False or None)
print(3 and 10)
print(3 and None and 10)
print(3 and 0)
print(3 and None and 0)
print(3 or 10)
print(None or 0 or 10)
print(0 or 0)
print("--------------")
print(not True)
print(not False)
print(not None)
print("--------------")


# using "in" to check
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
#else:
#	print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
	print(i, end=" ")
print("\r")


# using is to check object identity
print(3 is 3)
print('a' is 'a')
print('3' is 3)
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')
# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})

# Using for loop
for i in range(10):
    print(i, end=" ")
    # break the loop as soon it sees 6
    if i == 6:
        break
print()

# loop from 1 to 10
i = 0
while i < 10:
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
    i += 1

    # Python program to illustrate if-elif-else ladder
    # !/usr/bin/python

    i = 20
    if (i == 10):
        print("i is 10")
    elif (i == 20):
        print("i is 20")
    else:
        print("i is not present")


# def keyword
def fun():
    print("Inside Function")
fun()


# Return keyword
def fun():
    S = 0
    for i in range(10):
        S += i
    return S
print(fun())

# Yield Keyword
def fun():
    S = 0
    for i in range(10):
        S += i
        yield S
for i in fun():
    print(i)


# Python3 program to
# demonstrate instantiating
# a class
class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
# Driver code
# Object instantiation
Rodger = Dog()
# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')

# as keyword alias for module
import math as gfg
print(gfg.factorial(5))

n = 10
for i in range(n):
# pass can be used as placeholder
# when code is to added later
    pass

# Lambda keyword
g = lambda x: x*x*x
print(g(7))

# import keyword
import math
print(math.factorial(10))
# from keyword
from math import factorial
print(factorial(10))

# initializing number
a = 4
b = 0
# No exception Exception raised in try block
try:
	k = a//b # raises divide by zero exception.
	print(k)
# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
# assert Keyword
# using assert to check for 0
print ("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print (a / b)

my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)
# delete both the variables
del my_variable1
del my_variable2
# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# global variable
a = 15
b = 10
# function to perform addition
def add():
    c = a + b
    print(c)
# calling a function
add()

# nonlocal keyword
def fun():
    var1 = 10
    def gun():
        # tell python explicitly that it
        # has to access var1 initialized
        # in fun on line 2
        # using the keyword nonlocal
        nonlocal var1
        var1 = var1 + 10
        print(var1)
    gun()
fun()

#