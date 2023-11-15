# REVISION

def funD(n):
    if n == 1:
        result = 1
    else:
        result = n + funD(n-1)
    return result


print(funD(3))
