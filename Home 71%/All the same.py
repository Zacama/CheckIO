def all_the_same(elements):
    bool1 = True
    for x in range(len(elements)-1):
        if hash(elements[x]) == hash(elements[x + 1]):
            pass
        else:
            return bool1 and False
    return bool1
