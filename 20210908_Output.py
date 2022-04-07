
print("Hello \n World")
print()
print("")
print('Test')
print('Hello World',end = '**')
print()
print('G','F','E')
print('G','F','E', sep = '*')

# code for disabling the softspace feature
print('G', 'F', 'G', sep='')
print('G','F', sep='', end='')
print('G')
# for formatting a date
print('09', '12', '2016', sep='-')
print('09', '12', '2016', sep='-', end = '\n')
# another example
print('pratik', 'geeksforgeeks', sep='@')
print('pratik','agarwal', sep='', end='@')
print('geeksforgeeks')


"""
# flush
import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush=True)
        time.sleep(1)
    else:
        print('Start')

import io
# declare a dummy file
dummy_file = io.StringIO()
# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)
# get the value from dummy file
dummy_file.getvalue()
"""

# formatting
print('%d' %(123.5678))
print('%f' %(123.5678))
print('%.2f' %(123.5678))
print("total students: %3d, portal: %5.2f" %(120,05.333))

print('{} and {}'.format('Buddy1','Buddy2'))
print('{0} and {1}'.format('Buddy1','Buddy2'))
print('{1} and {0}'.format('Buddy1','Buddy2'))
print("total students: {0:3d}, portal: {1:5.2f}".format(120,05.333))
# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009))
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009))
print("{:*^20s}".format("Geeks"))

cstr = "Buddy"
print(cstr.center(10,'#'))
print(cstr.ljust(10,'#'))
print(cstr.rjust(10,'#'))
print(cstr.center(3,'#'))

# f string
name = 'Eugene'
age = 32
print(f"Hello, My name is {name} and I'm {age} years old.")

import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

val1="Buddy1"
val2="Buddy2"
print(f"{val1} and {val2}")