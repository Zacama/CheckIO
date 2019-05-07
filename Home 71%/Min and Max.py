def min_max(args, key, ok):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=ok)[0]


def max(*args, key=None):
    return min_max(args, key, True)


def min(*args, key=None):
    return min_max(args, key, False)
