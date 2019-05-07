def longest_palindromic(str1):
    dict1 = {}
    list1 = [x for x in str1]
    for i, value in enumerate(list1):
        try:
            if value == list1[i + 1]:
                count = 1
                while 1:
                    try:
                        if i - count >= 0:
                            pass
                        else:
                            print(list1[9999999])
                        if list1[i - count] == list1[i + count + 1]:
                            count += 1
                        else:
                            str2 = ''
                            for alpha in list1[i - count + 1:i + count + 2]:
                                str2 += alpha
                            if len(list1[i - count - 1:i + count + 1]) in dict1.keys():
                                pass
                            else:
                                dict1[len(list1[i - count - 1:i + count + 1])] = str2
                            break
                    except:
                        str2 = ''
                        for alpha in list1[i - count + 1:i + count + 1]:
                            str2 += alpha
                        if len(list1[i - count + 1:i + count + 1]) in dict1.keys():
                            pass
                        else:
                            dict1[len(list1[i - count + 1:i + count + 1])] = str2
                        break
        except:
            pass
    for i, value in enumerate(list1):
        try:
            if value == list1[i + 2]:
                count = 1
                while 1:
                    try:
                        if list1[i - count] == list1[i + count + 2]:
                            count += 1
                        else:
                            str2 = ''
                            for alpha in list1[i - count + 1:i + count + 2]:
                                str2 += alpha
                            if len(list1[i - count + 1:i + count + 2]) in dict1.keys():
                                pass
                            else:
                                dict1[len(list1[i - count + 1:i + count + 2])] = str2
                            break
                    except:
                        str2 = ''
                        for alpha in list1[i - count + 1:i + count + 2]:
                            str2 += alpha
                        if len(list1[i - count + 1:i + count + 2]) in dict1.keys():
                            pass
                        else:
                            dict1[len(list1[i - count + 1:i + count + 2])] = str2
                        break
        except:
            pass
    list2 = [int(x) for x in dict1.keys()]
    list2.sort()
    list2.reverse()
    try:
        return dict1[list2[0]]
    except:
        return str1[0]

