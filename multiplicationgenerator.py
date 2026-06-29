'''Multiplication Table Generator'''
#input number from user 
number = int(input("Enter a number: "))
#display multiplication table
print(f"Multiplication Table of {number}:")
for i in range(1, 21):
    print(f"{number} x {i} = {number * i}")