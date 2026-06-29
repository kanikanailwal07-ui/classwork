'''factorial of a number'''
#input number from user
n=int(input("Enter a number:"))
#---------------------------------
if n == 0:
    print("The factorial of 0 is 1.")
elif n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is:", factorial)