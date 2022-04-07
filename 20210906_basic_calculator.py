def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

print("Please select operation -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
opt = int(input("Select operations form 1, 2, 3, 4 :"))
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

if opt == 1:
    print(num1, " + ", num2, " = ", add(num1, num2))
elif opt == 2:
    print(num1, " - ", num2, " = ", subtract(num1, num2))
elif opt == 3:
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif opt == 4:
    print(num1, " / ", num2, " = ", divide(num1, num2))
else :
    print("Invalid Input")