"""2.Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
    print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
    if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.
"""

# available_balance
balance = 1000 

# Minimum balance requirement
min_balance = 500

# Ask user for the amount to withdraw
withdrawal_amount = int(input("Enter the amount to withdraw : "))

# Check if withdrawal is possible

if withdrawal_amount > balance:
    print("Insufficient balance")
else:
    new_balance = balance - withdrawal_amount
    if new_balance < min_balance:
        print("Withdrawal successful, but your new balance is", new_balance,
              "which is below the minimum balance of", min_balance, ".")
        print("Please keep your account balance above Rs.500 to avoid unwanted charges.")
    else:
        print("Withdrawal successful. Your new balance is:", new_balance)

