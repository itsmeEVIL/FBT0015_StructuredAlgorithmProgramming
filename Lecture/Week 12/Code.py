print("=============================")
print("UTP Average Grade Calculator")
print("=============================")


def calc_average(list_scores):
    average = sum(list_scores) / len(list_scores)
    return average


def assign_grades(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


num = int(input("Enter number of students: "))

while True:
    main_list = []

    for i in range(1, num + 1):
        marks = eval(input(f"Student #{i} marks: "))
        main_list.append(marks)

    average = calc_average(main_list)

    print(f"Number of students: {num}")
    print(f"Average score is: {average}")
    print(f"Average grade is: {assign_grades(average)}")

    num = int(input("\nEnter the next number of students or -1 to end program: "))

    if num == -1:
        print("End program....")
        break
