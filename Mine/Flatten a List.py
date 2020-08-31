def flat_list(list1):
    list2 = []
    for x in list1:
        if type(x) is int:
            list2.append(x)
        else:
            for y in x:
                list2.append(y)
    return sorted(list2)