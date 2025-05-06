# inputs
# email = input("Write your email: ")
# name = input("Your first name: ")

# print(name, email)

# print(f"{name}, check your email: {email} that we sent a confirmation email")

# billing = float(input("Write billing: "))

# tax = billing* 0.1
# print(tax)

# lists
sales = [100, 50, 14, 20, 30, 700]

# sum of elements
total_sales = sum(sales)
print(total_sales)

# list size
sales_quantity = len(sales)
print(sales_quantity)

# max and min
print(max(sales))
print(min(sales))

# pick up position
print(sales[5])

product_list = ["iphone", "airpod", "ipad", "macbook"]

# product_sought = input("Search by name of the product: ")
# product_sought = product_sought.lower()

# print(product_sought in product_list)

# add item
product_list.append("apple watch")
print(product_list)

# remove item
product_list.remove("apple watch")
print(product_list)

product_list.pop(0)
print(product_list)

# edit item 
prices = [1000, 1500, 3500]
prices[0] = prices[0] * 1.5
print(prices)

# count equal items
product_list = ["iphone", "airpod", "ipad", "macbook", "iphone", "ipad", "iphone"]

print(product_list.count("apple watch"))

# sort list
sales.sort()
print(sales)