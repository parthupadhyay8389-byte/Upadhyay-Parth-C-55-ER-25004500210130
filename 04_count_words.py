with open("sentence.txt", "w") as doc:
    doc.write("Learning Python is quite simple")
with open("sentence.txt", "r") as doc:
    content = doc.read()
word_list = content.split()
print("Number of words:", len(word_list))
