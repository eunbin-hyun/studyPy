# 너비우선탐색
# 큐 자료구조를 이용하여 가장 가까운 노드부터 탐색

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  queue = deque([start])  # 시작 노드를 큐에 넣고
  visited[start] = True   # 방문처리
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],         # 0번 노드는 없으므로 비워둠
  [2, 3, 8],  # 1번 ↔ 2, 3, 8
  [1, 7],     # 2번 ↔ 1, 7
  [1, 4, 5],  # 3번 ↔ 1, 4, 5
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)