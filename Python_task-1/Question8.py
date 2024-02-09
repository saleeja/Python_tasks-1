"""8. Find the factorial of a number taken as input using for loop"""


number = int(input("Enter input number : "))

# Initialize the factorial variable
factorial = 1

# Calculate factorial
for i in range(1, number + 1):
    factorial = factorial * i
    
# Print the result
print("The factorial of",number,"is",factorial)