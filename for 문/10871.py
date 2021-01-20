import sys

N, X = map(int, input().split())
A = sys.stdin.readline().split()
for i in A:
    i = int(i)
    if i < X:
        print(i, end=" ")
