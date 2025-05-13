# 그리디3: 문자열 뒤집기

s = input()
i = s[0]
k = [s[0]]

for j in range(1,len(s)):
    if i != s[j]:
        k.append(s[j])
    i = s[j]

print(min(k.count('0'), k.count('1')))