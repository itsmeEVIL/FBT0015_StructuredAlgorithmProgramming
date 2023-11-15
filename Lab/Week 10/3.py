integerList = []

integer = int(input("Enter an integer to start the program"))

integerList.append(integer)

while True:
    integer = int(
        input("Enter another integer.[Enter -32767 to stop the program]"))

    if integer == -32767:
        break

    integerList.append(integer)

print(
    f"The largest number among {len(integerList)} number of intergers entered is {max(integerList)}")
