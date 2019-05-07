from functools import reduce


def multiply(x, y):
    return x * y


def checkio(num):
    return reduce(multiply, [int(x) for x in str(num) if int(x) != 0])
