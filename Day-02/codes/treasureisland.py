print("""
_/  |________   ____ _____    ________ _________   ____   |__| _____|  | _____    ____    __| _/
\   __\_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  |  |/  ___/  | \__  \  /    \  / __ | 
 |  |  |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  |  |\___ \|  |__/ __ \|   |  \/ /_/ | 
 |__|  |__|    \___  >____  /____  >____/ |__|    \___  > |__/____  >____(____  /___|  /\____ | 
                   \/     \/     \/                   \/          \/          \/     \/      \/ 
                   """)
print("Welcome to TREASURE ISLAND")
print("Your mission is to find the treasure.")

print("guide the bot ?")

ip = input("Left/ Right :").lower()

if ip == "left":
    ip = input("Swim/ Wait  :").lower()
    if ip == "wait":
        ip = input("Which door (Red/ Blue/ Yellow) :").lower()
        if ip == "yellow":
            print("Congratulations ! You got the trasure.")
        elif ip == "blue":
            print("Eaten by beasts !\n GAME OVER !")
        elif ip == "res":
            print("Burned by fire ! \nGAME OVER !")
    else:
        print("Attacked by traut. \nGAME OVER !")
else:
    print("Fell into a hole ! \nGAME OVER !")
