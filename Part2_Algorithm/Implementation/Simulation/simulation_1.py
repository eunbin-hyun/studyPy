# 구현 중 시뮬레이션 유형: 일련의 명령에 따라서 개체를 차례대로 이동

# 시뮬레이션 문제1: 상하좌우 문제

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향 
dx = [0, 0, -1, 1] # x축은 행을 의미해서 위아래 움직임
dy = [-1, 1, 0, 0] # y축은 열을 의미해서 좌우 움직임
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)

