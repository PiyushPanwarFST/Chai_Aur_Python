# in this file we will use *args means we can multiple arguments

def add(*args):
    total = 0
    print(*args) 
    print(args) # it's a tuple
    for arg in args:
        total += arg
    print("Hii: ", total)
    return sum(args)
print(add(1, 2, 3))  # Output: 6