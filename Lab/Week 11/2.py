# 1.

"""

def func_a():
    print('inside func_a')


def func_b(y):
    print('inside func_b')
    return y


def func_c(z):
    print('inside func_c')
    return z()


print(func_a())
print(5+func_b(2))
print(func_c(func_a))

Output:

inside func_a
None
inside func_b
7
inside func_c
inside func_a
None

"""

# 2.

"""

def f(y):
    y = y+3
    x = 1
    x += 1
    print(x)
    print(y)


def g(y):
    print(x)
    print(x+1)


def h(y):
    return x+1


x = 5
f(x)
print('after call 1', x)

g(x)
print('after call 2', x)

h(x)
print('after call 3', x)


Output:

2
8
after call 1 5
5
6
after call 2 5
after call 3 5

"""

# 3.

"""

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x


x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)

Output:

in f(x): x = 4
in main program scope: z = 4
in main program scope: x = 3
in g(x): x = 4
in h(x): x = 5
in main program scope: x = 3
in main program scope: z = 4

"""
