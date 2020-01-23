#find palindromic permutation
import re
i = 0
def find_palindrome(s):
    arr1 = s.lower().split(' ')
    if find_duplicates(arr1) == True:
        return "Is palindrome"
    else:
        return  "is not palindrome"
    # Determine if there are two of each character

def find_duplicates(array):
    mod_array = array
    if (len(array) % 2) == 0:
        return True
    else:
        mod_array = array[::len(array)-1]
    mid = (len(mod_array) -1)
    print(mid)
    s1 = array[:mid]
    s2 = array[mid:]

    if s1 == s2:
        return True

p = "carrace"
a = "notpalin"

print(find_palindrome(p))
