#input user name
name = input ("Enter your name:")
#initialize a list
first=[]
for i in name :
    if i>='A' and i<='Z' or i>='a' and i<='z':
        first.append(i)
    else:
        break
print("first name is :",first)

