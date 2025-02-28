items = ["apples", "banana", "orange", "apple", "mango", "grapes"]

for i in items:
    if items.count(i) == 2:
        print(f"{i} it is a duplicate word in a list")
        break
    print("there is no duplicate word in list")
    break
