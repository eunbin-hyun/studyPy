# 접두사 합을 활용한 구간 합 계산 소스코드
n = 5  # 데이터의 개수 N
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

# left ~ right 구간 합을 계산 (3번재 수부터 4번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])