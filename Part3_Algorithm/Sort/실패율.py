# 정렬25: 실패율
# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

N = int(input())
stages = list(map(int, input().split()))
answer = []
length = len(stages)

for i in range(1,N+1):
    count = stages.count(i)

    # 실패율 계산 
    if length == 0:
        fail = 0
    else:
        fail = count / length

    answer.append((i, fail)) # 이 때 i에 대해 오름차순으로 정렬되어있음
    length -= count

answer = sorted(answer, key=lambda t: t[1], reverse=True) # 실패율에 대해 내림차순으로 정렬
answer = [i[0] for i in answer]
print(answer)