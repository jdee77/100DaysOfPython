print("Love Calculator.")

his = input("Enter his name :").lower()
her = input("Enter her name :").lower()

true = 0
love = 0

for char in his:
    if char == "t" or char == "r" or char == "u" or char == "e":
        true += 1
    if char == "l" or char == "o" or char == "v" or char == "e":
        love += 1

score = true * 10 + love

print(f"your love score is : {score}.")

if score < 10 and score > 90:
    print('"You go together like coke and mentos."')
elif score > 40 and score < 50:
    print('"You are alright together."')
else:
    print('"Enjoy your life."')