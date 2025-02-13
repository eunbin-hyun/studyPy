#그리디 알고리즘
#탐욕적인 방법으로 각 단계에서 최적의 방법을 선택

# 문제: N이 1이 될 때까지
# 풀이: 나눌수 있는 최대로 나누고 나머지는 -1해주기
n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)