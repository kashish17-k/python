'''Write a program (function!) that takes a list and returns a
new list that contains all the elements of the first list minus
all the duplicates.'''

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(original_list)

print("Original list:", original_list)
print("List without duplicates:", result)