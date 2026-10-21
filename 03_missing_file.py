file_path = input("Enter a file name: ")
try:
    with open(file_path, "r") as doc:
        print(doc.read())
except FileNotFoundError:
    print("File does not exist.")
