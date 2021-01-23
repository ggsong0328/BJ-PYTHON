T = int(input())
for i in range (T):
    b = input()
    results = list(b)
    add = cnt = 0
    for result in results:
        if result == 'O':
            cnt = cnt + 1
        else:
            cnt = 0
        add = add + cnt
    print(add)
