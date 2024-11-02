# Write a program that asks the user for a year and then determines if it is a leap year or not. A leap year is a year that is divisible by 4. But is not a leap year if is divisible by 100 unless it is divisible by 400. 

#variables
year = int(input("Enter a year: "))
is_leap_year = False

#conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
