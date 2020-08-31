def first_word(x):
    str1 = ''
    str2 = ''
    while (ord('A') <= ord(x[0]) <= ord('Z')) is False and (ord('a') <= ord(x[0]) <= ord('z')) is False:
        x = x[1:]
    for n in x:
        if n != chr(32):
            str1 += n
        else:
            break
    for m in str1:
        if ord('A') <= ord(m) <= ord('Z') or ord('a') <= ord(m) <= ord('z') or ord(m) == 39:
            str2 += m
    return str2


print(first_word("fdfewfew"))#这里要用双引号哦，因为如果字符串里有单引号没救gg了
