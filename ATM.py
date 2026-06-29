'''ATM pin verification program'''
#input pin
pin = input("Enter your PIN: ")
#correct pin
correct_pin = "4589"
#while loop for pin verification
while pin != correct_pin:
    print("Incorrect PIN.")
    pin = input("Enter your PIN: ")

print("Access granted")