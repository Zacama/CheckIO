def checkio(*arg):
    return max(*arg) - min(*arg) if len([x for x in arg]) > 1 else 0


