billing = 1200
cost = 700
profit = billing - cost
profit_margin = profit / billing
print(f"Enterprise billing: {billing}, Cost: {cost}, Profit: {profit}")

client_email = "clientemail@gmail.com"

# uppercase
client_email = client_email.upper()
print(client_email)
# lowercase
client_email = client_email.lower()
print(client_email)

# "@"
print(client_email.find("@")) # -1 cant find

# text size
print(len(client_email))

# catch a character
print(client_email[4])

print(client_email[-4])

# get a piece of text
print(client_email[4:])

# change a piece of text
new_email = client_email.replace("gmail.com", "hotmail.com")
print(new_email)

name = "client"
# work with names
print(name.capitalize())
print(name.title())

# get the email server
at_position = client_email.find("@") + 1
server = client_email[at_position:]
print(server)

# get the first name
space_position = name.find(" ")
first_name = name[:space_position]

# get the lastname
lastname = name[space_position+1:]
print(first_name)
print(lastname)

# special case - text numeric formatting
profit_margin = round(profit_margin, 2)
print(f"Enterprise Billing: R${billing:.2f}, Cost: R${cost:.2f}, Profit: R${profit:.2f}, Margin: {profit_margin:.0%}")