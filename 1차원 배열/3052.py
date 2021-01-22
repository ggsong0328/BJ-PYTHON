arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr) #set함수는 중복을 제거하기 위한 필터역할
print(len(arr))
