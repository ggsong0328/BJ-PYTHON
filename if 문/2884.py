H, M = map(int, input().split())
if (M - 45 < 0):
    if(H - 1 < 0):
        print("23 {}" .format(M + 15))
    else:
        print("{} {}" .format(H-1, M+15))
else:
    print("{} {}" .format(H, M - 45))
    
