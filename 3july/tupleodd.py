#creating a blank list
numbers=[]
for i in range(15):
    number=int(input("Enter a number: "))
    numbers.append(number)

t1=tuple(numbers)
for i in range(15):
    print("the numbers in the tuple are:")
    print(i,end=" ")

print("the odd numbers in the tupple are:")
for i in t1:
    if i%2!=0:
        print(i,end=" ")
