'''
def repeat_inside(str1):
    length = len(str1) // 2 + 1
    dict1 = {}
    try:
        for x in range(length):
            for i, value in enumerate(str1):
                if str1[i:i + x + 1] == str1[i + 2 * x:i + 3 * x + 1]:
                    dict1[x + 1] = str1[i:i + 3 * x + 1]
    except:
        pass
    list1 = [x for x in dict1.keys()]
    list1.sort()
    return dict1[list1[-1]]
'''


def repeat_inside(str1):
    str1_list = [x for x in str1]
    str_dict = {}
    for num in range(1, len(str1_list) // 2+1):
        mid_str1 = ''
        try:
            for i, value in enumerate(str1_list):
                mid_str1 = value
                for x in range(1, len(str1_list) // num + 1):
                    if str1_list[i + num * x] == value:
                        mid_str1 += value
                    else:
                        if len(mid_str1) > 1:
                            str_dict[len(mid_str1)] = mid_str1
        except:
            if len(mid_str1) > 1:
                str_dict[len(mid_str1)] = mid_str1
    return str_dict[max([x for x in str_dict.keys()])]


print(repeat_inside('abcabcabab'))