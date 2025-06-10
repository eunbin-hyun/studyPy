# 그리디4: 볼링공 고르기
# 서로다른 무게의 볼링공 고르는 경우의 수

# 내 풀이: 하나씩 비교

n, m = map(int, input().split())
w = list(map(int, input().split()))
count = 0

for i in range(len(w)):
    target = w[i]
    for j in range(i+1, len(w)):
        if target != w[j]:
            count += 1 

print(count)

#----------------------------------------------------
# 답안 풀이: 무게별로 볼링공 개수 세기(조합이용)

n,m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1 # 각 무게에 해당하는 볼링공의 개수 카운트

result = 0

for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)
