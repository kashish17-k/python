'''Ask the user for a number. Depending on whether the
number is even or odd, print out an appropriate message to
the user. Hint: how does an even / odd number react
differently when divided by 2?'''

num = int(input("Enter a number: "))

# Check if even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")