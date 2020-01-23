# create a fucntion that takes a string and sorts the characters. But it will leave special char '$' in the same index.
# possibly use list.insert()

def string_sort_special(s):
    s = s.replace(" ", "")
    s = s.lower()
    s = list(s)
    spec_loc = []
    i = 0
    while i < len(s):
        if s[i] == '$':
                spec_loc.append(i)
        i += 1
    s.sort()
    i = 0
    while i < len(spec_loc): # this will only work with special chars since sorting a list with chars and special chars will append special chars first.
        # add an isalpha() check?
        s.remove(s[0])
        i += 1
    loc_count = 0
    while loc_count < len(spec_loc):
        s.insert(spec_loc[loc_count], '$')
        loc_count += 1
    return ''.join(s)

# test case
a = 'Hel$lo Wor$ld' # index of $ is 3 and 10 before removing spaces
b = 'HELLO $ my frie$nd ho$w $are $you'

print(string_sort_special(a))
print(string_sort_special(b))