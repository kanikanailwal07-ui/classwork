'''Create a class named Student to store and display a student's details. '''
# Define the following instance variables:  student_id , name , course , marks
class Student:
    def __init__(self):
        self.student_id = ""
        self.name = ""
        self.course = ""
        self.marks = 0

#taking Input in Variables:
    def accept_data(self):
        self.student_id = input("Enter Student ID : ")
        self.name = input("Enter Name : ")
        self.course = input("Enter Course : ")
        self.marks = int(input("Enter Marks : "))

#Defining A Function To Display Data
    def display_data(self):
        print("\n------ Student Details ------")
        print("Student ID :", self.student_id)
        print("Name :", self.name)
        print("Course :", self.course)
        print("Marks :", self.marks)

#Defing A Fucntion to check Result
    def check_result(self):
        if self.marks >= 35:
            print("Result : Pass")
        else:
            print("Result : Fail")


# Creating object and calling methods
s1 = Student()
s1.accept_data()
s1.display_data()
s1.check_result()
