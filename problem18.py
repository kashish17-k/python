'''Python program to copy the contents of a file to another file. '''

# Copy contents from source file to destination file
source_file = "source.txt"
destination_file = "destination.txt"

# Open the source file in read mode and destination file in write mode
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line)

print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")