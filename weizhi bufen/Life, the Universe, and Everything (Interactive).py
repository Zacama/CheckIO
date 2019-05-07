a = []
b = 1
while b > 0:
    c = input()
    c = int(c, base=10)
    if c != 42:
        print(c)
    else:
        print(42)
        b = -1
