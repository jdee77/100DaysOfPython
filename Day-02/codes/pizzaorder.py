print("Pizza order Menu")

print("Enter pizza details :")
size = input("Size (S/M/L)").lower()
add_pepperoni = input("Want to add pepperoni (Y/N) :").lower()
extra_cheese = input("Want to add extra chees (Y/N) :").lower()

# price details 
# size S : $15, M : $20, L : $25
# add pepperoni, in small pizza : $2 and in big & medium pizza : $3
# extra cheese : $ 1

price = 0

if size == "s":
    price += 15
    if add_pepperoni == "y":
        price += 2
elif size == "m":
    price += 20
    if add_pepperoni == "y":
        price += 3
elif size == "l":
    price += 25
    if add_pepperoni == "y":
        price += 3

if extra_cheese == "y":
    price += 1

print(f"Price : {price}")


