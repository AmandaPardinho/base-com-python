# Write a program that simulates an ATM machine. The program should ask the user to enter the value of the amount they want to withdraw. The program should then calculate the number of each denomination of notes to be given to the user. The denominations should be 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1. The program should print the number of each denomination of notes to be given to the user. The program should also print the total number of notes to be given to the user.

# variables
amount = 0
notes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

while True:
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount < 1:
            print("Invalid amount entered.")
        else:
            break
    except ValueError:
        print("Invalid amount entered.")

for note in notes:
    if amount >= note:
        num_notes = amount // note
        amount = amount % note
        total_notes += num_notes
        print(f"{num_notes} notes of $ {note:.2f}")
print(f"Total number of notes: {total_notes}")
            
    
    