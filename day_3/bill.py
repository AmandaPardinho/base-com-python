# Three friends went to a restaurant. They wanted to split the bill equally. The bill was $ 150.00. The waiter had a tip of $22.50 which was added to the bill and the total bill was $172.50. The friends want to split the bill equally. Write a program that calculates the amount each friend has to pay.

# Variables
total_bill = 172.50
friends = 3

# Calculate the amount each friend has to pay
amount_each = total_bill / friends
print(f"Each friend has to pay: ${amount_each:.2f}")

# modulus
mod = total_bill % friends
if mod == 0:
    print(f"The division is exact.")
else:
    print(f"The division is not exact. The remainder is: {mod:.2f}")
