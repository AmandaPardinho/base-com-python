# A shop offers a discount if client buys more than 10 items or if total price is more than $ 100.00.
# These are the total of items and the total price of them:
# Ammount of items: 8 
# Total price: $ 120.00
#  Write a program that verifies if the client will receive a discount or not.

# Variables
items = 8
total_price = 120.00

# Conditions
if items > 10 or total_price > 100.00:
    print("The client will receive a discount.")
else:
    print("The client will not receive a discount.")