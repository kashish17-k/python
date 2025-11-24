'''A spell checker can be a helpful tool for people who struggle
to spell words correctly. In this exercise, you will write a
program that reads a file and displays all of the words in it
that are misspelled. Misspelled words will be identified by
checking each word in the file against a list of known words.
Any words in the user’s file that do not appear in the list of
known words will be reported as spelling mistakes. The user
will provide the name of the file to check for spelling mistakes
as a command line parameter. Your program should display
an appropriate error message if the command line parameter
is missing. An error message should also be displayed if your
program is unable to open the user’s file. Words followed by
a comma, period or other punctuation mark are not reported
as spelling mistakes. Ignore the capitalization of the words
when checking their spelling.'''

import sys
import string

def load_dictionary(dict_file="dictionary.txt"):
    """Load known words from a dictionary file into a set."""
    try:
        with open(dict_file, "r") as f:
            # Read words and convert to lowercase
            words = {line.strip().lower() for line in f}
        return words
    except FileNotFoundError:
        print(f"Dictionary file '{dict_file}' not found.")
        sys.exit(1)

def spell_check(file_to_check, dictionary):
    """Check the file for spelling mistakes."""
    try:
        with open(file_to_check, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Cannot open file '{file_to_check}'.")
        sys.exit(1)

    # Remove punctuation from each word
    translator = str.maketrans('', '', string.punctuation)
    words = content.split()
    misspelled = set()

    for word in words:
        clean_word = word.translate(translator).lower()  # Remove punctuation and lowercase
        if clean_word and clean_word not in dictionary:
            misspelled.add(clean_word)

    if misspelled:
        print("Misspelled words found:")
        for word in sorted(misspelled):
            print(word)
    else:
        print("No spelling mistakes found!")

if __name__ == "__main__":
    # Check for command line argument
    if len(sys.argv) < 2:
        print("Usage: python spell_checker.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    dictionary = load_dictionary()  # Load known words
    spell_check(filename, dictionary)