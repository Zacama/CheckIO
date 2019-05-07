def add(list1, num, number):
    if num >= 0:
        number = number + list1[num]
        num -= 1
        return add(list1, num, number)
    else:
        return number


def checkio(list1):
    return add(list1, len(list1) - 1, 0)
