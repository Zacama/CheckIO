def bigger_price(num, list1):
    final_list = []
    list2 = [x['price'] for x in list1 ]
    list2 = sorted(list2)
    list2.reverse()
    list3 = list2[0:num]
    for count in range(len(list3)):
        for x in list1:
            if x['price'] == list3[count]:
                final_list.append(x)
    return final_list
