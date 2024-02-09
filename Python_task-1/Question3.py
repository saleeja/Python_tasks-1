""" 3. Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same """

# Ask user input 

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Compare the numbers
if number1 == number2 == number3:
    print("All three numbers are equal.")
elif number1 >= number2 and number1 >= number3:
    print("The greatest number is:",number1)
elif number2 >= number1 and number2 >= number3:
    print("The greatest number is:",number2)
else:
    print("The greatest number is:",number3)

