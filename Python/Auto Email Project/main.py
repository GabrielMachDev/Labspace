import pandas as pd
import win32com.client as win32

# import database
sale_tables = pd.read_excel('Sales.xlsx')

# visualize database
pd.set_option('display.max_columns', None)
print(sale_tables)

# billing by store
billing = sale_tables[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(billing)

# quantity of products sold by store
quantity = sale_tables[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantity)

print('-' * 50)
# average ticket by product in each store
average_ticket = (billing['Valor Final'] / quantity['Quantidade']).to_frame()
average_ticket = average_ticket.rename(columns={0: 'Ticket Médio'})
print(average_ticket)

# send an email with the report
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'exampler@gmail.com'
mail.Subject = 'Sales by Store Report'
mail.HTMLBody = f'''
<p>Dear,</p>

<p>Here is the Sales Report for each Store.</p>

<p>Billing:</p>
{billing.to_html(formatters={'Final Value': '${:,.2f}'.format})}

<p>Quantity Sold:</p>
{quantity.to_html()}

<p>Average Ticket of Products in each Store:</p>
{average_ticket.to_html(formatters={'Average Ticket': '${:,.2f}'.format})}

<p>Any questions I'm at your disposal.</p>

<p>Att.,</p>
<p>Manager</p>
'''

mail.Send()

print('Mail sent')
