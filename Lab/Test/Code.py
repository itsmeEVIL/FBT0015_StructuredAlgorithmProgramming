print("============================")
print("Crop Harvest Advisory System")
print("============================")
cropName = input("Please enter the crop name: ")

while True:
    growthPeriod = int(
        input("Please enter the crop's estimated growth period in days: "))

    print(f"Crop Name: {cropName}")
    print(f"Estimated Growth Period: {growthPeriod} days")

    if 0 < growthPeriod <= 30:
        print("It's recommended to harvest your crop in the next week.")
    elif 31 <= growthPeriod <= 60:
        print("You can start preparing for the harvest within the next two weeks.")
    elif 61 <= growthPeriod <= 90:
        print("The best time for harvest is within the next month.")
    elif growthPeriod > 90:
        print("Your crop is a long-term crop. Harvesting time can vary based on factors like weather, soil condition, and crop variety.")

        factors = input(
            "Is the weather forecast favorable for your crop? [Y/N] : ")

        if factors == "Y":
            print("You should start monitoring your crop's condition and be prepared for harvesting when it's ready.")
        elif factors == "N":
            print("Consider consulting with local agricultural experts for advice on managing your long-term crop.")
        else:
            while True:
                factors = input(
                    "WRONG INPUT... Please answer again. Is the weather forecast favorable for your crop? [Y/N] : ")

                if factors == "Y":
                    print(
                        "You should start monitoring your crop's condition and be prepared for harvesting when it's ready.")
                    break
                elif factors == "N":
                    print(
                        "Consider consulting with local agricultural experts for advice on managing your long-term crop.")
                    break

        #  while factors not in ["Y", "N"]:
        #     factors = input(
        #         "WRONG INPUT... Please answer again. Is the weather forecast favorable for your crop? [Y/N] : ")

        #     if factors == "Y":
        #         print("You should start monitoring your crop's condition and be prepared for harvesting when it's ready.")
        #     else:
        #         print("Consider consulting with local agricultural experts for advice on managing your long-term crop.")
    else:
        print("Invalid growth period!")

    cropName = input(
        "\nPlease enter another crop's name or Exit to end the program: ")

    if cropName == "Exit":
        print("\nThank you for using the Crop Harvest Advisory System.")
        break
