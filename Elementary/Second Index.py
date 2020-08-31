def second_index(str1, letter):
    count = 0
    for x, y in zip(str1, range(len(str1))):
        if x == letter and count == 1:
            return y
        elif x == letter and count == 0:
            count += 1
    return None


def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2:
        return None
    FirstIndex = text.find(symbol)
    text = text[FirstIndex + 1:]
    SecondIndex = text.find(symbol)
    return FirstIndex + SecondIndex + 1

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    index_resault = 0
    index_resault = text.find(symbol,text.find(symbol)+1)
    if index_resault == -1 :
        index_resault = None
    return index_resault
