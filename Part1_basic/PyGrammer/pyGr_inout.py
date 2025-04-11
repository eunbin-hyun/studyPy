# 7강 기본입출력

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

print(n)
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

# 입력을 최대한 빠르게 받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 출력
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")
# 출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.")