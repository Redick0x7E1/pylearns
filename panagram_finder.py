# create a function that returns true if it is a panagram
# a panagram is a sentance with every letter of the alphabet at least once.
def is_panagram(s):
    s = s.replace(' ', '')
    s = s.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in s:
            return False
        else:
            return True

a = "The fox jumps over the lazy dog "
print(is_panagram(a))
