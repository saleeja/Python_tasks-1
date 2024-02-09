"""6 Python program to print all even/odd numbers in the range given by user"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Even numbers in the range:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')

print("\nOdd numbers in the range:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=' ')
