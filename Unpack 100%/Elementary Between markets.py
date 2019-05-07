def between_markets(str1, str2, str3):
    if str2 not in str1 and str3 in str1:
        return str1[:str1.find(str3)]
    elif str2 in str1 and str3 not in str1:
        return str1[str1.find(str2) + 1:]
    elif str2 in str1 and str3 in str1 and str1.find(str2) > str1.find(str3):
        return ''
    elif str2 in str1 and str3 in str1 and str1.find(str2) <= str1.find(str3):
        return str1[str1.find(str2) + 1:str1.find(str3)]