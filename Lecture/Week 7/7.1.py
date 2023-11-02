expenseList = []

for i in range(1, 6):
    expenseValue = eval(input(f"Enter the expense value for day {i}: "))
    expenseList.append(expenseValue)

print("The expense value for the 5 days:")

for j in expenseList:
    print(j, end=" ")

print(
    f"\nThe highest expense is {max(expenseList)} at day {expenseList.index(max(expenseList)) + 1}")
print(
    f"The lowest expense is {min(expenseList)} at day {expenseList.index(min(expenseList)) + 1}")
print(f"The total expense is {sum(expenseList)}")
