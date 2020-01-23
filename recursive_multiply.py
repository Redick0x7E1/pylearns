# given two integers, provide product of them

def multiple_recurse(x,y):
    if y == 0:
        return 0
    return x + multiple_recurse(x,y-1)

a = 5
b = 3

print(multiple_recurse(a,b))