def correct_sentence(x):
    x = str.capitalize(x)
    if x[len(x) - 1] != '.':
        x += '.'
    return x


print(correct_sentence('greetings, friends'))
