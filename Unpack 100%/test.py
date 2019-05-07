list1 = [[1, 2, 1, 1],
         [1, 1, 4, 1],
         [1, 3, 1, 6],
         [1, 7, 2, 5]]
list2 = [[list1[y][x] for y in range(4)] for x in range(4)]
print(list2)