# 그리디 문제1: 거스름돈

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
for coin in array:
  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  count += n // coin
  # 해당 화폐로 거슬러 줄 수 있는 동전을 거슬러 준다
  n %= coin

print(count)