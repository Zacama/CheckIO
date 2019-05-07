def checkio(a, b):
    list1 = [str(x) for x in bin(a)]
    list2 = [str(x) for x in bin(b)]
    list1 = list1[2:]
    list2 = list2[2:]
    list1.reverse()
    list2.reverse()
    for x in range(max(len(list1), len(list2)) - len(list1)):
        list1.append('0')
    for x in range(max(len(list1), len(list2)) - len(list2)):
        list2.append('0')
    list1.reverse()
    list2.reverse()
    list3 = [int(x) ^ int(y) for x, y in zip(list1, list2)]
    return list3.count(1)
