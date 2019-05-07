def checkio(num):
    str1 = ''
    table = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    list1 = [x for x in str(num)]
    list1.reverse()
    for index1, value in enumerate(list1):
        if int(value) <= 3:
            for x in range(int(value)):
                str1 = table[index1 * 2] + str1
        elif int(value) == 4:
            str1 = table[index1 * 2] + table[index1 * 2 + 1] + str1
        elif 5 <= int(value) <= 8:
            for x in range(int(value) - 5):
                str1 = table[index1 * 2] + str1
            str1 = table[index1 * 2 + 1] + str1
        elif int(value) == 9:
            str1 =  table[index1 * 2] +table[index1 * 2 + 2]+ str1
        elif int(value) == 0:
            pass
    return str1

