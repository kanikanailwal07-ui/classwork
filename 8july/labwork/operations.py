#import the twofigures module
from twofigures import*

#function to display the main menu
def display_main_menu():
    print("Select a figure:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Square")
    print("5. Exit")

#function to display the opeartion menu
def display_operation_menu():
    print("Select an operation:")
    print("1. Area")
    print("2. Perimeter")

#main program loop
while True:
    display_main_menu()
    choice = input("Enter your choice (1-5):")

    if choice == '5':
        print("Exiting the application.")
        break

    display_operation_menu()
    operation_choice = input("Enter your choice (1-2):")

    if choice == '1':  #Rectangle
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        if operation_choice == '1':
            area = calculate_area_of_rectangle(length, width)
            print("Area of rectangle:", area)
        elif operation_choice == '2':
            perimeter = calculate_perimeter_of_rectangle(length, width)
            print("Perimeter of rectangle:", perimeter)
        else:
            print("Invalid operation choice.")

    elif choice == '2':  #Triangle
        side1 = float(input("Enter the length of side 1 of the triangle:"))
        side2 = float(input("Enter the length of side 2 of the triangle:"))
        side3 = float(input("Enter the length of side 3 of the triangle:"))
        if operation_choice == '1':
            base = float(input("Enter the base of the triangle:"))
            height = float(input("Enter the height of the triangle:"))
            area = calculate_area_of_triangle(base, height)
            print("Area of triangle:", area)
        elif operation_choice == '2':
            perimeter = calculate_perimeter_of_triangle(side1, side2, side3)
            print("Perimeter of triangle:", perimeter)
        else:
            print("Invalid operation choice.")

    elif choice == '3':  #Circle
        radius = float(input("Enter the radius of the circle:"))
        if operation_choice == '1':
            area = calculate_area_of_circle(radius)
            print("Area of circle:", area)
        elif operation_choice == '2':
            circumference = calculate_circumference_of_circle(radius)
            print("Circumference of circle:", circumference)
        else:
            print("Invalid operation choice.")
    
    elif choice == '4': #Square
        side = float (input("Enter the side length of the square:"))
        if operation_choice == '1':
            result = calculate_area_of_square(side)
            print("The area of square is:{result}")
        elif operation_choice == '2':
            result = calculate_perimeter_of_square(side)
            print("The perimeter of square is:{result}")
    else:
        print("Invaild Choice. Please Try Again.")