'''Write a program that prompts the user to enter his name.
The program then greets the person with his name. But if the
person’s name is ‘Rahul’ and exception is thrown and he is
asked to quit the program.'''

class QuitProgramException(Exception):
    pass

try:
    # Prompt the user for their name
    name = input("Enter your name: ")

    # Check if the name is 'Rahul'
    if name == "Rahul":
        raise QuitProgramException("You are not allowed to proceed. Please quit the program.")

    # Greet the user
    print(f"Hello, {name}! Welcome!")

except QuitProgramException as e:
    print(e)