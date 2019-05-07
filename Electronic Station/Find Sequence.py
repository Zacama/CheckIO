def checkio(list1):
    length = len(list1)
    for x in list1:
        for addr, value in enumerate(x[:-3]):
            if x[addr + 1] == value and x[addr + 2] == value and x[addr + 3] == value:
                return True
    list2 = [[list1[y][x] for y in range(length)] for x in range(length)]
    for x in list2:
        for addr, value in enumerate(x[:-3]):
            if x[addr + 1] == value and x[addr + 2] == value and x[addr + 3] == value:
                return True
    for addry, value1 in enumerate(list1[:-3]):
        for addrx, value2 in enumerate(value1[:-3]):
            if list1[addry + 1][addrx + 1] == value2 and list1[addry + 2][addrx + 2] == value2 and list1[addry + 3][addrx + 3] == value2:
                return True
    list3 = [[y for y in reversed(x)] for x in list1 ]
    for addry, value1 in enumerate(list3[:-3]):
        for addrx, value2 in enumerate(value1[:-3]):
            if list3[addry + 1][addrx + 1] == value2 and list3[addry + 2][addrx + 2] == value2 and list3[addry + 3][addrx + 3] == value2:
                return True
    return False

