def best_stock(data):
    list1 = [x for x in data.values()]
    list1.sort()
    for x, y in data.items():
        if y == list1[-1]:
            return x


'''
def best_stock(data):
    return max(data, key=lambda code: data[code])

def best_stock(data):
    # your code here
    list = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return list[0][0]

def best_stock(data):
    # your code here
    return max(data.items(), key=lambda x: x[1])[0]

def best_stock(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1])
    return sorted_data[-1][0]



'''
