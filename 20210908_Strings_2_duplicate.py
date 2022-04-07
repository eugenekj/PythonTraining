'''
Duplicate characters
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
'''

def dup_check(str1):
    lst = []
    dup_lst = []
    res = []
    for i in (str1):
        lst.append(i)
    index = 0
    for i in lst:
        for j in range(index+1,len(lst)):
            if i == lst[j]:
                dup_lst.append(i)
        index += 1
    print(dup_lst)
    [res.append(x) for x in dup_lst if x not in res]
    res.sort()
    print(res)

if __name__ == "__main__":
    str1 = "GeeksforGeeks"
    dup_check(str1)

## using counter()
from collections import Counter
def find_dup(str1):
    WC = Counter(str1)
    res = []
    j = -1
    for i in WC.values():
        j = j + 1
        if ( i > 1 ):
            res.append(WC.values()[i])
    print(res)
if __name__ == "__main__":
    str1 = "geeksforgeeks"
    find_dup(str1)