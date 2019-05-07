def checkio(x):
    def form(x):
        list1 = [[0 for i in range(3)]for i in range(3)]
        row = 0
        while row < 3:
            count = 0
            for n in x[row]:
                list1[row][count] = n
                count += 1
            row += 1
        return list1

    def match(y):
        if (y[0][0] == y[0][1] == y[0][2]
           or y[0][0] == y[1][1] == y[2][2]
           or y[0][0] == y[1][0] == y[2][0]) is True and y[0][0] != '.':
                return y[0][0]
        else:
            if (y[0][1] == y[1][1] == y[2][1]
               or y[1][0] == y[1][1] == y[1][2]
               or y[2][0] == y[1][1] == y[0][2]) is True and y[1][1] != '.':
                return y[1][1]
            else:
                if (y[2][0] == y[2][1] == y[2][2]
                   or y[0][2] == y[1][2] == y[2][2]) is True and y[2][2] != '.':
                    return y[2][2]
                else:
                    return 'D'

    return match(form(x))

