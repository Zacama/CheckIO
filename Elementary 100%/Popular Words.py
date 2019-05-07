def popular_words(str1, list1):
    str1 = str1.lower()
    str1 = ' '.join(str1.split())
    print(str1)
    dict1 = {}
    str_list = [x for x in str1.split(' ')]
    while 1:
        for x in list1:
            count = 0
            for y in str_list:
                if x == y:
                    count += 1
            dict1[x] = count
        break
    return dict1


'''
def popular_words(text: str, words: list) -> dict:
    
    text = (text.lower()).split()
    dict = {}
    val = []
    index = 0
    count = 0
    
    for w in words:
        count = 0
        for t in text:
            if w == t:
                count += 1
        val.append(count)
    
    for i in range(len(words)):
        dict[words[i]] = val[i]
    
    return dict
    

def popular_words(text: str, words: list) -> dict:
    result = dict()
    ltext = text.lower().split()
    for word in words:
        result[word] = ltext.count(word)
    return result

def popular_words(text, words):
    text = text.lower().split()
    return {word:text.count(word) for word in words}

def popular_words(text: str, words: list) -> dict:
    return dict([(i, text.lower().split().count(i)) for i in words])
    
def popular_words(text: str, words: list) -> dict:
    return {word: text.lower().split().count(word) for word in words}

from collections import Counter
def popular_words(text: str, words: list) -> dict:
    o = Counter(text.lower().split())
    return {x:o[x] for x in words}
'''
