# 재귀함수는 자기 자신을 호출하는 함수
# 재귀함수를 사용하면 종료 조건을 반드시 명시! (무한호출 방지)

def recursive_function(i):

  if i == 100:
    return
  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)