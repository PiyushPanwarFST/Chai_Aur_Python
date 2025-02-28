str = "teeter"
count = 0

for ch in str:
    print(ch)
    if str.count(ch) == 1:
        print(f"this is my ans: {ch}")
        break
    

