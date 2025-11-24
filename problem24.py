'''Write a Regular Expression to represent all 10 digit mobile
numbers. Rules: 1. Every number should contains exactly 10
digits. 2. The first digit should be 7 or 8 or 9 Write a Python
Program to check whether the given number is valid mobile
number or not?'''

import re

# Regular expression for valid mobile numbers
# ^[789] -> first digit must be 7, 8, or 9
# \d{9}$ -> followed by exactly 9 digits (total 10 digits)
mobile_pattern = r"^[789]\d{9}$"

# Input mobile number from user
mobile_number = input("Enter your mobile number: ")

# Check if the input matches the pattern
if re.fullmatch(mobile_pattern, mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
