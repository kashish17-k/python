'''Python program to perform read and write operations on a
file. '''

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("We are writing some text into this file.\n")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Appending new text to the file
with open("example.txt", "a") as file:
    file.write("Adding a new line to the file.\n")

# Reading the updated content
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("Updated file content:")
    print(updated_content)