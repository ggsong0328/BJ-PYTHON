N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
newscore = []
for score in scores:
    newscore.append(score/M*100)
avg = sum(newscore) / N
print(avg)
