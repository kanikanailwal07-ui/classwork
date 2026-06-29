'''electricity bill analysis'''
#input units consumed from  n houses
n = int(input("Enter the number of houses: "))
total_units = 0
highest_units = 0
lowest_units = float('inf')
for i in range(n):
    units = float(input(f"Enter the units consumed by house {i+1}: "))
    total_units += units
    if units > highest_units:
        highest_units = units
    if units < lowest_units:
        lowest_units = units

print(f"Total units consumed by all houses: {total_units}")
print(f"Average units consumed per house: {total_units / n}")
print(f"Highest units consumed by a single house: {highest_units}")
print(f"Lowest units consumed by a single house: {lowest_units}")