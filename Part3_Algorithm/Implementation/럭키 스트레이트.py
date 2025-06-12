#구현7: 럭키 스트레이트
n = input()

lens = len(n)
re1 = 0
re2 = 0

for i in range(lens//2):
    re1 += int(n[i])

for i in range(lens//2, lens):
    re2 += int(n[i])

if re1 == re2:
    print("LUCKY")
else:
    print("REAEY")