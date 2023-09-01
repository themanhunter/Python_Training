import random

possibility_list = ["Rock","Paper","Scissors"]

print("Welcome to Rock, Paper, Scissors!")

choice_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if choice_index == 0:
    print("You chose rock!")
elif choice_index == 1:
    print("You chose paper!")
elif choice_index == 2:
    print("You chose scissors!")
else:
    print("Thats an invalid number")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("The computer chose rock!")
elif computer_choice == 1:
    print("The computer chose paper!")
else:
    print("The computer chose scissors!")


if computer_choice == 0 and choice_index == 0:
    print("Stale mate, you both lose!")
elif computer_choice == 0 and choice_index == 1:
    print("You win!")
elif computer_choice == 0 and choice_index == 2:
    print("The computer won!")
elif computer_choice == 1 and choice_index == 0:
    print("The computer won!")
elif computer_choice == 1 and choice_index == 1:
    print("Stale mate, you both lose")
elif computer_choice == 1 and choice_index == 2:
    print("You win!")
elif computer_choice == 2 and choice_index == 0:
    print("You win!")
elif computer_choice == 2 and choice_index == 1:
    print("The computer wins")
elif computer_choice == 2 and choice_index == 2:
    print("Stale mate, you both lose!")
else:
    print("The computer wins cause you tried to be funny")

