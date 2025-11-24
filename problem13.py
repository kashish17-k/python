'''Ask the user for a number and determine whether the
number is prime or not. (For those who have forgotten, a
prime number is a number that has no divisors.).'''

# Ask the user for a number
num = int(input("Enter a number: "))

# A number less than 2 is not prime
if num < 2:
    print(f"{num} is not a prime number.")
else:
    # Check for divisors from 2 to sqrt(num)
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
