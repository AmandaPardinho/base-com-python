# Write a program that simulates a loan application process. The program should ask the user for the following details:
# - Monthly income
# - Number of parcels
# - Amount of loan
# The loan will be approved if the parcels are less than or equal to 30% of the monthly income. Otherwise, the loan will be rejected.
# The program should display the result to the user.

# variables
income = float(input("Enter your monthly income: "))
loan = float(input("Enter the amount of loan: "))
parcels = int(input("Enter the number of parcels: "))
monthly_parcels = loan / parcels

if monthly_parcels <= (0.3 * income):
    print("Congratulations! Your loan has been approved.")
else:
    print("Sorry! Your loan has been rejected.")