# Create Dictionary
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Add a new product
inventory["Printer"] = 12

# Update the stock of an existing product
inventory["Laptop"] = 20

# Remove a product from inventory
del inventory["Mouse"]

# Display products having stock less than 20
print("Products having stock less than 20:")
for product in inventory:
    if inventory[product] < 20:
        print(product, ":", inventory[product])

# Display total number of items available
total = 0
for product in inventory:
    total = total + inventory[product]

print("Total items in inventory =", total)
