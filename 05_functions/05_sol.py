def get_numbers():
    return [1, 2, 3]
print(get_numbers())  # Output: [1, 2, 3]



def get_numbers():
    for i in range(1, 4):
        yield i

for num in get_numbers():
    print(num)


