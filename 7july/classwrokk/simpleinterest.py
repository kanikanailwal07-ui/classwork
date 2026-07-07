#function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
#------------------------------------------------
principal = float(input("Enter the principal amount: (in Rs.)"))
rate = float(input("Enter the rate of interest: (in %)"))
time = int(input("Enter the time in years: (in years)"))
print("The simple interest is: Rs.", calculate_simple_interest(principal, rate, time))