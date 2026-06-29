'''number guessing game'''
#input number from user
number = int(input("Enter a number :"))
#secret number
secret_number = 37
#while loop for number guessing
while number != secret_number:
    if number < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    number = int(input("Enter a number :"))
print("Correct.")