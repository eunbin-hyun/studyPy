# 정렬24: 안테나
# 중간값을 출력하면 된다.

n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n-1)//2])