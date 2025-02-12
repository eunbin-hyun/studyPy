# 8강 조건문과 반복문

# 조건문
a = 5
if a >= 0:
  print("a >= 0")
elif a >= -10:
  print("0 > a >= -10")
else:
  print("-10 > a")

if a > 0 and a < 10:
  print("0 < a < 10")


# 반복문

# while문(무한루프일때 주로 씀)
i = 1
result = 0

while i <= 9:
  result += i
  i += 1

print(result)

# for문(많이사용)
array = [9,8,7,6,5]
for x in array:
  print(x)

# range 함수
result = 0
for i in range(1,10):
  result += i
print(result)

# continue (반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 사용)
result = 0
for i in range(1,4):
  if i % 2 == 0:
    continue
  result += i
print(result)

# break (반복문을 즉시 탈출하고자 할 때 사용)
i = 1
while True:
  print("현재 i의 값:", i)
  if i == 5:
    break
  i += 1

# for문 예제1
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2,4}

for i in range(5):
  if i+1 in cheating_student_list:
    continue
  if scores[i] >= 80:
    print(i+1, "번 학생은 합격입니다.")

# for문 예제2
for i in range(2,10):
  for j in range(1,10):
    print(i, "X", j, "=", i*j)
  print()