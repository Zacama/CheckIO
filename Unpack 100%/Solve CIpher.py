def recall_password(list1, list2):
    str1 = ''
    for x, y in zip(list1, list2):
        for a, b in zip(x, y):
            if a == 'X':
                str1 += b
    return str1