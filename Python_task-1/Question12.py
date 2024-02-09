"""12.Print first 10 fibonacci numbers using 'for' and 'while' loops"""

# The Fibonacci series is the sequence of numbers in which the next number is the sum of the two previous numbers.
# using while loop
number = 10  #we have to print first 10 numbers

num1=0  #first number is 0
num2=1  #second number is 1
i=0

while i<number:
    print(num1)
    nterm=num1+num2
    num1=num2
    num2=nterm
    i+=1


# using for loop
number = 10

num1=0
num2=1

for i in range(10):
    print(num1)
    nterm=num1+num2
    num1=num2
    num2=nterm
    

