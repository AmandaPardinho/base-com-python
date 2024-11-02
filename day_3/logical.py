# Logical Operators

# variables
age = 20
has_license = True
student = False


# and
can_rent_car = (age >= 21) and has_license
print("Can I rent a car? ", can_rent_car)

# or
elderly = age >= 60 
half_price = elderly or student
print("Do I get a discount? ", half_price)

# not
is_raining = False
not_raining = not is_raining
print("Is it not raining? ", not_raining)
print("Is it raining? ", is_raining)