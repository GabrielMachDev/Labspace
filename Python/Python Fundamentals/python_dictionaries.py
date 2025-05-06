dic_products = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# take an element
print(dic_products["iphone"])

# edit an element
dic_products["iphone"] = dic_products["iphone"] * 1.3
print(dic_products)

# quantity of items
print(len(dic_products))

# remove a item
# dic_products.pop("airpod")
# print(dic_products)

# add a item
dic_products["apple watch"] = 2500
print(dic_products)

# check a item exist
if "iphone" in dic_products:
    print("Product exists")
else:
    print("No exists")

# check if a value exists in the dictionary values
# if 9000 in dic_products.values():
#     print("Exists")
# else:
#     print("No exists")
    
product_name = input("Product name: ")
product_price = input("Product price: ")

# register the new product(if the product don't exist)
# if th product exists it will edit the product
product_name = product_name.lower()
product_price = float(product_price)

dic_products[product_name] = product_price
print(dic_products)


# update the price of all products and more 10%

for product in dic_products:
    new_preco = dic_products[product] * 1.1
    dic_products[product] = new_preco

print(dic_products)