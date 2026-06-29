'''password strength chechker'''
#input password from user
password = input("Enter your password: ")
#validaition of password strength
#while loop for password validation
while len(password) < 8:
    print("Password is too short")
    password = input("Enter your password: ")
print("Password Accepted")