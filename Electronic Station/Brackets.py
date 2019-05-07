def checkio(str1):
    list_a = ("{", "[", "(")
    list_b = ("}", "]", ")")
    list2 = [x for x in str1 if x in list_a + list_b]
    list3 = []
    try:
        for x in list2:
            if x in list_a:
                list3.append(x)
            elif x in list_b:
                if list_a.index(list3[-1]) == list_b.index(x):
                    list3.pop(-1)
                else:
                    return False
    except:
        return False
    return True if len(list3) == 0 else False
