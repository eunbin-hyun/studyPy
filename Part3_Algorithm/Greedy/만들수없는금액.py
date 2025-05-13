# 그리디4: 만들 수 없는 금액

n = int(input())
list = list(map(int, input().split()))
list.sort()
s = False
l = False

for num in range(1, n*list[-1]):
    if num in list:
        continue
    k = 0
    for i in list:
        k += i
        if k == num:
            break
        elif k > num:
            for j in list:
                k -= j 
                if k == num:
                    l = True
                    break
                elif k <= 0:
                    s = True
                    break
        else:
            continue
        if s == True or l == True:
            break
    if s == True:
        break

print(num)