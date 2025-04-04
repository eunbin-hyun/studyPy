# 구현2 - 완전탐색
# 완전탐색 문제1: 시각의 3이 있으면 카운트 하기

h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
