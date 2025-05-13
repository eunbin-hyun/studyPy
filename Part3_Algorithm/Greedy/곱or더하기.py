# 그리디2: 곱하기 혹은 더하기
# 0이나 1은 더하기, 나머지는 곱하기

s = input()
k = []

for i in s:
    k.append(i)

result = int(k[0])
for i in range(1, len(k)):
    k[i] = int(k[i])
    if result <= 1 or k[i] <= 1:
        result += k[i]
    else:
        result *= k[i]

print(result)