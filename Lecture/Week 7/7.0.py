# s = 0
# j = 3
# k = 8
# t = 2

# for j in range(1, 6):
#     print(j, end="")
#     s = s + j
# print(s)

# for k in range(2):
#     print(k, end="")

# for i in range(10, 0, -1):
#     print(i)

# for i in range(j, k + 1):
#     print(i + t)

# data = eval(input("enter: "))

# sum = 0
# while data != 0:
#     sum += data

#     data = eval(input("enter"))

# print(f"the sum is {sum}")

s = 0
j = 3
k = 8
l = 2

for j in range(1, 5):
    print(j, end="")
    s = s + j
print(s)

for k in range(2):
    print(k, end="")

for i in range(10, 1, -1):
    print(i)

print(i)
print(j)
print(k)

for i in range(j, k + 1):
    print(i)
    print(i + 1)

print('skip last for loop')

"""
|  s  |  j  |  k  |  l  |  i  | output |
   0     3     8     2     10   123410
   1     1     0           9    0110
   3     2     1           8    9
   6     3                 7    8
   10    4                 6    7
                           5    6
                           4    5
                           3    4
                           2    3
                                2
                                2
                                4
                                1
                                skip last for loop

"""
