"""10 Find the sum of all even numbers between the range given by user"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize the sum variable
even_sum = 0

# Calculate the sum of even numbers
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num

# Print the result
print("The sum of even numbers is:", even_sum)
