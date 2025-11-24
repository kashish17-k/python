'''Generate a random number between 1 and 9 (including 1
and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very
first exercise)'''

import random

# Generate a random number between 1 and 9
number = random.randint(1, 9)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 9: "))

# Check the guess
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Exactly right! You guessed it.")
    