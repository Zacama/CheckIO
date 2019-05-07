'''
def largest_histogram(*args):
    if len(args) == 1:
        list1 = [x for x in args[0]]
    else:
        list1 = [x for x in args]
    square_list = []
    try:
        for x in range(len(list1)):
            for i, value in enumerate(list1):
                mid_list = list1[i:i + x + 1]
                if len(mid_list) == x + 1:
                    square_list.append(sorted(mid_list)[0] * (x + 1))
    except:
        pass
    return sorted(square_list)[-1]
'''


def largest_histogram(*args):
    if len(args) == 1:
        list1 = [x for x in args[0]]
    else:
        list1 = [x for x in args]
    square_list = []
    for x in list1:
        square_list.append(x)
    while len(list1) > 1:
        for num in range(len(list1)):
            square_list.append((num + 1) * min(list1[0:num + 1]))
        list1.pop(0)
    return max(square_list)

