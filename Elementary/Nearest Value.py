def nearest_value(values: set, one: int) -> int:
    values = sorted(values)
    num, mid = 0, 9999
    for value in values:
        if mid > abs(value - one):
            num, mid = value, abs(value - one)
        else:
            return num
    return num


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

# 之前的解法，有问题
# def nearest_value(values: set, one: int) -> int:
#     origin = list(values)
#     values = list(map(lambda x: abs(x - one), values))
#     return origin[values.index(min(values))]
