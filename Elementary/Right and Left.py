def left_join(tuple1):
    str1 = ''
    for x in tuple1:
        str1 += ','
        x = x.replace("right", "left")
        str1 += x
    str1 = str1[1:]
    return str1
