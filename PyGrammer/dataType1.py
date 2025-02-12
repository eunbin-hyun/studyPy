# 4강 리스트자료형

#유효실수e
a = int(1e9)
print(a)

#실수형
b = 0.3 + 0.6
print(b)

if b == 0.9:
  print(True)
else:
  print(False)

#round 함수
a= 0.3 + 0.6
print(round(a, 3)) #4자리에서 반올림

#연산
a=7
b=3

#나누기
print(a/b)
#나머지
print(a%b)
#몫
print(a//b)

#리스트
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])

#크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
n=10
a=[0]*n
print(a)

#인덱싱
a = [1,2,3,4,5,6,7,8,9]
print(a[-1])
print(a[-3])

#슬라이싱
print(a[1:4])

#리스트 컴프리헨션
array = [i for i in range(10)]
print(array)

array = [i for i in range(20) if i%2 == 1]
print(array)

array = [i*i for i in range(1,10)]
print(array)

#2차원 리스트 초기화
n=4
m=3
array = [[0]*m for _ in range(n)]
print(array)

#리스트 관련 메서드
a = [1,4,3]
print("기본 리스트: ", a)
#리스트에 원소 삽입
a.append(2)
print("삽입: ", a)
#오름차순 정렬
a.sort() 
print("오름차순 정렬: ", a)
#내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)
#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)
#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))
#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

#특정 값 데이터 모두 삭제
a=[1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result)
