# A cab company charges a basic fare of $4.00, plus R$0.25 per kilometer driven. Create a program that calculates the total value of the ride based on the distance traveled.

# variables
fare = 4
extra_km = 0.25
km = int(input("How many kilometers will be traveled? "))
travel = fare + (km * extra_km)

print(f"The travel will coast $ {travel:.2f}")

