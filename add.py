def add_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Sum =", a + b)
    except ValueError:
        print("Please enter valid numbers only.")

add_numbers()
