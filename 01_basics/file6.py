order_size = input("What size would you like to prefer? (large/medium/small): ").strip().lower()
extra_shot = input("Would you like an extra shot of espresso? (yes/no): ").strip().lower() == "yes"

prices = {"large": 80, "medium": 60, "small": 40}
shot_price = 20

total_bill = prices.get(order_size) + (shot_price if extra_shot else 0)

print(f"Total bill: {total_bill} rupees")
