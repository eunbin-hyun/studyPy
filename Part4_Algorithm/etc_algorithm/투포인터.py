# 투포인터: 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하며 처리

# 투포인터 문제1: 특정한 합을 가지는 부분 연속 수열 찾기
n = 5  # 데이터의 개수 N
m = 5  # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
  # end를 가능한 만큼 이동시키기(부분합이 m보다 작을 때)
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1
  # 부분합이 m일 때 카운트 증가
  if interval_sum == m:
    count += 1
  # 부분합이 m보다 크거나 같을 때 start를 증가시키기
  interval_sum -= data[start]

print(count)

#-----------------------------------------------------------------------
# 투포인터 문제2: 정렬되어 있는 두 리스트의 합집합
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
  # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
  if j >= m or (i < n and a[i] <= b[j]):
    # 리스트 A의 원소를 결과 리스트로 옮기기
    result[k] = a[i]
    i += 1
  # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
  else:
    # 리스트 B의 원소를 결과 리스트로 옮기기
    result[k] = b[j]
    j += 1
  k += 1

# 결과 리스트 출력
for i in result:
  print(i, end=' ')
