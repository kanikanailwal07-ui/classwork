'''count prime number in a given range'''
#input range from user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
#loop to count prime numbers in the range
count = 0
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            count += 1
print(f"Number of prime numbers in the range [{start}, {end}]: {count}")