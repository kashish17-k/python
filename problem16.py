'''Implement a function that takes as input three variables, and
returns the largest of the three. Do this without using the
Python max() function!'''

def largest_of_three(a, b, c):
    largest = a  # Assume a is the largest initially

    if b > largest:
        largest = b  # Update if b is larger
    if c > largest:
        largest = c  # Update if c is larger

    return largest

# Example usage:
print(largest_of_three(5, 9, 3))  # Output: 9
print(largest_of_three(12, 7, 12))  # Output: 12
