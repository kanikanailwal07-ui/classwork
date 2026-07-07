# Define a function to search for a student by roll number
def search_student(student_dict, roll_no):
    return student_dict.get(roll_no, "Student Not Found")

# Main program
#accept a dictionary of students with roll numbers as keys and names as values
student_dict = {}
for i in range(5):
    roll_no = input(f"Enter roll number for student {i+1}: ")
    name = input(f"Enter name for student {i+1}: ")
    student_dict[roll_no] = name

#accept a roll number to search for 
search_roll_no = input("Enter roll number to search for: ")

#call the search_student function and display the result
result = search_student(student_dict, search_roll_no)
print(f"Search Result: {result}")