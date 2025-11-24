'''Python program to count frequency of characters in a given
file. '''

# File to analyze
file_name = "example.txt"

# Dictionary to store character frequency
char_frequency = {}

# Open the file in read mode
with open(file_name, "r") as file:
    content = file.read()  # Read the whole file

    # Count each character
    for char in content:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

# Display the frequency of characters
print("Character frequency in the file:")
for char, freq in char_frequency.items():
    if char == "\n":
        print("\\n :", freq)  # Represent newlines visibly
    elif char == " ":
        print("' ' :", freq)   # Represent spaces visibly
    else:
        print(f"{char} : {freq}")
