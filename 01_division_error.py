try:
    num_a = int(input("Enter first number: "))
    num_b = int(input("Enter second number: "))
    print("Result:", num_a / num_b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter integers only.")
