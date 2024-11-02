# Write a program that asks the user for two numbers and operator and then calculates the result.

#variables
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

#conditions
if operator == "+":
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} is {sum:.2f}")
elif operator == "-":
    difference = num1 - num2
    print(f"Difference of {num1} and {num2} is {difference:.2f}")
elif operator == "*":
    product = num1 * num2
    print(f"Product of {num1} and {num2} is {product:.2f}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        exit
    quotient = num1 / num2
    print(f"Quotient of {num1} and {num2} is {quotient:.2f}")
else:
    print("Invalid operator")