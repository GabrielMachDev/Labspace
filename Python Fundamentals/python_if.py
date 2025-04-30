sales = 1500
goal = 1300

# > greater than
# < less than
# >= greater or equal
# <= less or equal
# == equal
# != different

if sales >= goal:
    print("Seller gets bonus")
    print("Hit the sales taget")
    bonus = 0.1 * sales
    print("Seller bonus:", bonus)
else:
    print("Seller don't get bonus")
    print("Dont hit the targets")

# second case
sales = 2100
enterprise_sales = 22000
enterprise_goal = 20000
first_goal = 1300 # to win 10%
second_goal = 2000 # to win 13%

if sales >= 2000 and enterprise_sales >= enterprise_goal:
    bonus = 0.13 * sales
elif sales >= 1300 and enterprise_sales >= enterprise_goal:
    bonus = 0.1 * sales
else:
    bonus = 0

print("Bonus:", bonus)


product_list = ["airpod", "ipad", "iphone", "macbook"]
product_sought = input("Search a product: ")
product_sought = product_sought.lower()

if product_sought in product_list:
    print("Product in stock")
else:
    print("We don't have this product")