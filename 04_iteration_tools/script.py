import time
from itertools import count, cycle, repeat

print("Count:")
for i in count(10):
    print(i)
    if i == 20:
        break
print("\nCycle:")
items = ["apples", "banana", "orange", "apple", "mango", "grapes"]