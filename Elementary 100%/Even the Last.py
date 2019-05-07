def checkio(list1):
    return (sum(x for x, y in zip(list1, range(len(list1))) if y % 2 == 0) * list1[-1]) if len(list1) > 0 else 0
'''
def checkio(list1):
    return sum(x for x in list1 if list1.index(x) % 2 == 0) * list1[-1] if len(list1) != 0 else 0


print(checkio([-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62, 26, -76, 55, -24, 84, 49, -65, 41]))

'''