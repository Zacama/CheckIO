def is_stressful(str1):
    if str1[-1] == '!' and str1[-2] == '!' and str1[-3] == '!':
        return True
    str3 = ''
    for x in str1:
        if x.isalpha():
            str3 += x
    str1 = str3
    buer2 = 1
    for x in str1:
        if ord('a')<= ord(x) <= ord('z'):
            buer2 = buer2 * 0
    if buer2 == 1:
        return True
    str1 = str1.lower()
    word_list = ['help', 'asap', 'urgent']
    str2 = ''
    for x, y in zip(str1[0:-1], str1[1:]):
        if x == y:
            pass
        elif x != y:
            str2 += x
    str2 += str1[-1]
    print(str1)
    print(str2)
    buer = 1
    for x in word_list:
        if x in str2:
            buer = buer * 0
    return True if buer == 0 else False
