"""11.Find the sum of all odd numbers between the rane given by user using while loop"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize the sum variable
odd_sum = 0

# Calculate the sum of odd numbers using a while loop
num = start
while num <= end:
    if num % 2 != 0:
        odd_sum += num
    num += 1

# Print the result
print("The sum of even numbers is:", odd_sum)
