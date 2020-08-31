def match(x):
    a = ''
    for n in x:
        if n.isalpha() is True:
            a += n
        else:
            pass
    a = a.lower()
    return a


def match_op(y, up, start):
    alphabet = start
    b = {}
    c = 1
    while c == 1:
        count = 0
        for m in y:
            if m == alphabet:
                count += 1
            else:
                pass
        b[alphabet] = count
        if alphabet == up:
            c = 2
        else:
            pass
        alphabet = chr(ord(alphabet) + 1)
    return b


text = input()
text = sorted(match(text))
switch = ''
for x in text:
    switch += x
text = switch
start = text[0]
alpa = text[len(text) - 1]
text = match_op(text, alpa, start)
j = {}
for k, v in text.items():
    if v != 0:
        j.update({k: v})
text = j
text = sorted(text.items(), key=lambda n: n[1])
text.reverse()
max = text[0][1]
text = dict(text)
l = {}
for k, v in text.items():
    if v == max:
        l.update({k: v})
text = l
text = sorted(text.items(), key=lambda n: n[0])
print(text[0][0])     #return text[0][0]

