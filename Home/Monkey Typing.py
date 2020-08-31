def count_words(str1, dictory):
    count = 0
    str = ''
    for x in str1:
        str += x.lower()
    print(str)
    for x in dictory:
        length = len(x)
        better = x[0]
        for y, z in zip(str, range(len(str))):
            word = ''
            if y == better:
                for a in str[z:z + length]:
                    word += a
                if word == x:
                    count += 1
                    break
    return count


print(count_words("How aresjfhdskfhskd you?", ["how", "are", "you", "hello"]))



def count_words(text: str, words: set) -> int:
    counter = 0
    for word in words:
        if text.lower().find(word) != -1:
            counter += 1
    return counter

def count_words(text: str, words: set) -> int:
    return len([i for i in words if i in text.lower()])


def count_words(text: str, words: set) -> int:
    text = text.lower()
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for i in punctuation:
        text = text.replace(i, "")

    result = 0
    for word in words:
        if word in text:
            result += 1

    return result

import re


def count_words(text: str, words: set) -> int:
    amount = 0
    for i in words:
        word = re.compile(i)
        if word.search(text.lower()):
            amount += 1
    return amount

import re
def count_words(text: str, words: set) -> int:
    list = [re.search(j, text, re.I) for j in words if re.search(j, text, re.I)]
    return len(list)

def count_words(text: str, words: set) -> int:
    k=0
    rex=set(text.lower().replace(',','').replace('!','').split())
    for i in rex:
        for word in words:
            if word in i:
                k+=1
    return k


def count_words(text: str, words: set) -> int:
    return sum(word in text.lower() for word in words)

def count_words(text, words):
    return sum(w in text.lower() for w in words)