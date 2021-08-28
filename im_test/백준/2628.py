## 종이자르기

import sys
sys.stdin = open('2628.txt')

w, h = map(int, input().split())
N = int(input())
dash_list = [list(map(int, input().split())) for _ in range(N)]
width = [0]
height = [0]

# 이 문제는 규칙을 찾는것이 가장 중요하다!!!
# 규칙은 뭐냐?? -> 문제에서 <그림 2>를 보자
# 가로로 다 자르고 나면 나오는 길이는 (4, 6)이다.
# 세로로 다 자르고 나면 나오는 길이는 (2, 1, 5)이다.
# 여기서 최댓값들끼리의 곱이 가장 큰 면적이 된다. ==> 6 * 5 = 30이 가장 큰 면적

for i in dash_list:
    if i[0] == 0:
        # 가로로 자를 기준  
        width.append(i[1])
    else:
        # 세로로 자를 기준
        height.append(i[1])

# 정렬시킨 이후 가장 마지막 값인 W, H를 넣어준다.
width = sorted(width)
width.append(h)
height = sorted(height)
height.append(w)

# 그 값들간의 차이 중 최댓값을 max_w, max_h로 저장한 다음 곱을 프린트해준다.!!
max_w = width[1] - width[0]
max_h = height[1] - height[0]
for i in range(1, len(width)):
    n = width[i] - width[i-1]
    if max_w < n:
        max_w = n
for j in range(1, len(height)):
    m = height[j] - height[j-1]
    if max_h < m:
        max_h = m
print(max_w*max_h)





