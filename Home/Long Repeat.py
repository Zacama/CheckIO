def long_repeat(string1):
    if string1 is not '':
        list1 = []
        reference_string = string1[0]
        count = 0
        count1 = 0
        while count1 <= len(string1) - 1:
            if string1[count1] == reference_string:
                count += 1
                count1 += 1
            else:
                reference_string = string1[count1]
                if count != 0:
                    list1.append(count)
                    count = 0
        if list1 is False:
            return len(string1)
        else:
            return sorted(list1, reverse=True)[0]
    else:
        return 0


print(long_repeat('aaaaaa'))