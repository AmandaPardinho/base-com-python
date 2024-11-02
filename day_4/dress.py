# You have to decide what to wear today. You have a list of clothes and a list of weather conditions. Write a program that will help you decide what to wear today. The program should print out the clothes that are appropriate for the weather conditions. 

# variables
weather = input("What is the weather like today? (sunny, rainy, snowy, windy, cloudy): ")

if weather == "sunny":
    print("Wear a t-shirt, shorts, and sandals.")
elif weather == "rainy":
    print("Wear a raincoat, boots, and an umbrella.")
elif weather == "snowy":
    print("Wear a winter coat, snow boots, and a hat.")
elif weather == "windy":
    print("Wear a windbreaker, sneakers, and a hat.")
elif weather == "cloudy":
    print("Wear a light jacket, jeans, and sneakers.")
else:
    print("Check the weather condition.")