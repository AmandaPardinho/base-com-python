# The IMC program calculates the Body Mass Index (IMC) of a person. To calculate the IMC, you need to divide the weight (in kg) by the square of the height (in meters). The program should print the IMC and the classification of the person according to the table below:
# IMC Classification 
# < 18.5 Underweight 
# 18.5 - 24.9 Normal weight 
# 25 - 29.9 Overweight 
# 30 - 34.9 Obesity class 1 
# 35 - 39.9 Obesity class 2 
# >= 40 Obesity class 3
# The program should ask the user for the weight and height and then print the IMC and the classification. Use the following code as a starting point:

# variables
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
imc = weight / (height ** 2)

# conditions
if imc <= 18.5:
    print(f"IMC: {imc:.2f} - Underweight")
elif imc > 18.5 and imc < 25:
    print(f"IMC: {imc:.2f} - Normal weight")
elif imc >= 25 and imc < 30:
    print(f"IMC: {imc:.2f} - Overweight")
elif imc >= 30 and imc < 35:
    print(f"IMC: {imc:.2f} - Obesity class 1")
elif imc >= 35 and imc < 40:
    print(f"IMC: {imc:.2f} - Obesity class 2")
else:
    print(f"IMC: {imc:.2f} - Obesity class 3")
