# 1a

countEmp = 0

while countEmp < 5:
    hour = int(input('Please Enter Hours of Working: '))
    rate = float(input('Please Enter Rate for each Hours: '))

    print(f'Weekly payment is RM {hour * rate}')
    countEmp += 1

print('All employees salary are processed.')

# 1b

"""
Weekly payment is RM 287.5
Weekly payment is RM 287.5
Weekly payment is RM 287.5
Weekly payment is RM 287.5
Weekly payment is RM 287.5
All employees salary are processed.
"""

# 2

"""
Handtrace Ouput:
*      *       *       *       *       *       *       *       *       *
"""

CountStar = 0
Num = eval(input("Please enter a number: "))

while CountStar < Num:
    print("*", end="\t")
    CountStar += 1

# 3

"""
X = 3
Count = 0

while Count < 3:
    X = X * X
    print(X)
Count = Count + 1
print(Count)
"""
# 3a

"""
It will repeat the loop infinitely. It will display the value of X.
"""

# 3b

"""
It will only repeat the loop 3 times, and printing the X value 3 times.
"""

# 3c

"""
It will only repeat the loop 2 times, and printing the x value 2 times.
"""

# 3d

"""
It will repeat the loop infinitely.
"""
