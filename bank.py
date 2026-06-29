'''bank transaction summary'''

balance = 0.0
deposists = 0.0
withdrawals = 0.0

print("Enter your bank transactions. Type '0' when finished.")
print("Use positive numbers for deposits and negative numbers for withdrawals." \
"")

while True:
    amount = float(input("Enter transaction amount: "))
    if amount == 0:
        break
    balance += amount
    if amount > 0:
        deposists += amount
    else:
        withdrawals += abs(amount)

    print(f"Current balance: {balance:.2f}")

print(f"Total deposits: {deposists:.2f}")
print(f"Total withdrawals: {withdrawals:.2f}")
print(f"Final balance: {balance:.2f}")