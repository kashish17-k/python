'''Write a Python program to calculate number of days
between two dates. Sample dates: (2014, 7, 2), (2014, 7,
11) Expected output : 9 days'''

from datetime import date

# Input dates
year1, month1, day1 = map(int, input("Enter first date (YYYY MM DD): ").split())
year2, month2, day2 = map(int, input("Enter second date (YYYY MM DD): ").split())

# Create date objects
d1 = date(year1, month1, day1)
d2 = date(year2, month2, day2)

# Calculate difference
delta = d2 - d1

print("Number of days between dates:", delta.days)
