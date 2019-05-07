def checkio(num1):
    list1 = []
    for x in range(2, 10).__reversed__():
        while 1:
            if num1 % x == 0:
                num1 = num1 // x
                list1.append(x)
            else:
                break
    if num1 >= 10:
        return 0
    elif 1 < num1 < 10:
        list1.append(num1)
    list1.sort()
    try:
        str1 = ''
        for x in list1:
            str1 += str(x)
        return int(str1)
    except:
        return 0
