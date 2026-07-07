#define the function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 75:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'Fail'
    
#main program to accept marks of 5 students and display their grades
#input marks for 5 students
marks_list = []
for i in range(5):
    marks = float(input(f"Enter marks for student {i+1} (0-100): "))
    marks_list.append(marks)

#display marks and corresponding grades
print("\nStudent Marks and Grades:")
for i in range(5):
    grade = calculate_grade(marks_list[i])
    print(f"Student {i+1}: Marks = {marks_list[i]}, Grade = {grade}")