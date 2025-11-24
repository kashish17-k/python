'''Write a function that takes an ordered list of numbers (a list
where the elements are in order from smallest to largest)
and another number. The function decides whether or not
the given number is inside the list and returns (then prints)
an appropriate boolean'''

def is_in_list(ordered_list, number):
    # Since the list is ordered, we could use 'in' directly
    return number in ordered_list

# Example usage
my_list = [1, 3, 5, 7, 9, 11]
num = int(input("Enter a number to check: "))

result = is_in_list(my_list, num)
print(result)  # True if number is in the list, False otherwise
