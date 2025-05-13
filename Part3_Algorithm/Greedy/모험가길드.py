# 그리디1: 모험가 길드

n = int(input())
k = list(map(int, input().split()))

k.sort()
result = 0
m = []

for i in range(len(k)):
    count = k[i] -1
    count -= len(m)
    if count == 0:
        result += 1
        m = []
    else:
        m.append(k[i])

print(result)