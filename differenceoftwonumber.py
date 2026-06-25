'''calculate the difference of two numbers'''
#input numbers
n1=float(input("Enter the number 1:"))
n2=float(input("Enter the number 2:"))
#validation of numbers
if n1<0 or n2<0:
    exit("Numbers cannot be negative. Please enter valid numbers.")
#display of numbers
print("Number 1 is:", n1)  
print("Number 2 is:", n2)
#calculation of difference
difference=n1-n2
#display of difference
print("Difference of the two numbers is:", difference)
