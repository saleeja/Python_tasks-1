"""4. Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers"""

user_input = input("Enter any number to test whether it is odd or even:")

# checking if it is digit.
if user_input.isdigit():
    number = int(user_input)  # Convert the input to an integer

    if number % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Invalid input. Please enter a valid integer.")




    
