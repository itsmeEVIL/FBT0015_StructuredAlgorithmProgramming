listFoo = [3, 6, 9, 12, 15, 18, 21]
listFaa = [4, 8, 12, 16, 20, 24, 28]


# a
listFum = listFoo[:3] + listFaa[3:]

print(listFum)

# b
listFee = listFoo[1::2] + listFaa[::2]

print(listFee)

# c
element = listFoo.pop(4)
listFaa.insert(1, element)
listFaa.append(element)

print(listFoo)
print(listFaa)
