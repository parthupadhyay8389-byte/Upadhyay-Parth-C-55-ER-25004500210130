with open("source.txt", "w") as doc:
    doc.write("This is a basic Python exercise.")
with open("source.txt", "r") as doc:
    content = doc.read()
with open("copy.txt", "w") as doc:
    doc.write(content)
print("File copied successfully.")
