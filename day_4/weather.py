# You want to go to a park but only if the weather is appropriate and is weekend. You have to check the weather conditions and the day of the week. Write a program that will help you decide whether to go to the park. The program should print out whether you should go to the park or not based on the weather conditions and the day of the week.

# variables
weather = input("What is the weather like today? (sunny, rainy, snowy, windy, cloudy): ")
day = input("What day of the week is today? (monday, tuesday, wednesday, thursday, friday, saturday, sunday): ")

if weather == "sunny" and (day == "saturday" or day == "sunday"):
    print("Go to the park.")
else:
    print("Do not go to the park. Let's stay home and watch a movie.")

