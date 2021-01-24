def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x)
    return int(n) + a

a = []

for i in range (1, 10001):
    x = d(i)
    a.append(x)

for b in range (1, 10001):
    if b in a:
        pass
    else:
        print(b)
