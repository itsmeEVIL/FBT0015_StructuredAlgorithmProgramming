import math

# a


def Dn(n, r):
    return 1 / (1 + r)**n

# b


def tPrime(t, v, c):
    return t * (1 - v**2 / c**2)**(1/2)

# c


def V(r):
    return (4/3) * math.pi * (r**3)

# d


def quadratic(a, b, c):
    return -b + ((b**2) - (4 * a * c))**(1/2) / (2 * a)
