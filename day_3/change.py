# You go to a bakery and buy some items. 
#   bread: 3.50
#   milk: 4.20
#   coffee: 2.80
# You pay with a 20 dollar bill. The cashier gives you change. Write a program that calculates the change you should get back. 

# Variables
bread = 3.50
milk = 4.20
coffee = 2.80
payment_bill = 20.00

# Calculate total
total = bread + milk + coffee
print(f'Total: $ {total:.2f}')

# Calculate change
change = payment_bill - total
print(f'Change: $ {change:.2f}')
