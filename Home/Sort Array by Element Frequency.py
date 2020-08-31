from collections import Counter


def frequency_sort(items):
    dict1 = Counter(items)
    list2 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    list3 = []
    for y in list2:
        for times in range(y[1]):
            list3.append(y[0])
    return list3
