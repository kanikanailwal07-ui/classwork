'''login system with maximum 3 attempts'''
#input username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")
#check if username and password are correct
if username == "admin" and password =="python123":
    print("Login successful")
else:
    print("invalid ceredentials.")
    #allow user to try again for maximum 3 attempts
    for i in range(2):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password =="python123":
            print("Login successful")
            break
        else:
            print("invalid credentials.")
    else:
        print("Account Locked.")
