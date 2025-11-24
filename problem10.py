'''Ask the user for a string and print out whether this string is
a palindrome or not. (A palindrome is a string that reads the
same forwards and backwards.)'''

text = input("Enter a string: ")

# Remove spaces and make lowercase for accurate checking
cleaned_text = text.replace(" ", "").lower()

# Check if the string is the same forwards and backwards
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")