numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0
for each in numbers:
    if each > 0:
        count += 1

print(count)
    
count_method2 = sum(1 for num in numbers if num > 0)
print(count_method2)