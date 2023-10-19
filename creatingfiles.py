# creating new file .txt file in python

with open("newfile.txt", "w") as file:
    file.write("new file is created")
    print(file)

with open('newfile.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
