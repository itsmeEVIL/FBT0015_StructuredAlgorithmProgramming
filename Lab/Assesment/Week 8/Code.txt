import math


def calcBMI(weight, height):
    BMI = weight / math.pow((height / 100), 2)

    if 0 < BMI < 18.5:
        category = "Underweight"
    elif 18.5 <= BMI <= 24.9:
        category = "Normal Weight"
    elif 25 <= BMI <= 29.9:
        category = "Overweight"
    elif BMI >= 30:
        category = "Obesity"
    else:
        category = "Invalid"

    return BMI, category


while quit != "Q":
    height = eval(input("Please enter height in cm: "))
    weight = eval(input("Please enter weight in kg: "))

    BMI, category = calcBMI(weight, height)

    print(f"Your BMI value is {BMI:.2f}")
    print(f"You are in the {category} category")

    quit = input("\nEnter Q to end or any character to continue: ").upper()
