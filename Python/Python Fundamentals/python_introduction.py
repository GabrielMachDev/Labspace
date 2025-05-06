billing = 1200 # type int -> integer number
cost = 750.0 # type float -> number with decimal place 

new_sales = 100
billing = billing + new_sales

tax = billing * 0.1
profit = billing - cost - tax

profit_margin = profit / billing

print("The revenue was ", billing)
print("The cost was ", cost)
print("The profit was ", profit)
print("The profit margin was", round(profit_margin, 3))

meassage = "The billing was..." 
email = "email@gmail.com" # type string -> text

made_profit = True # variable type boolean

# Mod -> % rest of the division
contract_time = 170
time_years = 170 / 12
print("Time in years ", int(time_years))
time_months = 170 % 12
print("Time in months ", time_months)
