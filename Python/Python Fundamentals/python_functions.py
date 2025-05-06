price_list = [1500, 1000, 800, 3000]

# tax
# aliquot1 - IR = 0.2, if the price of the product is up to 2000, above that the rate is 0.3
# aliquot2 - ISS = 0.15
# aliquot3 - CSLL = 0.05

def calc_total_tax(price):
    if price <= 2000:
        tax_ir = 0.2 * price
    else:
        tax_ir = 0.3 * price
    tax_iss = 0.15 * price
    tax_csll = 0.05 * price
    total_tax = tax_ir + tax_iss + tax_csll
    return total_tax

for price in price_list:
    total_tax = calc_total_tax(price)
    print(f"Total tax on the product of ${price}: ${total_tax}")

new_products_list = [3000, 5000, 6000, 7000]

for price in new_products_list:
    total_tax = calc_total_tax(price)
    print(f"Total tax on the product of ${price}: ${total_tax}")