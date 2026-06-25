'''area of the rectangle '''
#input length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
#validation of dimensions
if length < 0 or width < 0:
    exit("Dimensions cannot be negative. Please enter valid dimensions.")
#display of dimensions
print("Length of the rectangle is:", length)
print("Width of the rectangle is:", width)
#calculation of area
area = length * width
#display of area
print("Area of the rectangle is:", area)
#calculation of perimeter
perimeter = 2 * (length + width)
#display of perimeter
print("Perimeter of the rectangle is:", perimeter)