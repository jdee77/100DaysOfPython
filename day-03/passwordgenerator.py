import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator !")
print("_______________________________")
print("Choose your preferences :")
choice = int(input('Enter 1 fro "EASY" (6 letters), enter 2 for "HARD" (8 letters)'))

no_letters = 0
no_numbers = 0
no_symbols = 0
choice_validity = True

if choice == 1:
    no_letters = random.randint(1,3)
    no_numbers = random.randint(0,2)
    no_symbols = 6 - no_letters - no_numbers

# easy password should contain atlest one character 
# and must contain number upt0 2 and letters upto 3

elif choice == 2:
    no_letters = random.randint(1,4)
    no_numbers = random.randint(0,3)
    no_symbols = 8 - no_letters - no_numbers

# hard password should contain atlest one character 
# and must contain number upt0 4 and letters upto 4
else:
    print("Enter a valid choice !!!")
    choice_validity = False

password_list = []

for i in range(0, no_letters):
    password_list.append(random.choice(letters))

for i in range(0, no_numbers):
    password_list.append(random.choice(numbers))
    
for i in range(0, no_symbols):
    password_list.append(random.choice(symbols))

password = ""

for character in password_list:
    password += character

if choice_validity:
    print(f"Your generated password is : {password}")


    