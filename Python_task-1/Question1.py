"""
Write python programs , which accept two inputs and perform the following arithmetic operations
    i)	 Addition (+)
    ii)	 Subtraction (-)
    iii) Multiplication (*)
    iv)	 Division (/)
    v)	 Modulus (%)
    vi)	 Exponentiation (**)
    vii) Floor Division (//)  
"""


# Get user input 
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number:"))

# Addition
result_add = number1 + number2
print("Addition :",result_add)

# Subtraction
result_sub = number1 - number2
print("Subtraction :",result_sub)


# Multiplication
result_mul = number1 * number2
print("Multiplication :", result_mul)

# Division
result_div = number1 / number2
print("Division :", result_div)

# Modulus
result_mod = number1 % number2
print("Modulus :", result_mod)

# Exponentiation
result_exp = number1 ** number2
print("Exponentiation :", result_exp)

# Floor Division
result_floor_div = number1 // number2
print("Floor Division :", result_floor_div)
