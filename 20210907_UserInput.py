
# Python program showing a use of input()
val = input("Enter your value: ")
print(val)

# input
num1 = int(input())
num2 = int(input())
float1 = float(input())
float2 = float(input())
string = str(input())
# printing the sum in integer
print(num1 + num2)
# printing the sum in float
print(float1 + float2)
# output
print(string)


# Python program showing how to multiple input using split
# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print(x)
print(y)
print("First number is {} and second number is {}".format(x, y))

# taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  # adding the element
print(lst)

# try block to handle the exception
try:
    my_list = []
    while True:
        my_list.append(int(input()))
# if the input is not-integer, just print the list
except:
    print(my_list)


# number of elements
n = int(input("Enter number of elements : "))
# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", a)

# List of lists as input
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = [input(), int(input())]
    lst.append(ele)
print(lst)

# Using List Comprehension and Typecasting
# For list of integers
lst1 = []
# For list of strings/chars
lst2 = []
lst1 = [int(item) for item in input("Enter the list items : ").split()]
lst2 = [item for item in input("Enter the list items : ").split()]
print(lst1)
print(lst2)
