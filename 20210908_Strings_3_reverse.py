#reverse

# 1. using loop
def reverse1(str1):
    rstr = ""
    for i in str1:
        rstr = i + rstr
    return rstr

# 2. recursion
def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse2(s[1:]) + s[0]

# 3. extended slice method
def reverse3(str1):
    str1 = str1[::-1]
    return str1

# 4. using reversed
def reverse4(str1):
    str1 = "".join(reversed(str1))
    return str1

if __name__ == "__main__":
    str = "buddy4ever"
    print(reverse1(str))
    print(reverse2(str))
    print(reverse3(str))
    print(reverse4(str))

# 5. using stack
# Function to create an empty stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack

# Function to determine the size of the stack
def size(stack):
    return len(stack)

# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return true

# Function to add an item to stack . It increases size by 1
def push(stack, item):
    stack.append(item)

# Function to remove an item from stack.  It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()

# A stack based function to reverse a string
def reverse(string):
    n = len(string)
    # Create a empty stack
    stack = createStack()
    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])
    # Making the string empty since all characters are saved in stack
    string = ""
    # Pop all characters of string and put them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string

s = "Buddy$ever"
print(reverse(s))
