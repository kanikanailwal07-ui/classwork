'''Write a function check_password(password) that checks whether a password is strong.

A password is considered Strong if:

It contains at least 8 characters.
It contains at least one uppercase letter.
It contains at least one lowercase letter.
It contains at least one digit.
The function should return:

"Strong Password" or
"Weak Password"
The main program should accept a password from the user and display the result.'''

#define the function to check password strength
def check_password(password):
    # Check for length
    if len(password) < 8:
        return "Weak Password"
    
    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak Password"
    
    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return "Weak Password"
    
    # Check for digit
    if not any(char.isdigit() for char in password):
        return "Weak Password"
    
    return "Strong Password"

#main program to accept a password from the user and display the result
user_password = input("Enter a password to check its strength: ")
result = check_password(user_password)
print(result)
