'''Write a Python program which accepts a sequence of
comma-separated numbers from user and generate a list
and a tuple with those numbers.'''

values = input("Enter comma-separated numbers: ")

# Generate list and tuple
number_list = values.split(",")
number_tuple = tuple(number_list)

print("List:", number_list)
print("Tuple:", number_tuple)