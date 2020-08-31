def to_encrypt(str1, num):
    str_print = ''
    for x in str1:
        if x == ' ':
            str_print += x
        elif x != ' ':
            str_print += chr(ord('a') + ((ord(x) - ord('a')) + num) % 26)
    return str_print
