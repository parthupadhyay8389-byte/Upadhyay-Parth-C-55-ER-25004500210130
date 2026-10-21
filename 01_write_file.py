content = input("Enter a message: ")
with open("message.txt", "w") as doc:
    doc.write(content)
print("Message saved.")
