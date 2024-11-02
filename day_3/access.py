# To enter a restrict area, the user need to enter the correct password and cannot be blocked on system.
# The password is "abcd1234". The user insert the password and the system will check if the password is correct. Then, the user will be able to enter the restricted area if he/she is not blocked.
# Write a program that receives the password and verifies the blocked status of the user and returns if the user can enter the restricted area or not.

# Variables
password = "abcd1234"
is_blocked = False

if password == "abcd1234" and not is_blocked:
    print("You can't enter the restricted area.")
elif password == "abcd1234" and is_blocked:
    print("You can't enter the restricted area.")
elif password != "abcd1234" :
    print("You can't enter the restricted area.")