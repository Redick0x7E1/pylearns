# Given any string. Count number of consonants. Use recursion.

def count_consonants_resurse(input_string):
    vowels = ['a','e', 'i', 'o', 'u', ' ']
    #spaces = ' ' spaces accounted for in vowels list
    if input_string == '':
        return 0

    if input_string[0] in vowels:
        return count_consonants_resurse(input_string[1:])

    return 1 + count_consonants_resurse(input_string[1:])


a = 'abc de'
b = 'SSSaaa aaa aaa S'
print(count_consonants_resurse(a))
print(count_consonants_resurse(b))
