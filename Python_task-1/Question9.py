"""9    Find the factorial of a number taken as input using while loop"""

# Accept input from the user
number = int(input("Enter a number to find its factorial: "))

# Initialize the factorial variable
factorial = 1

# Calculate factorial using a while loop
i = 1
while i <= number:
    factorial *= i
    i += 1

# Print the result
print("The factorial of",number,"is",factorial)
