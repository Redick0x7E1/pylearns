"""Given a string of words, reverse all the words.
without using builtins

start = "This is the best"
finish = "Best the is this"
"""

def reverse(s):

    length = len(s) # get length of string given
    i = 0 # index tracker to determine where in the list we are
    spaces = [' ']
    words = []

    while i < length: # go throguh all chars in string until the end.
        # spaces are chars in python
        if s[i] not in spaces:
            word_start = i # first letter of work is this index

            while i < length and s[i] not in spaces:
                i += 1 # move through word
                words. append(s[word_start:i])  # move through the word.
                                                # Break when word ends/ space found.
                                                #i now equals index of last char that is not a space

        i += 1 # within if loop. If it is a space, incriment i by one to skip it without entering inner loop.

    return " ".join(reversed(s)) # reverse s

print(reverse("This is the best"))