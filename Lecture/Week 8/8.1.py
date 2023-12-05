# def nPrintln(*message):
#     print(message[3])


# nPrintln("sayang", "saya", "say", "saying", "sayung")

def main():
    lst = [1, 2, 3, 4, 5]
    lst = reverse(lst)
    for value in lst:
        print(value, end=' ')


def reverse(lst):
    new_lst = len(lst) * [0]
    print(new_lst)
    for i in range(len(lst)):
        new_lst[i] = lst[len(lst) - 1 - i]
    print(new_lst)
    return (new_lst)


main()
