import logo

print(logo.logo)
print("AUCTION PROGRAM")

bidders_data = {}

def highest_bidder():
    nm = ""
    mx = -1
    for key in bidders_data:
        if bidders_data[key]>= mx:
            mx = bidders_data[key]
            nm = key
    print(f"Highest bidder is {nm}, with bid amount {mx}")


user_exists = True
while user_exists:
    name = input("Enter your name : ")
    amount = int(input("Enter your bidding amount : "))

    bidders_data[name] = amount

    ch = input("Is there any other user ? (y/n)").lower()
    if ch != "y":
        highest_bidder()
        user_exists = False
        