# A shop offers a discount based on the total amount of the purchase. If total amount is more than 1000, the discount is 10%. If total amount is between $500.00 and $999.99, the discount is 5%. If the amount is less than $500.00, there is no discount. Write a program that will help you calculate the discount based on the total amount of the purchase. The program should print out the discount you will get based on the total amount of the purchase.

# variables
total_amount = float(input("What is the total amount of the purchase? "))

if total_amount > 1000:
    discount = total_amount * 0.10
    print(f"You get a 10% discount. The discount is: $ {discount:.2f}")
elif total_amount >= 500 and total_amount < 1000:
    discount = total_amount * 0.05
    print(f"You get a 5% discount. The discount is: $ {discount:.2f}")
else:
    print("There is no discount.")

final_amount = total_amount - discount
print(f"The final amount is: $ {final_amount:.2f}")
