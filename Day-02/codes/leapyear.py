print("LEAP YEAR")

year = int(input("Enter the year :"))

leapYear = False

# a year is leap year if its evenly divisible by 4
# except evenly divisible by 100
# unless not divisible by 400

if year % 100 == 0:
    if year % 400 == 0:
        leapYear = True
else:
    if year % 4 == 0:
        leapYear = True

if leapYear:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year.")