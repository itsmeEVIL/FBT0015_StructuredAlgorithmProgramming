# a

import math
for NextCh in range("A", "Z"):
    print(NextCh)
    print()

"""
TypeError: 'str' object cannot be interpreted as an integer
"""

# b

A, Z = 2, 8

for NextCh in range(A, Z, 4):
    print(NextCh)
    print()

"""
2

6

"""

# c

MAX = 4
print("\t", 'i', "\t\t", 'i * i', "\t\t", 'Square root')
for i in range(1, MAX):
    Square = i*i
    Root_i = math.sqrt(i)

    print('{:>6}{:>12}{:>12.2f}'.format(i, Square, Root_i))


"""
     i           i * i          Square root
     1           1              1.00
     2           4              1.41
     3           9              1.73
"""

# d

for num in range(4):
    for i in range(num):
        print(num, end=" ")
    print("\n")

"""

1

2 2

3 3 3

"""
