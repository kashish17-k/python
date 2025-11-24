'''Write a Python program to calculate the sum of three given
numbers, if the values are equal then return thrice of their
sum.'''

def calculate_sum(a, b, c):
    total = a + b + c
    if a == b == c:
        return 3 * total
    return total

# Get user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = calculate_sum(a, b, c)
print("Result:", result)
