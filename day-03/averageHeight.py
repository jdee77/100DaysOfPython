print("Average height calcualtor.")
height = input("Enter the heights of stuents (separated by commas) :")
heightList = height.split()
sum = 0
i = 0

for x in heightList:
    sum = sum + int(x)
    i = i + 1

avg = round(sum/ i)

print(f"The average height of all students is {avg}")

for i in range(1, 100):
    print(i)