# *args – Hinglish me: Function me multiple positional arguments lene ke liye use hota hai, bina exact number define kiye.

# **kwargs – Hinglish me: Function me multiple keyword arguments lene ke liye use hota hai, bina exact key-value pairs define kiye.


def print_kwargs(**kwargs):
    print(kwargs)  # it's a dictionary
    print(kwargs.items())
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="John", age=30, city="New York")
print_kwargs(name="Johny", age=31)
