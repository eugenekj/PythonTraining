'''
Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
Output : Yes
Explanation : In the string GEEGEEKSKS, we can first
              delete the substring GEEKS from position 4.
              The new string now becomes GEEKS. We can
              again delete sub-string GEEKS from position 1.
              Now the string becomes empty.

Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
Output : No
Explanation : In the string it is not possible to make the
              string empty in any possible manner.
'''
def serach_substr(str1,substr1):
    if len(str1) == 0 and len(substr1) == 0:
        return True
    if len(str1) == 0:
        return True
    while (len(str1) != 0) :
        index = str1.find(substr1)
        if index == (-1):
            return False
        str1 = str1[0:index] + str1[index+len(substr1):]
    return True

if __name__ == "__main__":
    str1 = 'GEEGEEKSSGEK'
    substr1 = 'GEEKS'
    print(serach_substr(str1, substr1))
