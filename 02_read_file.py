with open("student.txt", "w") as doc:
    doc.write("Name: Karan\nCourse: BCA\n")
with open("student.txt", "r") as doc:
    print(doc.read())
