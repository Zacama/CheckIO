def checkio(str1, step):
    if step == 1 and len(str1) > 1 and str1.count('w') != 0:
        return round(str1.count('w')/len(str1), 2)
    elif step == 1 and len(str1) > 1 and str1.count('w') == 0:
        return 0
    elif step == 1 and len(str1) == 1:
        if str1 == 'w':
            return 1
        else:
            return 0
    possible_result_list = [[str1.count('w'), str1.count('b'), 1]]
    while step > 1:
        mid_list = []
        for one_mid_possible in possible_result_list:
            if one_mid_possible[0] != 0 and one_mid_possible[1] != 0:
                mid_list.append([one_mid_possible[0]-1, one_mid_possible[1]+1, one_mid_possible[2]*(one_mid_possible[0]/len(str1))])
                mid_list.append([one_mid_possible[0]+1, one_mid_possible[1]-1, one_mid_possible[2]*(one_mid_possible[1]/len(str1))])
            elif one_mid_possible[0] == 0:
                mid_list.append([one_mid_possible[0]+1, one_mid_possible[1]-1, one_mid_possible[2]*(one_mid_possible[1]/len(str1))])
            elif one_mid_possible[1] == 0:
                mid_list.append([one_mid_possible[0]-1, one_mid_possible[1]+1, one_mid_possible[2]*(one_mid_possible[0]/len(str1))])
        possible_result_list = mid_list
        step -= 1
    result_list = [x[2]*x[0]/len(str1) for x in possible_result_list]
    return round(sum(result_list), 2)

