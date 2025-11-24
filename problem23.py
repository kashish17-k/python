'''Write a program that accepts date of birth along with the
other personal details of a person. Throw an exception if an
invalid date is entered.'''

from datetime import datetime

# Function to get personal details
def get_personal_details():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

        # Try to convert the input into a valid date
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        
        # Display the details
        print("\nPersonal Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Date of Birth: {dob.strftime('%Y-%m-%d')}")

    except ValueError:
        print("Invalid date format! Please enter the date in YYYY-MM-DD format.")

# Call the function
get_personal_details()