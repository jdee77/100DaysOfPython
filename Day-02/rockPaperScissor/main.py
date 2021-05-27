import logo
import symbols
import random

print(logo.logo)

exit_game = False

def print_symbol(choice):
    if choice == 1:
        print("ROCK")
        print(symbols.rock)
    elif choice == 2:
        print("PAPER")
        print(symbols.paper)
    elif choice == 3:
        print("SCISSOR")
        print(symbols.scissor)
    else:
        print("Invalid choice.")

def print_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Match Drawn !!")
    elif user_choice == 1 and computer_choice == 3:
        print("Congratulations ! you won.")
    elif user_choice == 2 and computer_choice == 1:
        print("Congratulations ! you won.")
    elif user_choice == 3 and computer_choice == 2:
        print("Congratulations ! you won.")
    else:
        print("Oops !! Better lick next time.")

    
while not exit_game:
    print("Enter your choice")
    user_choice = int(input("type '1' for ROCK, type '2' for PAPER, type '3' for SCISSOR :"))
    computer_choice = random.randint(1, 3)

    print("Your choice :")
    print_symbol(user_choice)
    print("computer choice :")
    print_symbol(computer_choice)

    print_result(user_choice, computer_choice)

    exit = input("Do you want to play more (y/n) :").lower()
    if exit != 'y':
        exit_game = True

