def checkio(matrix):
    length = len(matrix)
    for x in range(length):
        for y in range(length):
            if abs(matrix[x][y]) != abs(matrix[y][x]) or matrix[x][y] == matrix[y][x] != 0:
                return False
    return True
