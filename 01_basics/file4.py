color_of_banana = input("Enter the color of the banana: ").strip().lower()

if color_of_banana == "green":
    print("Unripe")
elif color_of_banana == "yellow":
    print("Ripe")
else:
    print("Overripe")
