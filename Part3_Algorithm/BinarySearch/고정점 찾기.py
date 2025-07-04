# 이진탐색28. 고정점 찾기
# 고정점: 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# 이진탐색을 사용해야 O(logN)의 시간복잡도로 문제를 해결할 수 있음 (순차탐색은 O(N)로 시간초과)

def binary_search(array, start, end):
  if start > end:
      return None
  mid = (start + end) //2
  if array[mid] == mid:
      return mid
  elif array[mid] > mid:
      return binary_search(array, start, mid-1)
  else:
      return binary_search(array, mid+1, end)

n = int(input())
array =list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
  print(-1)
else:
  print(index)