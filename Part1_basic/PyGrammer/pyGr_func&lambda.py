# 10강 함수와 람다 표현식

# 함수 정의하기
def add(a,b):
  return a+b
print(add(3,7))

def add(a,b):
  print("함수의 결과: ", a+b)
add(3,7)

def subtract(a,b):
  return a-b
print(subtract(b=3,a=7))

# gloabl 키워드 
# (global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.)
a = 10

def func():
  global a
  a += 1
  print(a)
  a += 4

func()
print(a)

# array일 때 gloabl 키워드 사용
array = [1,2,3,4,5]

def func():
  array = [3, 4, 5]
  array.append(6)
  print(array)

func()
print(array)

# 여러 개의 반환 값
def operator(a,b):
  add_var = a+b
  subtract_var = a-b
  multiply_var = a*b
  divide_var = a/b
  return add_var, subtract_var, multiply_var, divide_var

a,b,c,d = operator(7,3)
print(a,b,c,d)


# 람다 표현식
# (람다 표현식은 함수를 간단하게 정의할 수 있도록 해줌, 한줄로 작성 가능)
print((lambda a,b: a+b)(3,7))

# 람다 표현식 예제
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def my_key(x):
  return x[1] #두번째 값을 기준으로 정렬
print(sorted(array, key=my_key))

print(sorted(array, key=lambda x:x[1]))

# 여러 개의 리스트에 적용 (map)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a,b: a+b, list1, list2)
print(list(result))