VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(str1):
    str1 += ','
    list1 = []
    str2 = ''
    for x in str1:
        if x.isalpha():
            print(x)
            str2 += x
        else:
            print(str2)
            if len(str2) > 1:
                str2 = str2.upper()
                list1.append(str2)
                str2 = ''
    count = 0
    print(list1)
    for x in list1:
        if x[0] in VOWELS:
            buer = 1
        elif x[0] in CONSONANTS:
            buer = 0
        for y in x:
            if y in VOWELS and buer == 1:
                buer = 0
            elif y in VOWELS and buer == 0:
                buer = 8
                break
            elif y in CONSONANTS and buer == 0:
                buer = 1
            elif y in CONSONANTS and buer == 1:
                buer = 8
                break
        if buer != 8:
            count += 1
    return count

