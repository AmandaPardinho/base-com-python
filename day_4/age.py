# Write a program to classify a person's age based on the following conditions:
#   -Child: 0-12 years
#   -Teenager: 13-17 years
#   -Adult: 18-59 years
#   -Senior: 60+ years

#variables
age = int(input("Enter your age: "))

#conditions
if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 17:
    print("You are a teenager")
elif age >= 18 and age <= 59:
    print("You are an adult")
elif age >= 60:
    print("You are a senior")
else:
    print("Invalid age")
    