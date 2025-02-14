# 두 배열의 원소 교체
# A배열의 합을 최대로 하기위해 B배열과 K번 교체 가능하다
# 아이디어: A배열의 원소들을 오름차순으로 정렬, B배열의 원소들을 내림차순으로 정렬
# 순차적으로 비교하면서 A배열의 원소가 작을경우 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
