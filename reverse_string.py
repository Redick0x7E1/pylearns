"""Given a string of words, reverse all the words.

start = "This is the best"
finish = "Best the is this"
"""

def reverse_string(sentence):
    myArray = sentence.split(' ')

    """
    # My Terrible code....
    newArray = []

    for i in myArray:
        newArray = newArray.append(myArray[startHere])
        startHere = startHere - 1
"""
    print(' '.join(myArray[::-1]))


print(reverse_string("This is the best"))