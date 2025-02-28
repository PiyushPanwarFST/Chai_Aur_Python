input_val = int(input(f"Enter the number: "))

is_prime = True

if input_val > 1:
    for i in range(2, input_val):
        if (input_val%i) == 0:
            is_prime = False
            break

print(is_prime)