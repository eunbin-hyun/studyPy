# 구현 중 완전탐색: 가능한 경우의 수를 모두 검사해보는 탐색 방법
# 완전탐색 문제1: 시각의 3이 있으면 카운트 하기

h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
