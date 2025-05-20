# 그리디4: 볼링공 고르기

n, m = map(int, input().split())
w = list(map(int, input().split()))
count = 0

for i in range(len(w)):
    target = w[i]
    for j in range(i+1, len(w)):
        if target != w[j]:
            count += 1 

print(count)