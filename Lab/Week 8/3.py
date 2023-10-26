questions = [
    "Do you stay online longer than you intended?",
    "Do you hear other people in your life complain about how much time you spend online?",
    "Do you say or think, 'Just a few more minutes' when online?",
    "Do you try and fail to cut down on how much time you spend online?",
    "Do you hide how long you've been online?"
]

minuteSpent = eval(input("How long did you spent on the internet (minutes): "))

hourSpent = minuteSpent / 60

if hourSpent >= 2:
    print("You might be addicted to the Net")

    yesCount = 0
    for question in questions:
        answer = input(f"{question} (Yes/No): ").lower()

        if answer == "yes":
            yesCount += 1

    if yesCount >= 3:
        print("You are an INTERNET ADDICT")
    else:
        print("Control your Internet usage. You might become an ADDICT")

elif 0 < hourSpent < 2:
    print("Keep up good habit")

else:
    print("Invalid! Negative hour spent")
