T = int(input())
for i in range(T):
    S = input()
    repeat = int(S[0])
    for j in S[2:]:
        print(j*repeat, end='')
    print()
