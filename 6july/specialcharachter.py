#input of sentence
sentence = input("Enter any sentence: ")
#initalize special character count as
special_count = 0
for char in sentence:
    if char.isalnum():
        pass
    elif char.isspace():
        pass
    else:
        special_count += 1  

print("number of special characters=", special_count)
