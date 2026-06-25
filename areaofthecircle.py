'''area of the circle '''
#input radius
radius = float(input("Enter the radius of the circle: "))
#validation of radius
if radius < 0:
    exit("Radius cannot be negative. Please enter a valid radius.")
#display of radius
print("Radius of the circle is:", radius)
#calculation of area
area = 3.14 * radius * radius
#display of area
print("Area of the circle is:", area)
