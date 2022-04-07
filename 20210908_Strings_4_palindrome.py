# palindrome
'''
Input : malayalam
Output : Yes

Input : geeks
Output : No
'''

# 1. reverse method
def reverse(str):
    str = "".join(reversed(str))
    return str
def check_palindrome(str):
    rstr = reverse(str)
    if rstr == str:
        return True
    else:
        return False

# 2. Iterative method
def isPalindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False;
    return True


if __name__ == "__main__":
    s = "malayalam"
    print(s)
    print(check_palindrome(s))
    print(isPalindrome(s))
    s = "buddy"
    print(s)
    print(check_palindrome(s))
    print(isPalindrome(s))


# function which return reverse of a string
def isPalindrome(s):
	return s == s[::-1]
# Driver code
s = "malayalam"
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")


# function to check string is
# palindrome or not
def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
# main function
s = "malayalam"
ans = isPalindrome(s)
if (ans):
    print("Yes")
else:
    print("No")

# Python program to check
# if a string is palindrome
# or not
x = "malayalam"
w = ""
for i in x:
	w = i + w
if (x == w):
	print("Yes")
else:
	print("No")


# Python program to check
# if a string is palindrome
# or not using flag
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
	    j = j - 1
	    flag = 1
	    break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")


# Recursive function to check if a
# string is palindrome
def isPalindrome(s):
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
    # if length is less than 2
    if l < 2:
        return True
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
    else:
        return False
# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

