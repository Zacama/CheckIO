def match1(n, m, p):
    dict1 = {}
    c = m
    while c <= p:
        count = 0
        for x in n:
            if x == c:
                count += 1
        dict1[c] = count
        c += 1
    return dict1


def delete(dict2):
    j = {}
    for k, v in dict2.items():
        if v != 1:
            j.update({k: v})
    return list(j.keys())


def match2(list3, list1):
    list2 = []
    for x in list3:
        for y in list1:
            if x == y:
                list2.append(x)
    return list2


text = eval(input())
text1 = text
text = sorted(text)
min1 = text[0]
max1 = text[len(text) - 1]
text = match1(text, min1, max1)
reference = []
reference = delete(text)
text = match2(text1, reference)
print(text)
