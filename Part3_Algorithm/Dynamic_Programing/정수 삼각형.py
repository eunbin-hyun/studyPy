# 다이나믹 프로그래밍 32. 정수 삼각형

n = int(input())
tri = []

for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            left = 0
        else:
            left = tri[i-1][j-1]

        if j == len(tri[i])-1:
            right =0
        else:
            right = tri[i-1][j]
        tri[i][j] = tri[i][j] + max(left, right)

print(max(tri[n-1]))
