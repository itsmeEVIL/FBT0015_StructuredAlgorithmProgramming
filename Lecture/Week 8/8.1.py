# def nPrintln(*message):
#     print(message[3])


# nPrintln("sayang", "saya", "say", "saying", "sayung")

def main():
    lst = [1, 2, 3, 4, 5]
    reverse(lst)
    for value in lst:
        print(value, end=' ')


def reverse(lst):
    new_lst = len(lst) * [0]
    for i in range(len(lst)):
        new_lst[i] = lst[len(lst) - 1 - i]
    lst = new_lst


main()
