'''program for factor of a number'''
#input number from user
n=int(input("Enter a number:"))
#display of number
if n == 0:
    print("The number is zero, which has infinite factors.")
elif n >0:
 #positive number
    print("The factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
else:
    #negative number
    num = -n
    print("The factors of", n, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(-i," , ",i," , ",end="")