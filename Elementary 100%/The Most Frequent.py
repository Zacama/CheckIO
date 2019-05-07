def most_frequent(list1):
    return max({x: list1.count(x) for x in list1}, key=lambda x: {x: list1.count(x) for x in list1}[x])