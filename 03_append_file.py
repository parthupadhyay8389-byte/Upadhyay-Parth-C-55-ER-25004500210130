with open("names.txt", "w") as doc:
    doc.write("Dev\nMira\n")
person_name = input("Enter another name: ")
with open("names.txt", "a") as doc:
    doc.write(person_name + "\n")
with open("names.txt", "r") as doc:
    print(doc.read())
