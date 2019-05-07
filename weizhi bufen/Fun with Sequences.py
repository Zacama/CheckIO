def get(*kw):
    h = []
    kw = input()
    for l in kw:
        if l == ' ':
            pass
        else:
            h.append(l)
    return list(map(int, h))


n1, n2, n, list1, list2, list3 = 0, 0, 0, [], [], []
a = int(input())
list1 = get()
b = int(input())
list2 = get()
for z in list1:
    y = 1
    for x in list2:
        if z != x:
            y = y * 1
        else:
            y = y * -1
    if y == 1:
        list3.append(z)
    else:
        pass
    n += 1
list4 = sorted(list3)
for x in list4:
    print(x)
