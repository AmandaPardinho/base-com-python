# When you drive a car, you have to obey the traffic lights and take decisions based on the color of the traffic light. Write a program that will help you decide what to do based on the color of the traffic light. The program should print out the action you should take based on the color of the traffic light.

# variables
light = input("What color is the traffic light? (red, yellow, green): ")

if light == "red":
    print("Stop the car.")
elif light == "yellow":
    print("Slow down.")
elif light == "green":
    print("Go.")
else:
    print("Unknown traffic light. Be cautious.")