'''Create a ditonary where employee id is the key and name,department,salary is the value.'''


#Creating a dictionary to store employee details
employee_details = {}

#taking no of employees from user
n = int(input("Enter the number of employees: "))

#Adding employee details to the dictionary
for i in range(n):
    emp_id = input("Enter employee id: ")
    name = input("Enter employee name: ")
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    employee_details[emp_id] = {'name': name, 'department': department, 'salary': salary}

#Displaying all employee details
print("The employee details are: ")
for emp_id, details in employee_details.items():
    print("Employee ID: ", emp_id)
    print("Name: ", details['name'])
    print("Department: ", details['department'])
    print("Salary: ", details['salary'])
    print()

#Searching for an employee using employee id
search_id = input("Enter the employee id to search: ")
if search_id in employee_details:
    print("Employee details for id ", search_id, " are: ")
    print("Name: ", employee_details[search_id]['name'])
    print("Department: ", employee_details[search_id]['department'])
    print("Salary: ", employee_details[search_id]['salary'])
else:
    print("Employee with id ", search_id, " not found.")

#Increasing the salary of all employees by 10%
for emp_id in employee_details:
    employee_details[emp_id]['salary'] *= 1.10
    print("Employee ID: ", emp_id)
    print("Name: ", employee_details[emp_id]['name'])
    print("Department: ", employee_details[emp_id]['department'])
    print("Updated Salary: ", employee_details[emp_id]['salary'])
    print()

#Displaying employees belonging to a specific department entered by the user
department_name = input("Enter the department name to display employees: ")
print(f"Employees belonging to department '{department_name}':")
for emp_id, details in employee_details.items():
    if details['department'] == department_name:
        print("Employee ID: ", emp_id)
        print("Name: ", details['name'])
        print("Salary: ", details['salary'])
        print()
