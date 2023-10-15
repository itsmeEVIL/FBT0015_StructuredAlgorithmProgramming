waveHeight = eval(input("Enter wave height: "))

if 1 <= waveHeight < 8:
    print("The tsunami is strong")

    regionName = str(input("Enter region name(Asia/Africa): ").lower())

    if regionName == "asia":
        print("Send a research team")
    else:
        print("Keep on monitoring")

if waveHeight >= 8:
    print("The tsunami is destructive")

    regionName = str(input("Enter region name(Asia/Africa): ").lower())

    if regionName == "asia":
        print("Send a rescue team")
    else:
        print("Keep on monitoring")
