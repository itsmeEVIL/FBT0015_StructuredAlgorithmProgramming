def perimeterRect():
    base = eval(input("Enter the base: "))
    height = eval(input("Enter the height: "))

    perimeter = (2 * base) + (2 * height)

    print(f"The perimeter is {perimeter}")


def areaTriangle():
    base = eval(input("Enter the base: "))
    height = eval(input("Enter the height: "))

    area = (base * height) / 2

    print(f"The area is {area}")


def celToFahr():
    temp = eval(input("Enter the temperature: "))

    T = temp * 1.8 + 32

    print(f"The temperature in Fahrenheit is {T}")


def fahrToCel():
    temp = eval(input("Enter the temperature: "))

    T = (temp - 32) / 1.8

    print(f"The temperature in Celcius is {T}")


print("Please enter one of the following: ")
print("A. Perimeter for a Rectangle\nB. Area of a triangle\nC. Convert Celcius to Fahrenheit\nD. Convert Fahrenheit to Celcius")

option = input("A/B/C/D: ").upper()

if option == "A":
    perimeterRect()
elif option == "B":
    areaTriangle()
elif option == "C":
    celToFahr()
elif option == "D":
    fahrToCel()
else:
    print("Not a valid option.")
