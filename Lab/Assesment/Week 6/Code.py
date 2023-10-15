while True:
    try:
        num = int(input("Enter a number: "))

        if 1 <= num <= 100:
            if num % 3 == 0:
                print("Fizz", end="")
            if num % 5 == 0:
                print("Buzz", end="")
            if num % 3 != 0 and num % 5 != 0:
                print(num, end="")
        else:
            print(num, end="")

        isQuit = input("\nType Quit to quit: ").upper()
        if isQuit == "QUIT":
            break

    except ValueError:
        print("Error! Not an interger. Please try again.")
