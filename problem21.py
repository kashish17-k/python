'''Python program to compute the number of characters, words
and lines in a file'''

file_name = "example.txt"

# Initialize counters
num_lines = 0
num_words = 0
num_chars = 0

# Open the file in read mode
with open(file_name, "r") as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)          # Count all characters including spaces and newline
        num_words += len(line.split())  # Split line into words and count them

# Display results
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")