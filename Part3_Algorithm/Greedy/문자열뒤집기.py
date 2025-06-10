# 그리디3: 문자열 뒤집기

# 내 풀이: 기본적인 아이디어는 같음
s = input()
i = s[0]
k = [s[0]]

for j in range(1,len(s)):
    if i != s[j]:
        k.append(s[j])
    i = s[j]

print(min(k.count('0'), k.count('1')))

# -----------------------------------------------------
# 답안 풀이
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))