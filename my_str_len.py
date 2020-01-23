# Calculate the length of any given string.
# what is base case

# what is recursive case. Each iteration should have a smaller case.

def findLen(string):
    if string == '':
        return 0
    return 1 + findLen(string[1:])

print(findLen("Hello"))