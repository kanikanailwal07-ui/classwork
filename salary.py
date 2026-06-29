'''employee salary statistics'''
#input salary from user
n = int(input("Enter the number of employees: "))


highest_salary = 0
lowest_salary = float('inf')
total_salary = 0
count_high = 0

for _ in range(n):
    salary = int(input("Enter employee salary: "))
    total_salary += salary
    if salary > highest_salary:
        highest_salary = salary
    if salary < lowest_salary:
        lowest_salary = salary
    if salary > 50000:
        count_high += 1

average_salary = total_salary / n if n > 0 else 0

print(f"Highest salary: {highest_salary}")
print(f"Lowest salary: {lowest_salary}")
print(f"Average salary: {average_salary:.2f}")
print(f"Number of employees with salary above 50,000: {count_high}")