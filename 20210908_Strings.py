# https://www.geeksforgeeks.org/python-strings/

# with single Quotes
str1 = 'Buddy'
# with double Quotes
str2 = "Buddy's car"
# with triple Quotes
str3 = '''Buddy's car "Hyundai i10"'''
# with triple Quotes allows multiple lines
str4 = '''multi
line
string'''
print(str1)
print(str2)
print(str3)
print(str4)

# Indexing
str1 = "EUGENE KOSHY"
print(str1[0])
print(str1[-12])

# slicing
print(str1[0:3])
print(str1[7:15])
print(str1[-12:-6])

# Escape
str1 = 'Buddy\'s car "Hyundai i10"'
print(str1)
str2 = "Buddy's car \"Hyundai i10\""
print(str2)
str3 = "E:\\Python\\Study"
print(str3)

# ignore escape sequence use r or R
str3 = "E:\\Python\\Study"
print(str3)
str4 = r"E:\\Python\\Study"
print(str4)

# Logical Operations
str1 = ''
str2 = 'geeks'
# repr is used to print the string along with the quotes
# Returns str1
print(repr(str1 and str2))
# Returns str1
print(repr(str2 and str1))
# Returns str2
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))

str1 = 'for'
# Returns str2
print(repr(str1 and str2))
# Returns str1
print(repr(str2 and str1))
# Returns str1
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))	

str1 ='geeks'
# Returns False
print(repr(not str1))
str1 = ''
# Returns True
print(repr(not str1))		

# Python program to demonstrate the use of formatting using %
# Initialize variable as a string
variable = '15'
string = "Variable as string = %s" %(variable)
print (string )
# Printing as raw data
print ("Variable as raw data = %r" %(variable))
# Convert the variable to integer And perform check other formatting options
variable = int(variable) # Without this the below statement will give error.
string = "Variable as integer = %d" %(variable)
print (string)
print ("Variable as float = %f" %(variable))
# printing as any string or char after a mark
# here i use mayank as a string
print ("Variable as printing with special char = %cmayank" %(variable))
print ("Variable as hexadecimal = %x" %(variable))
print ("Variable as octal = %o" %(variable))

# Template
# A Python program to demonstrate the working of the string template
from string import Template
# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]
# We are creating a basic structure to print the name and marks of the students.
t = Template('Hi $name, you have got $marks marks')
for i in Student:
	print (t.substitute(name = i[0], marks = i[1]))
print(t.safe_substitute(name='Eugene'))

# The $$ can be used to escape $ and treat as part of the string.
template = Template('$$ is the symbol for $name')
string = template.substitute(name='Dollar')
print(string)

# The ${Identifier}
template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)

# split()
line = "Geek1 \nGeek2 \nGeek3"
print(line)
print(line.split())
print(line.split(' ', 1))

# docstring
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    return None
print("Using __doc__:")
print(my_function.__doc__)