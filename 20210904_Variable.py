# Python program processing global variable
count = 5
def some_method():
	global count
	count = count + 1
	print(count)
some_method()

# Python program showing a scope of object
def some_func():
	print("Inside some_func")
	def some_inner_func():
		var = 10
		print("Inside inner function, value of var:",var)
	some_inner_func()
	#print("Try printing var from outer function: ",var)  ##runtime error var not defined
some_func()

# Python 3 code to demonstrate variable assignment
# upon condition using One liner if-else
# initialising variable using Conditional Operator
# a = 20 > 10 ? 1 : 0 is not possible in Python
# Instead there is one liner if-else
a = 1 if 20 > 10 else 0
# printing value of a
print ("The value of a is: " + str(a))

# Python 3 code to demonstrate variable assignment
# upon condition using Direct Initialisation Method
# initialising variable directly
a = 5
# printing value of a
print ("The value of a is: " + str(a))

# Python3 code to demonstrate variable assignment
# upon condition using Conditional Operator
# Initialising variables using Conditional Operator
a = 1 if 20 > 10 else 0
# Printing value of a
print("The value of a is: " , str(a))

print("Eugene")
print("Koshy")
#print without new line
print("Eugene","", end = "")
print("Koshy")

a = [1, 2, 3, 4]
for i in range(4):
	print(a[i])
#print without new line
for i in range(4):
	print(a[i], end=" ")
#print end of line
print('\r')
# print without new line
print(*a)