def WorldCup(team):
    try:
        file.write(f"{team}\n")
        print("Name saved successfully in a file.", end=" ")
    except:
        print("Name failed to save in a file.", end=" ")


def WorldCup_display():
    file = open(
        r"C:\Users\User\Downloads\Uni\1st Sem\Structured Algorithm & Programming\Codes\Lab\Week 12\WCTeam.txt", "r")
    print(f"\nTeam saved in WCTeam.txt are:\n{file.read()}")
    file.close()


file = open(r"C:\Users\User\Downloads\Uni\1st Sem\Structured Algorithm & Programming\Codes\Lab\Week 12\WCTeam.txt", "w")

team = input("Enter the world cup team: ")

while team != "Quit":
    WorldCup(team)
    team = input("Quit to exit or else to continue: ")
else:
    file.close()
    print("Exit program")
    WorldCup_display()
