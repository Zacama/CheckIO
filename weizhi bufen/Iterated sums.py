t = int(input())
a = '*.'
for i in range(t):
    line = input()
    l = int(line.split(' ')[0])
    c = int(line.split(' ')[1])
    for j in range(l):
        for k in range(c):
            print(a[int((j + k) % 2)], sep='', end='')
        print()
