n = 7
for i in range(1, 11):
    if i == 5:
        continue
    print(f"{n} * {i} == {n * i}")

# print([f"{n} * {i} == {n * i}" for i in range(11)])