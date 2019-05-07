def pray(row, long=1):
    c = 1
    while c <= row:
        d = 1
        while d <= long:
            if (c + 2) % 2 != 0:
                if (d + 2) % 2 != 0:
                    print('*', end='')
                    d = d + 1
                else:
                    print('.', end='')
                    d = d + 1
            else:
                if (d + 2) % 2 != 0:
                    print('.', end='')
                    d = d + 1
                else:
                    print('*', end='')
                    d = d + 1
        print('\n')
        c = c + 1


a, b = input().split()
a = int(a)
if b == '':
    pray(a)
else:
    b = int(b)
    pray(a, b)
