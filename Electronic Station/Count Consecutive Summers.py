def count_consecutive_summers(num):
    count = 1
    num_list = [x for x in range(1, num + 1)]
    for x in range(2, num + 1):
        for y in range(num):
            if sum(num_list[y:y + x]) == num and y + x < num:
                count += 1
    return count


print(count_consecutive_summers(1575))
