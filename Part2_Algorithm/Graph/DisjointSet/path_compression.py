# 경로 압축 기법 소스코드
def find_parent(parent, x):
  # 경로 압축: find 함수를 재귀적으로 호출한 뒤 부모 테이블값 갱신
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) 
  return parent[x]