# 11강 자주 사용되는 표준 라이브러리

# 자주 사용되는 내장함수
# sum()
result = sum([1,2,3,4,5])
print(result)
# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합 (전체 경우의 수 확인 가능)
# 순열 (순서 고려해서 나열)
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# 조합 (순서 고려하지 않고 나열)
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# 중복 순열과 중복 조합
from itertools import product
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# Counter
# 등장 횟수를 세는 기능 제공
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
import math
print(math.gcd(21, 14)) # 최대 공약수
print(math.lcm(21, 14)) # 최소 공배수

