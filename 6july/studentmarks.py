#create a dictionary to store student marks of 5 students
student_marks = {}
#adding 5 students and their marks to the dictionary
for i in range(5):
    name = input("Enter the name of student {}: ")
    marks = int(input("Enter the marks of {}: ".format(name)))
    student_marks[name] = marks


#displaying all student marks
print("The student with their marks are:")
for name, marks in student_marks.items():
    print(name, ":", marks)

#adding a new student and their marks to the dictionary
new_student = input("Enter the name of the new student: ")
new_marks = int(input("Enter the marks of new student: "))
student_marks[new_student] = new_marks

#updating the marks of an existing student
update_student = input("Enter the name of the student whose marks you want to update: ")    
if update_student in student_marks:
    new_marks = int(input("Enter the new marks for {}: ".format(update_student)))
    student_marks[update_student] = new_marks
else:
    print("Student not found.")

#deleting a student from the dictionary
delete_student = input("Enter the name of the student you want to delete: ")
if delete_student in student_marks:
    del student_marks[delete_student]
else:
    print("Student not found.")

#displaying all student with highest marks
highest_marks = max(student_marks.values())
print("The student(s) with the highest marks are:")
for name, marks in student_marks.items():
    if marks == highest_marks:
        print(name, ":", marks)
