print("BMI CALCULATOR")

height = float(input("Enter your height (in meter):"))
weight = int(input("Enter your weight (in KG) :"))

bmi = round(weight / height ** 2, 3)


# assert the user with the following measures.
# bmi < 18.5                UNDERWEIGHT
# 18.5 < BMI < 24.5         HEALTHY
# BMI > 24.5                OVER WEIGHT


if bmi < 18.5:
    print(f"BMI :{bmi}, UNDER WEIGHT.")
elif bmi < 24.5:
    print(f"BMI :{bmi}, HEALTHY.")
else:
    print(f"BMI :{bmi}, OVER WEIGHT.")