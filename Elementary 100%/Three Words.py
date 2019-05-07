def checkio(str1):
    count = 0
    list1 = [x for x in str1.split(' ')]
    for x in list1:
        if ord('a') <= ord(x[0]) <= ord('z') or ord('A') <= ord(x[0]) <= ord('Z'):
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
