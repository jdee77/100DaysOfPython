import random
print("Who will pay the bill?")
names = input("Enter everyones name separated with comma :").split(", ")

size = len(names)
person = random.randint(0, size-1)
print(f"Don't worry! {names[person]} will pay the bill !")