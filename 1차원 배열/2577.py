A = int(input())
B = int(input())
C = int(input())
result = A * B * C
r_list = list(str(result))
for i in range (10):
    count = r_list.count(str(i))
    print(count)
