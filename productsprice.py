#creating a list  of 10 products and their prices
products = [
    ("Product A", 1200.00),
    ("Product B", 1500.49),
    ("Product C", 2000.00),
    ("Product D", 2500.99),
    ("Product E", 3000.49),
    ("Product F", 3500.00),
    ("Product G", 4000.99),
    ("Product H", 4500.49),
    ("Product I", 5000.00),
    ("Product J", 5500.99)
]
#display the products in tuple format
tuple1 = tuple(products)
print("The products and their prices in tuple format are:")
for product in tuple1:
    print(product)

#products with highest and lowest price
highest = max(tuple1)
print("The product with the highest price is:", highest)
lowest = min(tuple1)    
print("The product with the lowest price is:", lowest)

#count the number of products with price greater than 4000 along with their names
count = 0
for product in tuple1:
    if product[1] > 4000:
        count += 1
        print("Product with price greater than 4000:", product[0], "Price:", product[1])
print("The number of products with price greater than 4000 is:", count) 
