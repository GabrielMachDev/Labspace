sales_list = [1000, 500, 800, 1500, 2000, 2300]

goal = 1200
bonus_percent = 0.1


for sale in sales_list:
    if sale >= goal:
        bonus = bonus_percent * sale
    else:
        bonus = 0
    print(bonus)


# for sale in sales_list:
#     print(sale)
#     print("Next item")

# out of the for
