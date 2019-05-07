def check1(password):
    length = len(password)
    return length >= 10


def check2(password):
    a = True
    for x in password:
        a = a and 48 <= ord(x) <= 57 or 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122
    return a


def check3(password):
    number = 0
    caps = 0
    discaps = 0
    for x in password:
        if 48 <= ord(x) <= 57:
            number += 1
        elif 65 <= ord(x) <= 90:
            caps += 1
        else:
            discaps += 1
    return discaps > 0 and caps > 0 and number > 0


def combination(password):
    a = check1(password)
    b = check2(password)
    c = check3(password)
    if a and b and c is True:
        return True
    else:
        return False


password1 = input()
print(combination(password1))
