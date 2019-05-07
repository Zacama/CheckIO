times = int(input())
while times > 0:
    times -= 1
    line = input()
    row = int(line.split(' ')[0])
    num = int(line.split(' ')[1])
    row_count = 1
    while row > 0:
        row -= 1
        num_count = 1
        if row_count == 1 or row == 0:
            while num_count <= num:
                print('*', end='')
                num_count += 1
        else:
            while num_count <= num:
                if num_count == 1 or num_count == num:
                    print('*', end='')
                    num_count += 1
                else:
                    print('.', end='')
                    num_count += 1
        row_count += 1
        print('\n')
