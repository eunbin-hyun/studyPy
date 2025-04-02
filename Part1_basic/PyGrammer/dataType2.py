#5강 문자열,튜플 자료형

# #문자열
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# #문자열 연산 (문자열은 변경불가)
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])


# #튜플
# #튜플은 리스트와 유사하지만, 변경 불가하고 소괄호 이용
tuple_a = (1,2,3,4,5,6,7,8,9)
print(tuple_a)
print(tuple_a[3])
print(tuple_a[1:4])


# 6강 사전,집합 자료형

# 사전 자료형은 키와 값의 쌍을 데이터
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

# #키 데이터만 담은 리스트
key_list = data.keys()
# #값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)
# #각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])


# #집합 자료형
# #중복 허용X, 순서가 없음
data = set([1,1,2,3,4,4,5])
print(data)
data ={1,1,2,3,4,4,5}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

data = set([1,2,3])
print(data)

data.add(4)
print(data)

data.update([5,6])
print(data)

data.remove(3)
print(data)

