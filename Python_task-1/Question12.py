"""12.Print first 10 fibonacci numbers using 'for' and 'while' loops"""


# using while loop
number = 10

num1=0
num2=1
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
    

