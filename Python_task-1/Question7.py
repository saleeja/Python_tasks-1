"""7 Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)"""

# Ask input from the user
number = int(input("Enter the number for multiplication table: "))
end_limit = int(input("Enter the end limit for the multiplication table: "))

# Print the multiplication table

for i in range(1, end_limit + 1):
    result = number * i
    print(number,'*' , i ,"=" ,result)

