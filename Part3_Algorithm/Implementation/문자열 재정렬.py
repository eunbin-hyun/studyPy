# 구현8: 문자열 재정렬

S = input()
result = []
value = 0

for i in S:
    if i.isdigit():
        value += int(i)
    else:
        result.append(i)

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))