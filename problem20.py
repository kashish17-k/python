'''Python program to print each line of a file in reverse order'''

file_name = "example.txt"

# Open the file in read mode
with open(file_name, "r") as file:
    lines = file.readlines()  # Read all lines into a list

# Print each line in reverse order
for line in lines:
    print(line.rstrip()[::-1])  # Remove trailing newline and reverse the line