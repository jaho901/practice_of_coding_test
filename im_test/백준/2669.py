## 직사각형 네게의 합집합의 면적 구하기

import sys
sys.stdin = open('2669.txt')

data = [list(map(int, input().split())) for _ in range(4)]
# print(data)

# 결과를 담을 행렬 생성
result = [[0]*100 for _ in range(100)]

for i in data:
    # x의 범위 지정
    for x in range(i[0], i[2]):
        # y의 범위 지정
        for y in range(i[1], i[3]):
            # 이미 1이 적혀있는 경우는 중복됨으로 무시하기 위해 조건 지정
            if result[x][y] == 0:
                result[x][y] = 1

total = 0
for j in result:
    total += sum(j)

print(total)