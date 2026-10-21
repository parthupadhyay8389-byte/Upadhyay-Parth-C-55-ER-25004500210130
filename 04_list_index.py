values = [12, 24, 36, 48, 60]
try:
    position = int(input("Enter an index from 0 to 4: "))
    print("Value:", values[position])
except IndexError:
    print("Index is out of range.")
except ValueError:
    print("Please enter an integer.")
