'''Write a Python program that defines the following functions:

find_max(numbers)
find_min(numbers)
find_average(numbers)
The program should:

Accept a list of 10 integers from the user.
Call all three functions.
Display the maximum value, minimum value, and average of the list.
'''
## Function to find the maximum value in a list
def find_max(numbers):
    return max(numbers)

## Function to find the minimum value in a list
def find_min(numbers):
    return min(numbers)

## Function to find the average value of a list
def find_average(numbers):
    return sum(numbers) / len(numbers)

#main program to accept 10 integers from the user and display max, min, and average
numbers_list = []
for i in range(10):
    number = int(input(f"Enter integer {i+1}: "))
    numbers_list.append(number)

# Call the functions and display the results
max_value = find_max(numbers_list)
min_value = find_min(numbers_list)
average_value = find_average(numbers_list)
print("\nResults:")
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")
print(f"Average Value: {average_value}")



