'''Write a Python program to test whether a passed letter is a
vowel or not'''

letter = input("Enter a single letter: ").lower()

# Check if it's a vowel
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")
